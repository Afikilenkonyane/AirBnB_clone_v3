#!/usr/bin/python3
"""
Views for AirBnB_clone_v3
"""

from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

imports for each subdirectory
api.v1.views.index import IndexView
api.v1.views.states import StateView
api.v1.views.cities import CityView  # Assuming CityView exists
api.v1.views.amenities import AmenityView  # Assuming AmenityView exists
api.v1.views.users import UserView  # Assuming UserView exists
pi.v1.views.places import PlaceView  # Assuming PlaceView exists
api.v1.views.places_reviews import
