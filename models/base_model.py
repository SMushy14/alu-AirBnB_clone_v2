#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)  # No parentheses
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)  # No parentheses

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        expected_keys = ['id', 'created_at', 'updated_at']

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key not in expected_keys and key != '__class__':
                    raise KeyError("Unexpected key: {}".format(key))

                if key in ('created_at', 'updated_at'):
                    try:
                        setattr(self, key, datetime.fromisoformat(value))
                    except ValueError:
                        raise ValueError("Incorrect date format for key: {}".format(key))
                else:
                    setattr(self, key, value)

            # Set defaults if not provided in kwargs
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """Deletes this BaseModel instance from the storage"""
        from models import storage
        storage.delete(self)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        res = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    res[key] = value.isoformat()
                else:
                    res[key] = value
        res['__class__'] = self.__class__.__name__
        return res
