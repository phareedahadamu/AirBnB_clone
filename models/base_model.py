#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
import datetime
import models


class BaseModel:
    """Features if the class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Instantiation of BaseModel."""
        if kwargs is not None and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.datetime.fromisoformat(v)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ The string representation of BaseModel"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """ Updates the updated_at attribute with current time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Dictionary representation of BaseModel"""
        my_dict = self.__dict__.copy()
        cr_at = datetime.datetime.isoformat(self.created_at)
        up_at = datetime.datetime.isoformat(self.updated_at)
        my_dict['created_at'] = cr_at
        my_dict['updated_at'] = up_at
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
