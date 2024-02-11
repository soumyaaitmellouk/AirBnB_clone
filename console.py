#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    the HolbertonBnB command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the console """
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
