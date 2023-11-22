#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from .user import User
from .state import State
from .city import City
from .amenity import Amenity
from .place import Place
from .review import Review
from .base_model import BaseModel

if getenv("HBNB_TYPE_STORAGE") == "db":
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

__all__ = ["storage", "User", "State", "City", "Amenity", "Place", "Review", "BaseModel"]
