from reasoning_engine import generate_plan
from validation import validate_plan
from planner import execute_plan
from logger import log_event


def main():
    user_input = input("Enter command: ")

    # Generate plan
    plan = generate_plan(user_input)

    # Ask for score (for validation demo)
    score_input = input("Enter score (0-100): ")

    try:
        score_input = int(score_input)
    except ValueError:
        pass

    user_data = {
        "score": score_input
    }

    # Validate
    is_valid, message = validate_plan(plan, user_data)

    if is_valid:
      result = execute_plan(plan)
      print("✅ Action Executed")
      print(result)

    # ✅ ADD LOGGER HERE (Success Case)
      log_event(user_input, plan["action"], "Success")

    else:
       print("⛔ Action Blocked")
       print(message)

    # ✅ ADD LOGGER HERE (Failure Case)
       log_event(user_input, plan["action"], message)


if __name__ == "__main__":
     main()