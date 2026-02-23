from planner import generate_plan
from validation import validate_plan

# Example user request
intent = "view_stats"

# Generate plan
plan = generate_plan(intent)

# Simulated user state
user_data = {
    "is_authenticated": True,
    "db_connected": True
}

# Validate
is_valid, message = validate_plan(plan, user_data)

if is_valid:
    print("Executing:", plan["action"])
else:
    print("Blocked:", message)
