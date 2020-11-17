from ma import ma
from permission_handler.models.permission_handler import PermissionHandlerModel


class PermissionRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PermissionHandlerModel
        dump_only = ("id",)
        # enables to load foreign key value
        include_fk = True


class PermissionGrantSchema(ma.Schema):
    class Meta:
        fields = ("permission_id", "permission_status")
