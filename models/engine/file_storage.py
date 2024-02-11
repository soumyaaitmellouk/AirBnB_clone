#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    
    __file_path . the file path
    __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        obj_dict = {}
        for key, obj in odict.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for var in obj_dict.values():
                    cls_name = var["__class__"]
                    del var["__class__"]
                    self.new(eval(cls_name)(**var))
        except FileNotFoundError:
            return
