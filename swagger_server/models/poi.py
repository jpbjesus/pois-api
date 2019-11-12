# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.poi_geocode import POIGeocode
from swagger_server import util


class POI(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str = None, type: str = None, address: str = None, phone_number: str = None, geocode: POIGeocode = None, opening_hours: List[str] = None, website: str = None, photos: List[str] = None):  # noqa: E501
        """POI - a model defined in Swagger

        :param name: The name of this POI.  # noqa: E501
        :type name: str
        :param type: The types of this POI.  # noqa: E501
        :type type: List[str]
        :param address: The address of this POI.  # noqa: E501
        :type address: str
        :param phone_number: The phone_number of this POI.  # noqa: E501
        :type phone_number: str
        :param geocode: The geocode of this POI.  # noqa: E501
        :type geocode: POIGeocode
        :param opening_hours: The opening_hours of this POI.  # noqa: E501
        :type opening_hours: List[str]
        :param website: The website of this POI.  # noqa: E501
        :type website: str
        :param photos: The photos of this POI.  # noqa: E501
        :type photos: List[str]
        """
        self.swagger_types = {
            'name': str,
            'type': List[str],
            'address': str,
            'phone_number': str,
            'geocode': POIGeocode,
            'opening_hours': List[str],
            'website': str,
            'photos': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'address': 'address',
            'phone_number': 'phone_number',
            'geocode': 'geocode',
            'opening_hours': 'opening_hours',
            'website': 'website',
            'photos' : 'photos'
        }

        self._name = name
        self._type = type
        self._address = address
        self._phone_number = phone_number
        self._geocode = geocode
        self._opening_hours = opening_hours
        self._website = website,
        self._photos = photos 

    @classmethod
    def from_dict(cls, dikt) -> 'POI':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The POI of this POI.  # noqa: E501
        :rtype: POI
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this POI.

        Contains the human-readable name for the returned result. For establishment results, this is usually the canonicalized business name.  # noqa: E501

        :return: The name of this POI.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this POI.

        Contains the human-readable name for the returned result. For establishment results, this is usually the canonicalized business name.  # noqa: E501

        :param name: The name of this POI.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self) -> List[str]:
        """Gets the type of this POI.

        :return: The type of this POI.
        :rtype: Lsit[str]
        """
        return self._type

    @type.setter
    def type(self, type: List[str]):
        """Sets the type of this POI.

        :param type: The type of this POI.
        :type type: List[str]
        """
        allowed_values = ["accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery", "bank", "bar", "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "bus_station", "cafe", "campground", "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery", "church", "city_hall", "clothing_store", "convenience_store", "courthouse", "dentist", "department_store", "doctor", "drugstore", "electrician", "electronics_store", "embassy", "fire_station", "florist", "funeral_home", "furniture_store", "gas_station", "grocery_or_supermarket", "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "hospital", "insurance_agency", "jewelry_store", "laundry", "lawyer", "library", "light_rail_station", "liquor_store", "local_government_office", "locksmith", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_rental", "movie_theater", "moving_company", "museum", "night_club", "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "plumber", "police", "post_office", "primary_school", "real_estate_agency", "restaurant", "roofing_contractor", "rv_park", "school", "secondary_school", "shoe_store", "shopping_mall", "spa", "stadium", "storage", "store", "subway_station", "supermarket", "synagogue", "taxi_stand", "tourist_attraction", "train_station", "transit_station", "travel_agency", "university", "veterinary_care", "zoo", "point_of_interest", "establishment"]  # noqa: E501
        
        # for t in type:
        #     if t not in allowed_values:
        #         raise ValueError(
        #             "Invalid value for `type` ({0}), must be one of {1}"
        #             .format(type, allowed_values)
        #         )
        self._type = type

    @property
    def address(self) -> str:
        """Gets the address of this POI.

        Is a string containing the human-readable address of this place. Often this address is equivalent to the postal address.  # noqa: E501

        :return: The address of this POI.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this POI.

        Is a string containing the human-readable address of this place. Often this address is equivalent to the postal address.  # noqa: E501

        :param address: The address of this POI.
        :type address: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def phone_number(self) -> str:
        """Gets the phone_number of this POI.

        Contains the places phone number in its local format.  # noqa: E501

        :return: The phone_number of this POI.
        :rtype: str
        """
        return self._phone_number.replace(" ", "") if self._phone_number is not None else self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        """Sets the phone_number of this POI.

        Contains the places phone number in its local format.  # noqa: E501

        :param phone_number: The phone_number of this POI.
        :type phone_number: str
        """

        self._phone_number = phone_number

    @property
    def geocode(self) -> POIGeocode:
        """Gets the geocode of this POI.


        :return: The geocode of this POI.
        :rtype: POIGeocode
        """
        return self._geocode

    @geocode.setter
    def geocode(self, geocode: POIGeocode):
        """Sets the geocode of this POI.


        :param geocode: The geocode of this POI.
        :type geocode: POIGeocode
        """
        if geocode is None:
            raise ValueError("Invalid value for `geocode`, must not be `None`")  # noqa: E501

        self._geocode = geocode

    @property
    def opening_hours(self) -> List[str]:
        """Gets the opening_hours of this POI.

        Is an array of seven strings representing the formatted opening hours for each day of the week.   # noqa: E501

        :return: The opening_hours of this POI.
        :rtype: List[str]
        """
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, opening_hours: List[str]):
        """Sets the opening_hours of this POI.

        Is an array of seven strings representing the formatted opening hours for each day of the week.   # noqa: E501

        :param opening_hours: The opening_hours of this POI.
        :type opening_hours: List[str]
        """

        self._opening_hours = opening_hours

    @property
    def website(self) -> str:
        """Gets the website of this POI.

        Lists the authoritative website for this place, such as a business homepage.  # noqa: E501

        :return: The website of this POI.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website: str):
        """Sets the website of this POI.

        Lists the authoritative website for this place, such as a business homepage.  # noqa: E501

        :param website: The website of this POI.
        :type website: str
        """

        self._website = website

    @property
    def photos(self) -> List[str]:
        """Gets the photos of this POI.

        :return: The photos of this POI.
        :rtype: List[str]
        """
        return self._photos

    @photos.setter
    def photos(self, photos: List[str]):
        """Sets the photos of this POI.

        :param photos: The photos of this POI.
        :type photos: List[str]
        """

        self._photos = photos
