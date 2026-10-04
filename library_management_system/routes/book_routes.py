from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt
)

from services.book_service import (
    add_book,
    get_books,
    update_book,
    delete_book
)

book_bp = Blueprint(
    "books",
    __name__
)


# GET BOOKS
@book_bp.route(
    "/",
    methods=["GET"]
)
@jwt_required()
def get_all_books():

    books = get_books()

    return jsonify([
        dict(book)
        for book in books
    ])


# ADD BOOK
@book_bp.route(
    "/",
    methods=["POST"]
)
@jwt_required()
def create_book():

    claims = get_jwt()

    if claims["role"] != "admin":

        return jsonify({
            "error": "Admin only"
        }), 403

    data = request.json

    add_book(
        data["title"],
        data["author"],
        data["description"]
    )

    return jsonify({
        "message": "Book added"
    })


# UPDATE BOOK
@book_bp.route(
    "/<int:id>",
    methods=["PUT"]
)
@jwt_required()
def edit_book(id):

    claims = get_jwt()

    if claims["role"] != "admin":

        return jsonify({
            "error": "Admin only"
        }), 403

    data = request.json

    update_book(
        id,
        data["title"],
        data["author"],
        data["description"]
    )

    return jsonify({
        "message": "Book updated"
    })


# DELETE BOOK
@book_bp.route(
    "/delete-by-name/<string:title>",
    methods=["DELETE"]
)
@jwt_required()
def remove_book(title):

    claims = get_jwt()

    if claims["role"] != "admin":

        return jsonify({
            "error": "Admin only"
        }), 403

    delete_book(title)

    return jsonify({
        "message": "Book deleted"
    })