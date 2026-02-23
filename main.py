import reasoning_engine
from reasoning import detect_intent
from reasoning_engine import generate_plan
while True:
    user_input = input("Enter command: ")

    intent = detect_intent(user_input)
    print("Detected Intent:", intent)

    plan = generate_plan(intent)
    print("Generated Plan:", plan)