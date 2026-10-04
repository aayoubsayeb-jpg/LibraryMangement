from flask import Blueprint, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from services.borrow_service import (
    borrow_book,
    buy_book
)

borrow_bp = Blueprint(
    "borrow",
    __name__
)


# BORROW
@borrow_bp.route(
    "/borrow/<int:book_id>",
    methods=["POST"]
)
@jwt_required()
def borrow(book_id):

    user_id = get_jwt_identity()

    success = borrow_book(
        int(user_id),
        book_id
    )

    if success:

        return jsonify({
            "message": "Book borrowed"
        })

    return jsonify({
        "error": "Book unavailable"
    }), 400


# BUY
@borrow_bp.route(
    "/buy/<int:book_id>",
    methods=["POST"]
)
@jwt_required()
def buy(book_id):

    user_id = get_jwt_identity()

    buy_book(
        int(user_id),
        book_id
    )

    return jsonify({
        "message": "Book purchased"
    })