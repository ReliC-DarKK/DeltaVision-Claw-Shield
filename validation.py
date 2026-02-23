def validate_plan(plan, user_data):

    # 1. Check if intent exists
    if plan is None:
        return False, "Intent not recognized"

    # 2. Check authentication
    if plan["requires_auth"] and not user_data.get("is_authenticated"):
        return False, "User not authenticated"

    # 3. Check database connection
    if plan["requires_db"] and not user_data.get("db_connected"):
        return False, "Database not connected"

    return True, "Validation successful"
