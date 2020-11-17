from db import db


class PermissionHandlerModel(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    advertisement_id = db.Column(
        db.Integer, db.ForeignKey("advertisements.id"), nullable=False
    )
    permission_status = db.Column(db.Boolean, nullable=False)

    def __init__(self, user_id, advertisement_id, permission_status):
        self.user_id = user_id
        self.advertisement_id = advertisement_id
        self.permission_status = permission_status

    @classmethod
    def find_by_id(cls, permission_id: int) -> "PermissionHandlerModel":
        return cls.query.filter_by(id=permission_id).first()

    @classmethod
    def find_by_user_id(cls, user_id: int) -> list:
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def find_by_advertisement_id(cls, advertisement_id: int) -> list:
        return cls.query.filter_by(advertisement_id=advertisement_id).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
