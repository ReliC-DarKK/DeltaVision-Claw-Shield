def validate_plan(plan, user_input):

    if plan is None:
        return False, "Invalid intent"

    score = user_input.get("score")

    # Demo rule 1: Score must exist
    if score is None:
        return False, "Score missing"

    # Demo rule 2: Score must be integer
    if not isinstance(score, int):
        return False, "Score must be a number"

    # Demo rule 3: Score must be between 0 and 100
    if score < 0 or score > 100:
        return False, "Score must be between 0 and 100"

    return True, "Validation successful"