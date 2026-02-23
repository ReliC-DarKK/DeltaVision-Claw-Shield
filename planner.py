INTENT_MAP = {
    "view_stats": {
        "action": "fetch_stats",
        "requires_auth": True,
        "requires_db": True
    },
    "submit_score": {
        "action": "save_score",
        "requires_auth": True,
        "requires_db": True
    }
}

def generate_plan(intent):
    return INTENT_MAP.get(intent)
