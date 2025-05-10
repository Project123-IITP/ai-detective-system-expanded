def generate_and_evaluate_theories(observations, matched_cases):
    theories = []

    if observations["victim_found"] or observations["weapon_present"]:
        for weapon in observations["possible_weapons"]:
            theory = {
                "hypothesis": f"Victim attacked using a {weapon} after intruder entered through {observations['point_of_entry']}.",
                "supporting_evidence": observations["signs_of_violence"] + [weapon, observations["point_of_entry"]],
                "score": 0
            }
            theories.append(theory)

    for theory in theories:
        for case in matched_cases:
            overlap = len(set(case["elements"]) & set(theory["supporting_evidence"]))
            theory["score"] += overlap

    if not theories:
        return {"hypothesis": "No strong theory could be formed.", "score": 0}

    return sorted(theories, key=lambda x: x["score"], reverse=True)[0]