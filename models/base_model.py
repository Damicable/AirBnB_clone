#!/usr/bin/python3
"""A module that creates the base model dfining common attributes/methods"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model class to instantiate the foundationa Airbnb data unit(s)"""

    def __init__(self, *args, **kwargs):
        """
        Initiate an instance of the base model
        Arguments:
            @args: Variable arguments passed (non named)
            @kwargs: Variable namd arguments
        """
        kw_keys = list(kwargs.keys())
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if "__class__" in kw_keys:
            kw_keys.remove("__class__")
        if (len(kw_keys) > 0):
            for key in kw_keys:
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(kwargs[key], fmt))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            current_time = datetime.utcnow()
            self.created_at = current_time
            self.updated_at = current_time

    def __str__(self):
        """Specify the output of printing a class instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        An instant method to update the public instane attribute created_at
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Serialize the dict representation of a class instance to json"""
        dict_clone = self.__dict__
        dict_new = {}
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        for key in dict_clone.keys():
            if key in ["created_at", "updated_at"]:
                dict_new[key] = dict_clone[key].strftime(fmt)
            else:
                dict_new[key] = dict_clone[key]
        dict_new["__class__"] = self.__class__.__name__
        return dict_new
