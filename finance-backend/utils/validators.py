def validate_record(data):
    required_fields = ["amount", "type", "category", "date"]

    for field in required_fields:
        if field not in data:
            return False, f"{field} is required"

    if data["type"] not in ["income", "expense"]:
        return False, "Invalid type"

    return True, None
def safe_execute(func):
    try:
        return func()
    except Exception as e:
        return {"error": str(e)}, 500