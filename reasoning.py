# Dictionary mapping intent names to keywords
INTENT_KEYWORDS = {
    "start_system": ["start", "begin", "launch"],
    "stop_system": ["stop", "shutdown", "end"],
    "move_forward": ["forward", "ahead"],
    "move_backward": ["back", "backward"],
    "turn_left": ["left"],
    "turn_right": ["right"],
    "pick_object": ["pick", "grab"],
    "drop_object": ["drop", "release"],
    "show_status": ["status", "state"],
    "view_stats": ["view stats", "show stats", "my stats"],
    "submit_score": ["submit score", "add score", "save score"]
}


def detect_intent(user_input):
    user_input = user_input.lower()

    for intent, keywords in INTENT_KEYWORDS.items():
        for word in keywords:
            if word in user_input:
                return intent

    return "unknown_intent"
def detect_intent(user_input):
    if not user_input:
        return "unknown_intent"

    user_input = user_input.lower()

    for intent, keywords in INTENT_KEYWORDS.items():
        for word in keywords:
            if word in user_input:
                return intent

    return "unknown_intent"