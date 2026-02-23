from datetime import datetime

def log_event(user_input, intent, validation):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = (
        f"[{timestamp}] | "
        f"Input: {user_input} | "
        f"Intent: {intent} | "
        f"Validation: {validation}\n"
    )

    # Write to log file
    with open("system.log", "a") as file:
        file.write(log_message)

    print("📝 Event Logged")