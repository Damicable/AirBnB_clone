#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
