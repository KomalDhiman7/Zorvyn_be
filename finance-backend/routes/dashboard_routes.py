from flask import Blueprint, jsonify
from config import get_db_connection
from utils.decorators import role_required

dashboard_bp = Blueprint("dashboard_bp", __name__)

# 🔹 MAIN DASHBOARD
@dashboard_bp.route("/")
@role_required(["admin", "analyst"])
def get_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM records WHERE type='income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM records WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0

    balance = income - expense

    cursor.close()
    conn.close()

    return jsonify({
        "total_income": income,
        "total_expense": expense,
        "net_balance": balance
    })


# 🔹 CATEGORY SUMMARY (FIXED)
@dashboard_bp.route("/categories")
@role_required(["admin", "analyst"])
def category_summary():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT category, SUM(amount) as total
    FROM records
    GROUP BY category
    """

    cursor.execute(query)
    results = cursor.fetchall()

    # 🔥 convert to dict
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in results]

    cursor.close()
    conn.close()

    return jsonify(data)