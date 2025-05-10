def extract_observations(scene_data):
    observations = {
        "weapon_present": False,
        "possible_weapons": [],
        "signs_of_violence": [],
        "point_of_entry": None,
        "victim_found": False
    }

    for obj in scene_data["objects"]:
        label = obj["label"]

        if label in ["knife", "gun", "bat", "bloodied_knife"]:
            observations["weapon_present"] = True
            observations["possible_weapons"].append(label)

        if label in ["blood", "bruises", "body", "blood_on_bed"]:
            observations["signs_of_violence"].append(label)

        if label in ["broken_window", "open_door"]:
            observations["point_of_entry"] = label

        if label == "body":
            observations["victim_found"] = True

    return observations
