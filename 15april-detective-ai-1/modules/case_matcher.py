def match_previous_cases(observations):
    previous_cases = [
        {
            "case_id": "C123",
            "summary": "Victim found with stab wounds near broken window.",
            "elements": ["bloodied_knife", "blood_on_bed", "broken_window"]
        },
        {
            "case_id": "C456",
            "summary": "Overturned furniture and broken window suggest forced entry.",
            "elements": ["overturned_chair", "broken_window"]
        }
    ]

    matched = []
    obs_elements = observations["possible_weapons"] + observations["signs_of_violence"]
    if observations["point_of_entry"]:
        obs_elements.append(observations["point_of_entry"])

    for case in previous_cases:
        match_score = len(set(case["elements"]) & set(obs_elements))
        if match_score >= 2:
            matched.append(case)

    return matched
