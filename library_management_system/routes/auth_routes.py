from flask import Blueprint, request, jsonify

from services.auth_service import (
    register_user,
    login_user
)

from flask_jwt_extended import (
    create_access_token
)

auth_bp = Blueprint(
    "auth",
    __name__
)


# REGISTER
@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    data = request.json

    success = register_user(
        data["username"],
        data["password"],
        data["role"]
    )

    if success:

        return jsonify({
            "message": "User registered"
        }), 201

    return jsonify({
        "error": "Username already exists"
    }), 400


# LOGIN
@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.json

    user = login_user(
        data["username"],
        data["password"]
    )

    if not user:

        return jsonify({
            "error": "Invalid credentials"
        }), 401

    # IMPORTANT FIX
    token = create_access_token(
        identity=str(user["id"]),
        additional_claims={
            "role": user["role"]
        }
    )

    return jsonify({
        "token": token,
        "role": user["role"]
    })