INTENT_MAP = {
    "submit_score": {
        "action": "save_score",
        "requires_auth": False,
        "requires_db": False
    }
}

def generate_plan(intent):
    return INTENT_MAP.get(intent)