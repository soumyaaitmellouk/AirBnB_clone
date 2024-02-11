#!/usr/bin/python3
"""Define The Base Modul Class is the parent class"""
import models
from datetime import datetime
import uuid


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialisation de la fonction init
        :param args: not used
        :param kwargs:used
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        isoformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if (key == "created_at") or (key == "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, isoformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
         of __dict__ of the instance"""
        new_dic = self.__dict__.copy()
        new_dic["created_at"] = self.created_at.isoformat()
        new_dic["updated_at"] = self.updated_at.isoformat()
        new_dic["__class__"] = self.__class__.__name__

        return new_dic

    def __str__(self):
        """should print: [<class name>](<self.id>) <self.__dict__>"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
