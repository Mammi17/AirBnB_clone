#!/usr/bin/python3
"""Custom base class for the entire project"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Custom base for all the classes in the AirBnb console project
    Arttributes:
        id: handles unique user identity
        created_at: assigns with the current datetime when
        an instance is created
        updated_at: updates current datetime
    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save: updates instance arttributes with current datetime
        to_dict: returns the dictionary values of the instance obj"""

    def __init__(self, *args, **kwargs):
        """Public instance artributes initialization
        after creation"""
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        val, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(val)
                else:
                    self.__dict__[key] = val

    def __str__(self):
        """Returns string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute:
        'updated_at' - with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ instance"""
        map_objet = {}
        for key, val in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objet[key] = val.isoformat()
            else:
                map_objet[key] = val
        map_objet["__class__"] = self.__class__.__name__
        return map_objet
