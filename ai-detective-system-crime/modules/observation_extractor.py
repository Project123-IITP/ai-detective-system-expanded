def extract_observations(scene_data):
    observations = {
        "weapon_present": False,
        "possible_weapons": [],
        "signs_of_violence": [],
        "point_of_entry": None,
        "victim_found": False
    }
    
    observations = {
        "weapon_present": False,
        "possible_weapons": [],
        "signs_of_violence": [],
        "point_of_entry": None,
        "victim_found": False
    }
    
    observations = {
    "weapon_present": True,
    "possible_weapons": [],
    "signs_of_violence": [],
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
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to back door",
        "gasoline residue detected near body"
    ],
    "point_of_entry": "blood trail leading to back door",
    "victim_found": True
}

# Case 2
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": ["bloodied crowbar near the victim’s head"],
    "point_of_entry": None,
    "victim_found": True
}

# Case 3
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": [
        "blood trail leading to rooftop exit",
        "bloodied crowbar near the victim’s head",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": "blood trail leading to rooftop exit",
    "victim_found": True
}

# Case 4
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "note with smeared ink beside victim",
        "bleach residue detected near body"
    ],
    "point_of_entry": "partial work shoe print on ledge",
    "victim_found": True
}

# Case 5
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to back door",
        "bleach residue detected near body"
    ],
    "point_of_entry": "blood trail leading to back door",
    "victim_found": True
}

# Case 6
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [],
    "point_of_entry": "partial work shoe print on ledge",
    "victim_found": True
}

# Case 7
    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": [
        "blood trail leading to rooftop exit",
        "bloodied knife near the victim’s head"
    ],
    "point_of_entry": "blood trail leading to rooftop exit",
    "victim_found": True
}

# Case 8
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [],
    "point_of_entry": "partial high-heel print on window sill",
    "victim_found": True
}

# Case 9
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "bleach residue detected near body",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": "partial work shoe print on floor",
    "victim_found": True
}

# Case 10
    observations = {
    "weapon_present": True,
    "possible_weapons": ["hammer"],
    "signs_of_violence": [
        "bloodied hammer near the victim’s head",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": None,
    "victim_found": True
}
    # Case 11
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to rooftop exit",
        "chloroform residue detected near body",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": "partial sneaker print on window sill",
    "victim_found": True
}

# Case 12
    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": [
        "bloodied knife near the victim’s head"
    ],
    "point_of_entry": None,
    "victim_found": True
}

# Case 13
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "chloroform residue detected near body",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": "partial work shoe print on floor",
    "victim_found": True
}

# Case 14
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": [
        "bloodied crowbar near the victim’s head",
        "blood trail leading to rooftop exit"
    ],
    "point_of_entry": "blood trail leading to rooftop exit",
    "victim_found": True
}

# Case 15
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": [
        "bloodied crowbar near the victim’s head",
        "gasoline residue detected near body"
    ],
    "point_of_entry": "partial boot print on doorframe",
    "victim_found": True
}

# Case 16
    observations = {
    "weapon_present": True,
    "possible_weapons": ["bat"],
    "signs_of_violence": [
        "bloodied bat near the victim’s head",
        "gasoline residue detected near body"
    ],
    "point_of_entry": "blood trail leading to fire escape",
    "victim_found": True
}

# Case 17
    observations = {
    "weapon_present": True,
    "possible_weapons": ["hammer"],
    "signs_of_violence": [
        "alcohol residue detected near body",
        "bloodied hammer near the victim’s head",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": None,
    "victim_found": True
}

# Case 18
    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": [
        "bloodied knife near the victim’s head",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": None,
    "victim_found": True
}

# Case 19
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to back door",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": "blood trail leading to back door",
    "victim_found": True
}

# Case 20
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": [
        "bloodied crowbar near the victim’s head",
        "blood trail leading to rooftop exit"
    ],
    "point_of_entry": "partial work shoe print on doorframe",
    "victim_found": True
}
    
    # Case 21
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": [
        "blood trail leading to rooftop exit",
        "bleach residue detected near body",
        "note with smeared ink beside victim"
    ],
    "point_of_entry": "wallet with fingerprints found",
    "victim_found": True
}

# Case 22
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "alcohol residue detected near body"
    ],
    "point_of_entry": None,
    "victim_found": True
}

# Case 23
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "bleach residue detected near body"
    ],
    "point_of_entry": "partial work shoe print on floor",
    "victim_found": True
}

# Case 24
    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": [
        "bloodied knife near the victim’s head",
        "gasoline residue detected near body"
    ],
    "point_of_entry": None,
    "victim_found": True
}

# Case 25
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to service hatch"
    ],
    "point_of_entry": "watch with fingerprints found",
    "victim_found": True
}

# Case 26
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "alcohol residue detected near body",
        "security camera lens smashed"
    ],
    "point_of_entry": "cracked phone screen 5 feet away",
    "victim_found": True
}

# Case 27
    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": [
        "bloodied knife near the victim’s head",
        "bleach residue detected near body"
    ],
    "point_of_entry": "glove with fingerprints found",
    "victim_found": True
}

# Case 28
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to back door"
    ],
    "point_of_entry": "wallet with fingerprints found",
    "victim_found": True
}

# Case 29
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "alcohol residue detected near body"
    ],
    "point_of_entry": "strands of hair on the ground",
    "victim_found": True
}

# Case 30
    observations = {
    "weapon_present": True,
    "possible_weapons": ["bat"],
    "signs_of_violence": [
        "bloodied bat near the victim’s head",
        "bleach residue detected near body"
    ],
    "point_of_entry": "blood trail leading to service hatch",
    "victim_found": True
}

# Case 31
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to rooftop exit",
        "watch with fingerprints found"
    ],
    "point_of_entry": "keys missing from the victim’s pocket",
    "victim_found": True
}

# Case 32
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to rooftop exit",
        "bleach residue detected near body"
    ],
    "point_of_entry": "cracked phone screen 10 feet away",
    "victim_found": True
}

# Case 33
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "blood trail leading to service hatch"
    ],
    "point_of_entry": "partial work shoe print on doorframe",
    "victim_found": True
}

# Case 34
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [
        "blood trail leading to back door"
    ],
    "point_of_entry": "watch with fingerprints found",
    "victim_found": True
}

# Case 35
    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": [
        "bloodied knife near the victim’s head",
        "chloroform residue detected near body"
    ],
    "point_of_entry": "keys missing from the victim’s pocket",
    "victim_found": True
}

# Case 36
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "chloroform residue detected near body"
    ],
    "point_of_entry": "phone missing from the victim’s pocket",
    "victim_found": True
}

# Case 37
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": [
        "bloodied crowbar near the victim’s head",
        "alcohol residue detected near body"
    ],
    "point_of_entry": "partial sneaker print on floor",
    "victim_found": True
}

# Case 38
    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": [
        "bloodied crowbar near the victim’s head",
        "blood trail leading to back door"
    ],
    "point_of_entry": "security camera lens smashed",
    "victim_found": True
}

# Case 39
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "blood trail leading to rooftop exit"
    ],
    "point_of_entry": "strands of thread on the ground",
    "victim_found": True
}

# Case 40
    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": [
        "bloodied pipe near the victim’s head",
        "chloroform residue detected near body"
    ],
    "point_of_entry": "wallet with fingerprints found",
    "victim_found": True
}
    
    
   
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Blood trail", "Cracked phone screen"],
    "point_of_entry": "rooftop exit",
    "victim_found": True
    },
     
     
     
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Blood trail"],
    "point_of_entry": "rooftop exit",
    "victim_found": True
    },
    
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied knife"],
    "signs_of_violence": ["Bloodied knife", "Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Blood trail", "gasoline residue", "Cracked phone screen"],
    "point_of_entry": "fire escape",
    "victim_found": True
    },
    
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied hammer"],
    "signs_of_violence": ["Bloodied hammer", "alcohol residue"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Blood trail", "Cracked phone screen"],
    "point_of_entry": "back door",
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied hammer"],
    "signs_of_violence": ["Bloodied hammer", "alcohol residue"],
    "point_of_entry": "service hatch",
    "victim_found": True
    },
    
    
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied crowbar"],
    "signs_of_violence": ["Bloodied crowbar", "Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["bleach residue"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied bat"],
    "signs_of_violence": ["Bloodied bat", "alcohol residue", "Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied bat"],
    "signs_of_violence": ["Bloodied bat", "Blood trail", "Cracked phone screen"],
    "point_of_entry": "back door",
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied crowbar"],
    "signs_of_violence": ["Bloodied crowbar", "Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied knife"],
    "signs_of_violence": ["Bloodied knife", "Blood trail"],
    "point_of_entry": "rooftop exit",
    "victim_found": True
    },
    
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Blood trail", "Cracked phone screen"],
    "point_of_entry": "back door",
    "victim_found": True
    },
    
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["gasoline residue", "Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied crowbar"],
    "signs_of_violence": ["Bloodied crowbar", "Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied pipe"],
    "signs_of_violence": ["Bloodied pipe", "Blood trail", "alcohol residue", "Cracked phone screen"],
    "point_of_entry": "service hatch",
    "victim_found": True
    },
    
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied hammer"],
    "signs_of_violence": ["Bloodied hammer", "alcohol residue", "Blood trail", "Cracked phone screen"],
    "point_of_entry": "service hatch",
    "victim_found": True
    
    },
    observations = {
    "weapon_present": True,
    "possible_weapons": ["Bloodied bat"],
    "signs_of_violence": ["Bloodied bat", "gasoline residue", "Cracked phone screen"],
    "point_of_entry": None,
    "victim_found": True
    }








    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": [],
    "point_of_entry": None,
    "victim_found": False
}
    
    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Blood trail", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["Blood trail", "chloroform residue", "smashed security camera"],
    "point_of_entry": "fire escape",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": ["Blood trail", "bloodied crowbar", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "bleach residue"],
    "point_of_entry": "roof access",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": ["bloodied crowbar", "chloroform residue", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": ["bloodied pipe", "smashed security camera"],
    "point_of_entry": "restroom window",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["bat"],
    "signs_of_violence": ["bloodied bat", "chloroform residue"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "bleach residue"],
    "point_of_entry": "roof access",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": ["bloodied pipe", "chloroform residue", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["gasoline residue", "blood trail"],
    "point_of_entry": "rooftop exit",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "bleach residue"],
    "point_of_entry": "doorframe",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "note with smeared ink"],
    "point_of_entry": "loading dock",
    "victim_found": True
}
    obsrevations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": ["bloodied pipe", "chloroform residue", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["chloroform residue", "strands of thread"],
    "point_of_entry": "fire escape",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["bat"],
    "signs_of_violence": ["bloodied bat", "gasoline residue"],
    "point_of_entry": "back alley",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "bleach residue"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["bat"],
    "signs_of_violence": ["bloodied bat", "gasoline residue"],
    "point_of_entry": "roof access",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": ["bloodied crowbar", "blood trail"],
    "point_of_entry": "fire escape",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["blood trail", "smashed security camera"],
    "point_of_entry": "rooftop exit",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["gasoline residue", "smashed security camera"],
    "point_of_entry": "service hatch",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": ["bloodied knife", "gasoline residue"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "blood trail"],
    "point_of_entry": "fire escape",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": ["bloodied knife", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": ["bloodied crowbar", "smashed security camera"],
    "point_of_entry": "basement window",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["hammer"],
    "signs_of_violence": ["bloodied hammer", "alcohol residue"],
    "point_of_entry": "basement door",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": ["bloodied pipe", "smashed security camera"],
    "point_of_entry": "restroom window",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["chloroform residue", "blood trail"],
    "point_of_entry": "rooftop exit",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "bleach residue"],
    "point_of_entry": "forest clearing",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "strands of fur"],
    "point_of_entry": "train station window",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": ["bloodied crowbar", "strands of hair"],
    "point_of_entry": "roof access",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "gasoline residue"],
    "point_of_entry": "back door",
    "victim_found": True
}








    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "strands of hair"],
    "point_of_entry": "basement window",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["bat"],
    "signs_of_violence": ["bloodied bat", "gasoline residue", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["chloroform residue", "broken glass"],
    "point_of_entry": "broken window",
    "victim_found": True
}


    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "traces of blood"],
    "point_of_entry": "rear gate",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["knife"],
    "signs_of_violence": ["bloodied knife", "gasoline residue", "smashed security camera"],
    "point_of_entry": "fire escape",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["crowbar"],
    "signs_of_violence": ["bloodied crowbar", "traces of gasoline"],
    "point_of_entry": "roof access",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "gasoline residue", "blood trail"],
    "point_of_entry": "service hatch",
    "victim_found": True
}

    observations = {
    "weapon_present": True,
    "possible_weapons": ["pipe"],
    "signs_of_violence": ["bloodied pipe", "smashed security camera"],
    "point_of_entry": "back door",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["strands of hair", "blood trail", "smashed security camera"],
    "point_of_entry": "side window",
    "victim_found": True
}

    observations = {
    "weapon_present": False,
    "possible_weapons": [],
    "signs_of_violence": ["smashed security camera", "traces of blood"],
    "point_of_entry": "front door",
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

print("No  errors detected.")
