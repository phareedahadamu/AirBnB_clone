#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Features of the storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the stored object dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """Serializes stored objects in __objects to the JSON file
        __file_path."""
        my_dict = {obj: FileStorage.__objects[obj].to_dict()
                   for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path) as f:
            mydict = json.load(f)
            for v in mydict.values():
                cls_name = v["__class__"]
                self.new(eval(cls_name)(**v))
