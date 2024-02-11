#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__, obj.id] = obj
    
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[f"{key[0]}-{key[1]}"] = obj.to_dict() 
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f, default=str)
    
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name, obj_id = key.split(',')
                    obj = eval(cls_name)(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            return
