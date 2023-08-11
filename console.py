#!/usr/bin/python3
"""module containing the console for AirBnB"""

import cmd


class HBNBCommand(cmd.Cmd):
    """cmd interpreter for managing AirBnB objects"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ignore empty lines"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
