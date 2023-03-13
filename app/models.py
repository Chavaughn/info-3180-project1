from . import db
from werkzeug.security import generate_password_hash

class PropertyType(db.Model):
    __tablename__ = 'property_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    def __repr__(self):
        return self.name

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    property_type_id = db.Column(db.Integer, db.ForeignKey('property_type.id'))
    photo_album_id = db.Column(db.Integer, db.ForeignKey('photo_album.id'))

class PhotoAlbum(db.Model):
    __tablename__ = 'photo_album'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    main_photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'))

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(10203213))
    rooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Numeric(2, 1))
    price = db.Column(db.Numeric(20, 2))
    property_type_id = db.Column(db.Integer, db.ForeignKey('property_type.id'))
    location = db.Column(db.String(255))
    photo_album_id = db.Column(db.Integer, db.ForeignKey('photo_album.id'))
    main_photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'))

    # Define a relationship to the PropertyType model
    property_type = db.relationship('PropertyType', backref='properties')

    # Define a relationship to the PhotoAlbum model
    photo_album = db.relationship('PhotoAlbum', backref='property')

    # Define a relationship to the Photo model for the main photo
    main_photo_rel = db.relationship('Photo', foreign_keys=[main_photo_id])

    @property
    def main_photo_name(self):
        return self.main_photo_rel.name