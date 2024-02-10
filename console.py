#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    the HolbertonBnB command interpreter.
    """
    prompt = "(hbnb) "


    def do_quit(self, arg):
        """ exit the program."""
        return True
    def do_EOF(self, line):
        """Exit the console """
        print()
        return True








if __name__ == '__main__':
    HBNBCommand().cmdloop()
