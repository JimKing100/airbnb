""" SQLAlchemy models for Test """

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class users(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(355), nullable=False)
    first_name = DB.Column(DB.String(60), nullable=False)
    last_name = DB.Column(DB.String(60), nullable=False)
    city = DB.Column(DB.String(255))
    state = DB.Column(DB.String(2))
    date_of_birth = DB.Column(DB.Date)
    profile_image_id = DB.Column(DB.Integer)

    def __repr__(self):
        return '<users {}>'.format(self.name)


class listings(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"), nullable=False)
    property_type_id = DB.Column(DB.Integer, DB.ForeignKey("property_types.id"), nullable=False)
    neighborhood_id = DB.Column(DB.Integer, DB.ForeignKey("neighborhoods.id"), nullable=False)
    room_types = DB.Column(DB.String(60), nullable=False)
    accommodates = DB.Column(DB.Integer, nullable=False)
    bedrooms = DB.Column(DB.Integer, nullable=False)
    bathrooms = DB.Column(DB.Integer, nullable=False)
    beds = DB.Column(DB.Integer, nullable=False)
    listing_url = DB.Column(DB.String(355), nullable=False)
    title = DB.Column(DB.String(255), nullable=False)
    picture_url = DB.Column(DB.String(355))
    city = DB.Column(DB.String(255), nullable=False)
    state = DB.Column(DB.String(2), nullable=False)
    zip = DB.Column(DB.SmallInteger, nullable=False)
    country = DB.Column(DB.String(255), nullable=False)
    latitude = DB.Column(DB.Float, nullable=False)
    longitude = DB.Column(DB.Float, nullable=False)

    property_type = DB.relationship('property_types', foreign_keys='listings.property_type_id')
    neighborhood = DB.relationship('neighborhoods', foreign_keys='listings.neighborhood_id')

    def __repr__(self):
        return '<listings {}>'.format(self.name)


class listing_amenities(DB.Model):
    id = DB.Column(DB.Integer,  primary_key=True)
    listing_id = DB.Column(DB.Integer, DB.ForeignKey("property_types.id"), nullable=False)
    amenities_id = DB.Column(DB.Integer, DB.ForeignKey("amenities.id"), nullable=False)

    def __repr__(self):
        return '<listing_amenities {}>'.format(self.name)


class amenities(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    amenity = DB.Column(DB.String(255), nullable=False)

    def __repr__(self):
        return '<amenities {}>'.format(self.name)


class neighborhoods(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    neighborhood = DB.Column(DB.String(255))

    def __repr__(self):
        return '<neighborhoods {}>'.format(self.name)


class property_types(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    property_type = DB.Column(DB.String(255))

    def __repr__(self):
        return '<property_types {}>'.format(self.name)
