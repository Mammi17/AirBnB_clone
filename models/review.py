#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review
    Attributes:
        place_id: Place id
        user_id: User id
        text: text of the review"""
    place_id = ""
    user_id = ""
    text = ""
