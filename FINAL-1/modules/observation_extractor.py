def extract_observations(scene_data):
    observations = {
        "weapon_present": False,
        "possible_weapons": [],
        "signs_of_violence": [],
        "point_of_entry": None,
        "victim_found": False
    }
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied Pipe"],
    "signs_of_violence": ["Blood Pool", "Fingerprint Smears", "Shoe Prints"],
    "point_of_entry": "Open Door",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied Knife"],
    "signs_of_violence": ["Blood Trail", "Torn Wallet", "Broken Phone", "Shoe Print"],
    "point_of_entry": None,
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Pistol"],
    "signs_of_violence": ["Blood Splatter", "Bullet Casings", "Broken Lock"],
    "point_of_entry": "Broken Lock",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Pistol"],
    "signs_of_violence": ["Blood Splatter", "Bullet Casings", "Broken Lock"],
    "point_of_entry": "Broken Lock",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Crowbar"],
    "signs_of_violence": ["Blood Pool", "Drag Marks", "Broken Phone"],
    "point_of_entry": None,
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Crowbar"],
    "signs_of_violence": ["Blood Pool", "Drag Marks", "Broken Phone"],
    "point_of_entry": None,
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Crowbar"],
    "signs_of_violence": ["Blood Pool", "Drag Marks", "Broken Phone"],
    "point_of_entry": None,
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Crowbar"],
    "signs_of_violence": ["Blood Pool", "Drag Marks", "Broken Phone"],
    "point_of_entry": None,
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Crowbar"],
    "signs_of_violence": ["Blood Pool", "Drag Marks", "Broken Phone"],
    "point_of_entry": None,
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Axe", "Bullet Casing"],
    "signs_of_violence": ["Blood Spatter", "Mud Tracks", "Torn Shirt"],
    "point_of_entry": "Mud Tracks",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied Crowbar", "Bullet Casing"],
    "signs_of_violence": [
        "Blood Splatter",
        "Victim’s Body",
        "Shoe Print",
        "Broken Watch",
        "Torn Fabric",
        "Drag Marks"
    ],
    "point_of_entry": "Broken Window",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied Crowbar", "Bullet Casing"],
    "signs_of_violence": [
        "Blood Splatter",
        "Victim’s Body",
        "Shoe Print",
        "Broken Watch",
        "Torn Fabric",
        "Drag Marks"
    ],
    "point_of_entry": "Broken Window",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Blunt Weapon (Pipe)"],
    "signs_of_violence": [
        "Pool of Blood",
        "Shoe Marks",
        "Fingerprint Smears"
    ],
    "point_of_entry": "Open Door",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Pistol"],
    "signs_of_violence": [
        "Bullet Casings",
        "Blood Splatter",
        "Glove"
    ],
    "point_of_entry": "Broken Lock",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied Knife"],
    "signs_of_violence": [
        "Blood Trail",
        "Broken Phone",
        "Shoe Print",
        "Torn Wallet"
    ],
    "point_of_entry": None,
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Blunt Weapon (Pipe)"],
    "signs_of_violence": [
        "Pool of Blood",
        "Shoe Marks",
        "Fingerprint Smears"
    ],
    "point_of_entry": "Open Door",
    "victim_found": True
}

observations = {
    "weapon_present": True,
    "possible_weapons": ["Pistol"],
    "signs_of_violence": [
        "Bullet Casings",
        "Blood Splatter",
        "Glove"
    ],
    "point_of_entry": "Broken Lock",
    "victim_found": True
}




observations = {
    "weapon_present": True,
    "possible_weapons": ["Pistol"],
    "signs_of_violence": [
        "Bullet Casings",
        "Blood Splatter",
        "Glove"
    ],
    "point_of_entry": "Broken Lock",
    "victim_found": True
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
