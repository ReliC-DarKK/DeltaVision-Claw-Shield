from planner import generate_plan
from validation import validate_plan

intent = "submit_score"
plan = generate_plan(intent)

# Take user input
score_input = input("Enter score (0-100): ")

try:
    score_input = int(score_input)
except ValueError:
    score_input = score_input  # keep it as string to fail validation

user_data = {
    "score": score_input
}

is_valid, message = validate_plan(plan, user_data)

if is_valid:
    print("✅ Accepted:", message)
else:
    print("❌ Rejected:", message)