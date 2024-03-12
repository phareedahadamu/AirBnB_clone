#!/usr/bin/python3
""" Defines a class HBNBCommand"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Features of HBNB command interpreter"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                  "Review"]

    def do_EOF(self, line):
        """Exits the program"""
        print()
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            print("{}".format(eval(args[0])().id))
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            obj_key = str(args[0]) + "." + str(args[1])
            if obj_key not in all_objs:
                print("** no instance found **")
            else:
                my_obj = all_objs[obj_key]
                print(my_obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file)."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            obj_key = str(args[0]) + "." + str(args[1])
            if obj_key not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[obj_key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name"""
        args = shlex.split(line)
        if len(args) > 0 and args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            my_list = []
            for value in all_objs.values():
                if len(args) == 0:
                    my_list.append(value.__str__())
                elif len(args) > 0 and value.__class__.__name__ == args[0]:
                    my_list.append(value.__str__())
            print(my_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) > 1:
            all_objs = storage.all()
            obj_key = str(args[0]) + "." + str(args[1])
            if obj_key not in all_objs:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                my_obj = all_objs[obj_key]
                if args[2] in my_obj.__class__.__dict__.keys():
                    att_type = type(my_obj.__class__.__dict__[args[2]])
                    my_obj.__dict__[args[2]] = att_type(args[3])
                else:
                    my_obj.__dict__[args[2]] = args[3]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
