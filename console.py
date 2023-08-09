#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import models
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB command class"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the console on end of file"""
        return True

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def emptyline(self):
        """Ensure nothing happens when enter is hit"""
        pass

    def do_create(self, args):
        """Create a base model instance"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            base_instance = BaseModel()
            base_instance.save()
            print(base_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            saved_instances = storage.all()
            inst_key = "{}.{}".format(arg_list[0], arg_list[1])
            if inst_key not in list(saved_instances.keys()):
                print("** no instance found **")
            else:
                print(saved_instances[inst_key])

    def do_destroy(self, args):
        """Deletes a created instance by class name"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            saved_instances = storage.all()
            inst_key = "{}.{}".format(arg_list[0], arg_list[1])
            if inst_key not in list(saved_instances.keys()):
                print("** no instance found **")
            else:
                del saved_instances[inst_key]
                storage.save()

    def do_all(self, args):
        """Displays a string representation of all instances"""
        arg_list = shlex.split(args)
        has_cls = len(arg_list) > 0 and arg_list[0] == 'BaseModel'
        if len(arg_list) > 0 and arg_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            ob = list(storage.all().values())
            if has_cls:
                f = filter(lambda x: x.__class__.__name__ == arg_list[0], ob)
                obj_sl = list(map(lambda x: x.__str__(), f))
            elif len(argl) == 0:
                obj_sl = list(map(lambda x: x.__str__(), ob))
            print(obj_sl)

    def do_update(self, args):
        """Updates an instance based on classname and id"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] != 'BaseModel':
            print("** class doesn't exist **")
            return False
        if len(arg_list) < 2:
            print("** instance id missing **")
            return False
        saved_instances = storage.all()
        inst_key = "{}.{}".format(arg_list[0], arg_list[1])
        if inst_key not in list(saved_instances.keys()):
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            print("** value missing **")
            return False
        targ = saved_instances[inst_key]
        if len(arg_list) == 4:
            if arg_list[2] in targ.__class__.__dict__.keys():
                updtype = type(targ.__class__.__dict__[arg_list[2]])
                targ.__dict__[arg_list[2]] = updtype(arg_list[3])
            else:
                targ.__dict__[arg_list[2]] = arg_list[3]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
