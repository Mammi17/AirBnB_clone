#!/usr/bin/python3
"""Define the console"""

import cmd
import json
import re
import models
# from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Custom console class"""
    prom = '(hbnb) '

    def my_errors(self, line, numb_of_args):
        """Displays error messages to user
        line(any): gets user input using command line
        num_of_args(int): number of input arguments

        Description:
            Displays output to the use based on
            the input commands."""
        clsse = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        sms = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(sms[0])
            return 1
        arg = line.split()
        if numb_of_args >= 1 and arg[0] not in clsse:
            print(sms[1])
            return 1
        elif numb_of_args == 1:
            return 0
        if numb_of_args >= 2 and len(arg) < 2:
            print(sms[2])
            return 1
        serv = storage.all()

        for a in range(len(arg)):
            if arg[a][0] == '"':
                arg[a] = arg[a].replace('"', "")
        key = arg[0] + '.' + arg[1]
        if numb_of_args >= 2 and key not in serv:
            print(sms[3])
            return 1
        elif numb_of_args == 2:
            return 0
        if numb_of_args >= 4 and len(arg) < 3:
            print(sms[4])
            return 1
        if numb_of_args >= 4 and len(arg) < 4:
            print(sms[5])
            return 1
        return 0

    def handle_empty_line(self, line):
        """Eliminates empty lines"""
        return False

    def do_quit(self, line):
        """Handles the 'quit' command
        line: input argument for quiting the terminal"""
        return True

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d
        line: input argument for quiting the terminal"""
        return True

    def do_create(self, line):
        """Creates a new instance of @cls_name class,
        and prints the new instance's ID.
        line: Arguments to enter with command: <class name>
        Example: 'create User'"""
        if (self.my_errors(line, 1) == 1):
            return
        arg = line.split(" ")

        objet = eval(arg[0])()
        objet.save()

        print(objet.id)
        """args[0] contains class name, create new instance
        of that class updates 'updated_at' attribute,
        and saves into JSON file"""

    def do_show(self, line):
        """Prints a string representation of an instance.
        line: to enter with command <class name> <id>
        Example: 'show User 1234-1234-1234'"""
        if (self.my_errors(line, 2) == 1):
            return
        arg = line.split()
        serv = storage.all()
        if arg[1][0] == '"':
            arg[1] = arg[1].replace('"', "")
        key = arg[0] + '.' + arg[1]
        print(serv[key])

    def do_destroy(self, arg):
        """Deletes an instance of a certain class.
        arg: to enter with command: <class name> <id>
        Example: 'destroy User 1234-1234-1234'"""
        if (self.my_errors(arg, 2) == 1):
            return
        line = arg.split()
        serv = storage.all()
        if line[1][0] == '"':
            line[1] = line[1].replace('"', "")
        key = line[0] + '.' + line[1]
        del serv[key]
        storage.save()

    def do_all(self, line):
        """Shows all instances, or instances of a certain class
        line(args): enter with command (optional): <class name>
        Example: 'all' OR 'all User'"""
        serv = storage.all()
        if not line:
            print([str(x) for x in serv.values()])
            return
        arg = line.split()
        if (self.my_errors(line, 1) == 1):
            return
        print([str(b) for b in serv.values()
               if b.__class__.__name__ == arg[0]])

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating an attribute
        line: receives the commands:
        <class name> <id> <attribute name> "<attribute value>"
        Example: 'update User 1234-1234-1234 my_name "Bob"'"""
        if (self.my_errors(line, 4) == 1):
            return
        arg = line.split()
        serv = storage.all()
        for a in range(len(arg[1:]) + 1):
            if arg[a][0] == '"':
                arg[a] = args[a].replace('"', "")
        key = arg[0] + '.' + arg[1]
        attrik = arg[2]
        attriv = arg[3]
        try:
            if attriv.isdigit():
                attriv = int(attriv)
            elif float(attriv):
                attriv = float(attriv)
        except ValueError:
            pass
        clsse_attri = type(serv[key]).__dict__
        if attrik in clsse_attri.keys():
            try:
                attriv = type(clsse_attri[attrik])(attriv)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(serv[key], attrik, attriv)
        storage.save()

    def my_count(self, class_n):
        """Method counts instances of a certain class"""
        count_inst = 0
        for inst_objet in storage.all().values():
            if inst_objet.__class__.__name__ == class_n:
                count_inst += 1
        print(count_inst)

    def default(self, line):
        """Creates a list representations of functional models
        Then use the functional methods to implement user
        commands, by validating all the input commands"""
        nom = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]

        commande = {"all": self.do_all,
                    "count": self.my_count,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "update": self.do_update}

        arg = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if arg:
            arg = arg.groups()
        if not arg or len(arg) < 2 or arg[0] not in nom \
                or arg[1] not in commande.keys():
            super().default(line)
        return

        if arg[1] in ["all", "count"]:
            commande[arg[1]](arg[0])
        elif arg[1] in ["show", "destroy"]:
            commande[arg[1]](arg[0] + ' ' + arg[2])
        elif arg[1] == "update":
            param = re.match(r"\"(.+?)\", (.+)", arg[2])
            if param.groups()[1][0] == '{':
                dict_param = eval(param.groups()[1])
                for a, b in dict_param.items():
                    commande[arg[1]](arg[0] + " " + param.groups()[0] +
                                      " " + a + " " + str(b))
            else:
                reste = param.groups()[1].split(", ")
                commande[arg[1]](arg[0] + " " + param.groups()[0] + " " +
                                  reste[0] + " " + reste[1])


if __name__ == '__main__':
    clic = HBNBCommand()
    clic.cmdloop()
