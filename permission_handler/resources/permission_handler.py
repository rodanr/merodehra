from flask_restful import Resource
from flask import request
from permission_handler.models.permission_handler import PermissionHandlerModel
from permission_handler.schemas.permission_handler import (
    PermissionRequestSchema,
    PermissionGrantSchema,
)

# Instance of schema
permission_request_schema = PermissionRequestSchema()
permission_grant_schema = PermissionGrantSchema()


class RequestPermission(Resource):
    @classmethod
    def post(cls):
        permission_request_json = request.get_json()
        permission_request_data = permission_request_schema.load(
            permission_request_json
        )
        permission_request = PermissionHandlerModel(
            permission_request_data["user_id"],
            permission_request_data["advertisement_id"],
            permission_request_data["permission_status"],
        )
        permission_request.save_to_db()
        return {"message": "Your request added successfully"}, 200


class GrantPermission(Resource):
    @classmethod
    def post(cls):
        permission_grant_json = request.get_json()
        permission_grant_data = permission_grant_schema.load(permission_grant_json)
        permission = PermissionHandlerModel.find_by_id(
            permission_grant_data["permission_id"]
        )
        permission.permission_status = permission_grant_data["permission_status"]
        permission.save_to_db()
        if not permission_grant_data["permission_status"]:
            return {
                "message": "You denied permission but if you change your mind, you can come again and grant permission"
            }
        return {"message": "You have successfully granted the permission"}
