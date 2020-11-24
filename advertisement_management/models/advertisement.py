from db import db
from permission_handler.models.permission_handler import PermissionHandlerModel


class AdvertisementModel(db.Model):
    __tablename__ = "advertisements"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False
    )  # user_id who created this advertisement
    property_type = db.Column(db.String(10), nullable=False)  # Either its flat or room
    property_address = db.Column(
        db.String(100), nullable=False
    )  # Property's general address
    geo_location = db.Column(
        db.String(100), nullable=False
    )  # Geographical location of property i.e lat & long
    room_count = db.Column(db.Integer, nullable=False)  # Number of rooms
    price = db.Column(db.Float, nullable=False)  # Price of the property
    description = db.Column(
        db.String, nullable=False
    )  # Description about the property owner wants to tell
    photo = db.Column(
        db.String, nullable=False
    )  # Store the address of image for the advertisement uploaded in firebase storage
    water_source = db.Column(db.String(80), nullable=False)  # Like Well, boring or tap
    bathroom = db.Column(db.String(80), nullable=False)  # Shared or Private
    terrace_access = db.Column(db.Boolean, nullable=False)
    sold_status = db.Column(db.Boolean, nullable=False)
    permissions = db.relationship(
        "PermissionHandlerModel", backref="advertisement", lazy=True
    )

    def __init__(
        self,
        user_id,
        property_type,
        property_address,
        geo_location,
        room_count,
        price,
        description,
        photo,
        water_source,
        bathroom,
        terrace_access,
        sold_status,
    ):
        self.user_id = user_id
        self.property_type = property_type
        self.property_address = property_address
        self.geo_location = geo_location
        self.room_count = room_count
        self.price = price
        self.description = description
        self.photo = photo
        self.water_source = water_source
        self.bathroom = bathroom
        self.terrace_access = terrace_access
        self.sold_status = sold_status

    @classmethod
    def find_by_id(cls, advertisement_id: int) -> "AdvertisementModel":
        return cls.query.filter_by(id=advertisement_id).first()

    @classmethod
    def find_by_user_id(
        cls, user_id: int
    ) -> list:  # List of AdvertisementModel objects
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_advertisement_lists_by_location(cls, location_to_search: str) -> list:
        location_to_search_string = "%{}%".format(location_to_search)
        return cls.query.filter(
            AdvertisementModel.property_address.ilike(location_to_search_string)
        ).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
