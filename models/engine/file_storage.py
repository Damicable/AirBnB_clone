#!/usr/bin/python3
"""
    Module to declare the file storage class
    with its attributes and methods
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class to serialize instances to JSON
    and deserialize JSONs to instnaces
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all declared attributes of the instance
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the obj dict as the value for key <obj class name>.id
        """
        if obj is not None:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Serializes the __objects attribute to the file path __file_path
        """
        tmp_dict = {}
        for i, j in FileStorage.__objects.items():
            tmp_dict[i] = j.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(tmp_dict, f)

    def reload(self):
        """
        Deserialize the JSON file in __file_path into the __objects dict
        if file exists
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                des_obj = json.load(f)
                for i in des_obj.values():
                    tmp_name = i.pop("__class__")
                    self.new(eval(tmp_name)(**i))
        except FileNotFoundError:
            pass
