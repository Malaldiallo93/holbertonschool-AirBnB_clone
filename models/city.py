#!/usr/bin/python3
"""City class module"""


from models.base_model import BaseModel


class City(BaseModel):
    """Defines the City class which inherits from BaseModel
    """
    state_id = ""
    name = ""
