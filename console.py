#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import models
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

vcs = [
    'BaseModel',
    'User',
    'State',
    'City',
    'Place',
    'Amenity',
    'Review'
]


def strip_key(k):
    """Extract argument value"""
    prtn = re.search(r'[a-zA-Z]+.*[a-zA-Z]', k)
    if prtn:
        return prtn.group()
    else:
        return ""


def strip_val(v):
    """Stip value string"""
    return v.strip().strip('"').strip("'").strip('}')


class HBNBCommand(cmd.Cmd):
    """HBNB command class"""
    prompt = '(hbnb) '

    def default(self, arg):
        """Default behavior to handle Class.method commands"""
        exec_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        try:
            if "." in arg and arg.endswith(")"):
                cmds1 = arg.split(".")
                cmds2 = cmds1[1].split("(")
                cmd_args = cmds1[0]
                if len(cmds2[1]) > 1:
                    xtra_args = cmds2[1][:-1].split(',')
                    cmd_args += " "
                    cmd_args += xtra_args[0] + " "
                    if len(xtra_args) > 1 and '{' in xtra_args[1]:
                        cnt = 0
                        for k in xtra_args[1:]:
                            if cnt != 0:
                                cmd_args += " "
                            sep = k.split(':')
                            cmd_args += strip_key(sep[0])
                            cmd_args += " "
                            cmd_args += strip_val(sep[1])
                            cnt += 1
                    else:
                        for i in xtra_args:
                            cmd_args += i
                return exec_dict[cmds2[0]](cmd_args)
        except (AttributeError, IndexError, KeyError):
            pass
        print("*** Unknown syntax: {}".format(arg))
        return False

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
        elif arg_list[0] not in vcs:
            print("** class doesn't exist **")
        else:
            class_val = globals()[arg_list[0]]
            class_instance = class_val()
            class_instance.save()
            print(class_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in vcs:
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

    def do_count(self, args):
        """Counts the number of instances of a particular class"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in vcs:
            print("** class doesn't exist **")
        saved_instances = storage.all()
        num = 0
        for i in list(saved_instances.keys()):
            if i.startswith(arg_list[0]):
                num += 1
        print(num)

    def do_destroy(self, args):
        """Deletes a created instance by class name"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in vcs:
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
        has_cls = len(arg_list) > 0 and arg_list[0] in vcs
        if len(arg_list) > 0 and arg_list[0] not in vcs:
            print("** class doesn't exist **")
        else:
            ob = list(storage.all().values())
            if has_cls:
                f = filter(lambda x: x.__class__.__name__ == arg_list[0], ob)
                obj_sl = list(map(lambda x: x.__str__(), f))
            elif len(arg_list) == 0:
                obj_sl = list(map(lambda x: x.__str__(), ob))
            print(obj_sl)

    def do_update(self, args):
        """Updates an instance based on classname and id"""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in vcs:
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
        if len(arg_list) >= 4:
            if arg_list[2] in targ.__class__.__dict__.keys():
                updtype = type(targ.__class__.__dict__[arg_list[2]])
                targ.__dict__[arg_list[2]] = updtype(arg_list[3])
            else:
                targ.__dict__[arg_list[2]] = arg_list[3]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
