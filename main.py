from reasoning_engine import generate_plan
from validation import validate_plan
from planner import execute_plan
from logger import log_event

def main():
    user_input = input("Enter command: ")

    plan = generate_plan(user_input)

    is_valid, message = validate_plan(plan, {"score": 10})

    if is_valid:
        result = execute_plan(plan)
        print("✅ Action Executed")
        print(result)
    else:
        print("⛔ Action Blocked")
        print(message)

if __name__ == "__main__":
    main()