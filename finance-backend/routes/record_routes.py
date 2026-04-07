from flask import Blueprint, request, jsonify
from config import get_db_connection
from utils.decorators import role_required
from utils.validators import validate_record

record_bp = Blueprint("record_bp", __name__)

# 🔹 CREATE RECORD
@record_bp.route("/", methods=["POST"])
@role_required(["admin"])
def create_record():
    data = request.json

    valid, error = validate_record(data)
    if not valid:
        return jsonify({"error": error}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO records (amount, type, category, date, notes, user_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(query, (
        data["amount"],
        data["type"],
        data["category"],
        data["date"],
        data.get("notes"),
        data["user_id"]
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Record created"}), 201


# 🔹 GET RECORDS (FIXED FULLY)
@record_bp.route("/", methods=["GET"])
@role_required(["admin", "analyst", "viewer"])
def get_records():
    conn = get_db_connection()
    cursor = conn.cursor()

    type_filter = request.args.get("type")
    category = request.args.get("category")

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 5))
    offset = (page - 1) * limit

    query = "SELECT * FROM records WHERE 1=1"
    params = []

    if type_filter:
        query += " AND type=?"
        params.append(type_filter)

    if category:
        query += " AND category=?"
        params.append(category)

    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cursor.execute(query, tuple(params))
    records = cursor.fetchall()

    # 🔥 convert to dictionary (IMPORTANT)
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in records]

    cursor.close()
    conn.close()

    return jsonify({
        "page": page,
        "limit": limit,
        "data": data
    })