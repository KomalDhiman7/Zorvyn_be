from flask import Blueprint, request, jsonify
from config import get_db_connection

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO users (name, email, password, role, is_active)
    VALUES (?, ?, ?, ?, ?)
    """

    cursor.execute(query, (
        data["name"],
        data["email"],
        data["password"],
        data["role"],
        True
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User created"}), 201