#!/usr/bin/python3
"""module containing the console for AirBnB"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """cmd interpreter for managing AirBnB objects"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Review": Review,
        "Place": Place,
        "City": City,
        "Amenity": Amenity,
    }
    all_objects = storage.all()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ignore empty lines"""
        pass

    def do_create(self, class_name):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        usage: create $class_name
        """

        if class_name:
            if class_name in HBNBCommand.classes:
                obj = HBNBCommand.classes[class_name]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = args.split()

        if args:
            if args[0] in HBNBCommand.classes:
                if len(args) > 1:
                    obj_key = f"{args[0]}.{args[1]}"
                    if obj_key in HBNBCommand.all_objects:
                        print(HBNBCommand.all_objects[obj_key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = args.split()

        if args:
            if args[0] in HBNBCommand.classes:
                if len(args) > 1:
                    obj_key = f"{args[0]}.{args[1]}"
                    if obj_key in HBNBCommand.all_objects:
                        del HBNBCommand.all_objects[obj_key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = args.split()
        my_list = []
        if args:
            if args[0] in HBNBCommand.classes:
                for key, value in HBNBCommand.all_objects.items():
                    if type(value).__name__ == args[0]:
                        my_list.append(value.__str__())
            else:
                print("** class doesn't exist **")
                return
        else:
            for key, value in HBNBCommand.all_objects.items():
                my_list.append(value.__str__())
        print(my_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)"""
        args = args.split()

        if args:
            if args[0] in HBNBCommand.classes:
                if len(args) > 1:
                    obj_key = f"{args[0]}.{args[1]}"
                    if obj_key in HBNBCommand.all_objects:
                        if len(args) > 2:
                            if len(args) > 3:
                                obj = self.all_objects[obj_key]
                                value = type(args[2])(args[3].strip('"'))
                                setattr(obj, args[2], value)
                                obj.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
