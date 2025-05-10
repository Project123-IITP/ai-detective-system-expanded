def generate_and_evaluate_theories(observations, matched_cases):
    theories = []

    if observations["victim_found"] or observations["weapon_present"]:
        for weapon in observations["possible_weapons"]:
            theory = {
                "hypothesis": f"Victim attacked using a {weapon} after intruder entered through {observations['point_of_entry']}.",
                "supporting_evidence": observations["signs_of_violence"] + [weapon, observations["point_of_entry"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Burglary occurred through forced entry at {observations['point_of_entry']} using {tool_used}.",
                "supporting_evidence": observations["broken_locks"] + [tool_used, observations["point_of_entry"]],
                "score": 0
            }
            theory = {   
                "hypothesis": f"Fire was deliberately started using {flammable_material} in the {observations['location_of_fire']}.",
                "supporting_evidence": observations["burn_patterns"] + [flammable_material, observations["location_of_fire"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was poisoned using {toxin} likely mixed in {observations['last_meal']}.",
                "supporting_evidence": observations["toxicology_reports"] + [toxin, observations["last_meal"]],
                "score": 0
            }

            theory = {
                "hypothesis": f"Victim was shot with a {weapon} from a distance near {observations['crime_scene_location']}.",
                "supporting_evidence": observations["ballistics_report"] + [weapon, observations["crime_scene_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Intruder entered through {observations['point_of_entry']} and attacked with {weapon}.",
                "supporting_evidence": observations["forced_entry_signs"] + [weapon, observations["point_of_entry"]],
                "score": 0
            }   
            theory = {
                "hypothesis": f"Victim was poisoned with {substance} mixed in {observations['consumed_item']}.",
                "supporting_evidence": observations["lab_results"] + [substance, observations["consumed_item"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect fled the scene via {observations['exit_point']} using {vehicle_type}.",
                "supporting_evidence": observations["footprints"] + [vehicle_type, observations["exit_point"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Crime was planned in advance based on communication through {observations['digital_device']}.",
                "supporting_evidence": observations["message_logs"] + [observations["digital_device"]],
                "score": 0
            }
            theory = {
                 "hypothesis": f"Victim was stabbed multiple times with {weapon} in the {observations['room']}.",
                 "supporting_evidence": observations["blood_splatter"] + [weapon, observations["room"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Theft occurred after suspect disabled security at {observations['location']}.",
                "supporting_evidence": observations["tampered_devices"] + [observations["location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect impersonated {observations['victim_relation']} to gain access to the property.",
                "supporting_evidence": observations["neighbor_testimonies"] + [observations["victim_relation"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was pushed from height at {observations['fall_location']}.",
                "supporting_evidence": observations["injury_analysis"] + [observations["fall_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Crime occurred during robbery attempt involving {weapon} at {observations['store_location']}.",
                "supporting_evidence": observations["missing_items"] + [weapon, observations["store_location"]],
                "score": 0
            }
            theory = {
                 "hypothesis": f"Victim was abducted from {observations['last_seen_location']} using {vehicle_type}.",
                 "supporting_evidence": observations["surveillance_footage"] + [vehicle_type, observations["last_seen_location"]],
                 "score": 0
                }
            theory = {
                "hypothesis": f"Suspect tampered with evidence at {observations['crime_scene_location']} using {tool_used}.",
                "supporting_evidence": observations["disturbed_items"] + [tool_used, observations["crime_scene_location"]],
                "score": 0
            }   
            theory = {
                "hypothesis": f"Arson was committed using {flammable_substance} found at {observations['origin_of_fire']}.",
                "supporting_evidence": observations["fire_investigation_report"] + [flammable_substance, observations["origin_of_fire"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was held captive at {observations['suspected_location']} for several days.",
                "supporting_evidence": observations["dna_traces"] + [observations["suspected_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Crime occurred after a struggle in {observations['room']} involving {weapon}.",
                "supporting_evidence": observations["displaced_objects"] + [weapon, observations["room"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect attempted to cover tracks using {method} at {observations['scene_area']}.",
                "supporting_evidence": observations["cleanup_traces"] + [method, observations["scene_area"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Murder was triggered by a financial dispute related to {observations['financial_asset']}.",
                "supporting_evidence": observations["bank_statements"] + [observations["financial_asset"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect used a fake ID registered under {observations['false_name']} to access the area.",
                "supporting_evidence": observations["id_records"] + [observations["false_name"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was lured to {observations['trap_location']} under false pretense of {reason}.",
                "supporting_evidence": observations["text_messages"] + [reason, observations["trap_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect escaped detection by altering appearance using {disguise_item}.",
                "supporting_evidence": observations["clothing_fibers"] + [disguise_item],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was targeted due to prior altercation with suspect at {observations['previous_incident_location']}.",
                "supporting_evidence": observations["police_reports"] + [observations["previous_incident_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect gained unauthorized entry using {tool_used} at {observations['entry_point']}.",
                "supporting_evidence": observations["tool_marks"] + [tool_used, observations["entry_point"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was followed from {observations['public_place']} before the attack.",
                "supporting_evidence": observations["cctv_tracking"] + [observations["public_place"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Theft was an inside job involving employee with access to {observations['restricted_area']}.",
                "supporting_evidence": observations["access_logs"] + [observations["restricted_area"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was attacked while asleep in {observations['room_name']}, using {weapon}.",
                "supporting_evidence": observations["bed_disturbance"] + [weapon, observations["room_name"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect attempted to mislead investigation by planting false evidence in {observations['secondary_location']}.",
                "supporting_evidence": observations["inconsistent_finds"] + [observations["secondary_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was coerced into silence about {observations['sensitive_topic']}, leading to confrontation.",
                "supporting_evidence": observations["threat_messages"] + [observations["sensitive_topic"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect attempted to destroy digital evidence using {method} on {observations['device']}.",
                "supporting_evidence": observations["damaged_hardware"] + [method, observations["device"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Homicide committed out of jealousy involving {observations['relationship_context']}.",
                "supporting_evidence": observations["messages"] + [observations["relationship_context"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect disguised voice while making threat calls using {device}.",
                "supporting_evidence": observations["call_records"] + [device],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was blackmailed through anonymous messages sent from {observations['device_used']}.",
                "supporting_evidence": observations["message_logs"] + [observations["device_used"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Crime was staged to look like an accident at {observations['scene_location']}.",
                "supporting_evidence": observations["inconsistent_injuries"] + [observations["scene_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect left the scene disguised as {observations['role_or_uniform']}.",
                "supporting_evidence": observations["uniform_fibers"] + [observations["role_or_uniform"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect used {observations['digital_method']} to gain access to victim’s accounts.",
                "supporting_evidence": observations["login_logs"] + [observations["digital_method"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was manipulated emotionally through {observations['communication_platform']} before the crime.",
                "supporting_evidence": observations["chat_history"] + [observations["communication_platform"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect set a trap using {trap_mechanism} near {observations['location']}.",
                "supporting_evidence": observations["injury_patterns"] + [trap_mechanism, observations["location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was isolated from others at {observations['location']} before being assaulted.",
                "supporting_evidence": observations["witness_testimonies"] + [observations["location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Crime was captured on a hidden device placed in {observations['concealment_spot']}.",
                "supporting_evidence": observations["device_footage"] + [observations["concealment_spot"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect altered timestamps of security footage using {software}.",
                "supporting_evidence": observations["metadata_analysis"] + [software],
                "score": 0
            }
            theory = {
                "hypothesis": f"Crime was committed during a power outage at {observations['location']}, possibly using {weapon}.",
                "supporting_evidence": observations["power_log_reports"] + [weapon, observations["location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was stalked over several days before being attacked at {observations['final_location']}.",
                "supporting_evidence": observations["gps_tracking"] + [observations["final_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect bribed a third party to execute the plan using funds traced from {observations['bank_account']}.",
                "supporting_evidence": observations["transaction_history"] + [observations["bank_account"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was suffocated using {object_used} in the {observations['room_name']}.",
                "supporting_evidence": observations["autopsy_report"] + [object_used, observations["room_name"]],
                "score": 0
            }   
            theory = {
                "hypothesis": f"Suspect used fake social media profile {observations['fake_name']} to lure the victim.",
                "supporting_evidence": observations["online_chats"] + [observations["fake_name"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect created a distraction using {method} to gain access to the restricted area.",
                "supporting_evidence": observations["security_logs"] + [method],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect wore gloves and left no fingerprints at {observations['crime_scene_location']}.",
                "supporting_evidence": observations["absence_of_fingerprints"] + [observations["crime_scene_location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Crime occurred due to rivalry related to {observations['common_interest']} at {observations['meeting_spot']}.",
                "supporting_evidence": observations["social_media_posts"] + [observations["common_interest"], observations["meeting_spot"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect used access credentials of {observations['employee_name']} to enter {observations['location']}.",
                "supporting_evidence": observations["keycard_logs"] + [observations["employee_name"], observations["location"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was drugged and taken unconscious to {observations['secondary_scene']}.",
                "supporting_evidence": observations["medical_report"] + [observations["secondary_scene"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspect attempted to frame another individual using their {observations['belonging']} at the scene.",
                "supporting_evidence": observations["planted_evidence"] + [observations["belonging"]],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was poisoned during a meal, possibly with {weapon}, administered by someone with access to the kitchen.",
                "supporting_evidence": observations["food_traces"] + [weapon, "kitchen access"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was ambushed while asleep, with {weapon} used in a surprise attack.",
                "supporting_evidence": observations["bed_disruption"] + [weapon, "absence of defensive wounds"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Assailant waited in hiding and attacked the victim in the hallway using {weapon}.",
                "supporting_evidence": observations["signs_of_struggle"] + [weapon, "hallway surveillance blackout"],
                "score": 0
            }
            theory = {
                "hypothesis": f"The crime was premeditated, and the {weapon} was planted in advance before the victim was lured to the scene.",
                "supporting_evidence": observations["lack_of_forced_entry"] + [weapon, "planned meeting messages"],
                "score": 0
            }
#here are several theories specifically based on outdoor crime scenes
#5. Alleyway Ambush:
            theory = {
                "hypothesis": f"Victim was ambushed with a {weapon} while walking through a dimly lit alley late at night.",
                "supporting_evidence": observations["blood_trail"] + [weapon, "lack_of_street_lighting"],
                "score": 0
            } 
#6. Forest Assault:
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} in the forest, possibly by someone familiar with the area.",
                "supporting_evidence": observations["broken_branches"] + [weapon, "footprints_leading_deeper_into_forest"],
                "score": 0
            } 
#7. Highway Incident:
            theory = {
                "hypothesis": f"Victim was forced off the road and assaulted with a {weapon} during a roadside confrontation.",
                "supporting_evidence": observations["tire_marks"] + [weapon, "car_door_damage"],
                "score": 0
            }
#8. Playground Confrontation:
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} near the park playground after a brief verbal altercation.",
                "supporting_evidence": observations["witness_testimony"] + [weapon, "discarded personal_items"],
                "score": 0
            }
#9. Crime Near Riverbank:
            theory = {
                "hypothesis": f"Victim was struck with a {weapon} and left unconscious near the riverbank.",
                "supporting_evidence": observations["muddy_clothing"] + [weapon, "drag_marks_toward_water"],
                "score": 0
            } 
#10. Public Protest Gone Violent:
            theory = {
                "hypothesis": f"Victim was injured with a {weapon} during a chaotic protest in the public square.",
                "supporting_evidence": observations["crowd_footage"] + [weapon, "confiscated_protest_signs"],
                "score": 0
            }
 #Here are outdoor crime scene theories that include long-range weapons, environmental hazards, and nighttime visibility issues, 
#11. Long-Range Weapon – Hilltop Sniper Attack:
            theory = {
                "hypothesis": f"Victim was shot with a {weapon} from an elevated position while walking on a trail below.",
                "supporting_evidence": observations["bullet_casing_on_hill"] + [weapon, "lack_of_close-range_evidence"],
                "score": 0
            }
#12. Environmental Hazard – Cliff Push:
            theory = {
                "hypothesis": f"Victim was pushed from a cliff edge after a struggle, possibly using a {weapon} to disorient them.",
                "supporting_evidence": observations["drag_marks_near_edge"] + [weapon, "missing_phone_found_on_clifftop"],
                "score": 0
            }
#13. Environmental Hazard – Drowning at Lake:
            theory = {
                "hypothesis": f"Victim was struck with a {weapon} and thrown into the lake, leading to accidental or intentional drowning.",
                "supporting_evidence": observations["waterlogged_clothes"] + [weapon, "bruises_indicating_blunt_force"],
                "score": 0
            }
            #14. Nighttime Visibility – Dark Pathway Assault:
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} on a poorly lit walking path, possibly followed for some time.",
                "supporting_evidence": observations["security_camera_blind_spot"] + [weapon, "victim's_torn_clothing"],
                "score": 0
            }
#15. Nighttime Visibility – Camping Area Attack:
            theory = {
                "hypothesis": f"Victim was assaulted with a {weapon} while camping in an isolated area, likely during the night while others were asleep.",
                "supporting_evidence": observations["disturbed_tent"] + [weapon, "missing_flashlight_found_far_away"],
                "score": 0
            }
#16. Long-Range + Night – Hunting Rifle Misuse:
            theory = {
                "hypothesis": f"Victim was mistakenly or intentionally shot with a {weapon} resembling a hunting rifle, possibly during illegal night hunting.",
                "supporting_evidence": observations["rifle_cartridge"] + [weapon, "thermal_scope_marks_on_tree"],
                "score": 0
            }
#17. Extreme Weather – Snowstorm Disappearance:
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} during a snowstorm, and evidence was concealed by the heavy snowfall.",
                "supporting_evidence": observations["partial_footprints"] + [weapon, "frozen_blood_spatter"],
                "score": 0
            }
 #18. Extreme Weather – Thunderstorm Ambush:
            theory = {
                "hypothesis": f"Victim was ambushed with a {weapon} while seeking shelter during a thunderstorm, which masked the assailant’s approach.",
                "supporting_evidence": observations["torn_raincoat"] + [weapon, "muddy_ground_with_slide_marks"],
                "score": 0
            }
#19. Wilderness Survival – Hiker Struggle:
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} during a hiking expedition, possibly by a companion or another stranded hiker.",
                "supporting_evidence": observations["shared_gear_with_blood"] + [weapon, "incomplete_sos_signal_near_scene"],
                "score": 0
            }
#20. Wilderness Survival – River Crossing Conflict:
            theory = {
                "hypothesis": f"Victim was struck with a {weapon} after a dispute during a dangerous river crossing.",
                "supporting_evidence": observations["camp_near_river"] + [weapon, "broken_bridge_plank"],
                "score": 0
            }
#21. Outdoor Event – Music Festival Incident:
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} during a chaotic moment at the music festival crowd surge.",
                "supporting_evidence": observations["lost_items_near_stage"] + [weapon, "eyewitness_social_media_posts"],
                "score": 0
            }
#22. Outdoor Event – Fairground Altercation:
            theory = {
                "hypothesis": f"Victim was hit with a {weapon} following a heated argument at the fairground entrance.",
                "supporting_evidence": observations["cctv_fair_entry"] + [weapon, "injury_reports_from_security_team"],
                "score": 0
            }
#23. Hidden Trap – Pitfall Setup in Forest:
            theory = {
                "hypothesis": f"Victim fell into a concealed pit and was later struck with a {weapon}, suggesting the trap was pre-planned.",
                "supporting_evidence": observations["freshly_dug_soil"] + [weapon, "trap_mechanism_parts"],
                "score": 0
            }
#24. Hidden Trap – Booby Trap with Weapon:
            theory = {
                "hypothesis": f"Victim triggered a hidden trap rigged with a {weapon}, potentially set up to target trespassers.",
                "supporting_evidence": observations["tripwire_fragments"] + [weapon, "unusual_wiring_patterns"],
                "score": 0
            }
#25. Animal Attack Disguised as Murder – Claw Marks Staged:
            theory = {
                "hypothesis": f"Victim’s wounds were made to appear like an animal attack, but analysis suggests they were inflicted using a {weapon}.",
                "supporting_evidence": observations["inconsistent_wound_patterns"] + [weapon, "lack_of_animal_tracks"],
                "score": 0
            }
#26. Animal Attack Disguised – Bear Attack Cover-Up:
            theory = {
                "hypothesis": f"Suspect attempted to mask the killing using a {weapon} by leaving the body near bear territory to simulate a wild attack.",
                "supporting_evidence": observations["tool_marks_on_bones"] + [weapon, "meat_bait_near_scene"],
                "score": 0
            }
#27. Remote Village – Ritual Cover:
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} under the pretense of a local ritual, possibly to hide a personal motive.",
                "supporting_evidence": observations["ceremonial_items_found"] + [weapon, "conflicting_tribal_testimonies"],
                "score": 0
            }
#28. Remote Tribal Area – Outsider Conflict:
            theory = {
                "hypothesis": f"Victim, an outsider, was assaulted with a {weapon} after a territorial dispute with members of a secluded tribal community.",
                "supporting_evidence": observations["camp_supplies_looted"] + [weapon, "local_conflict_history"],
                "score": 0
            }
#29. Drone Attack – Surveillance Turned Deadly:
            theory = {
                "hypothesis": f"Victim was tracked and attacked using a {weapon}-equipped drone in a remote area.",
                "supporting_evidence": observations["drone_parts_found_nearby"] + [weapon, "buzzing_sounds_reported_by_witnesses"],
                "score": 0
            }
#30. Drone as Delivery for Weaponized Payload:
            theory = {
                "hypothesis": f"A drone delivered a harmful payload, releasing a {weapon} that incapacitated the victim.",
                "supporting_evidence": observations["airborne_traces_near_scene"] + [weapon, "remote_controller_fingerprint"],
                "score": 0
            }
#31. Poisoned Berries – Food Trap:
            theory = {
                "hypothesis": f"Victim consumed wild berries laced with a {weapon}-grade toxin, likely planted intentionally.",
                "supporting_evidence": observations["berry_samples"] + [weapon, "lack_of_animal_consumption"],
                "score": 0
            }
#32. Contaminated Water Source:
            theory = {
                "hypothesis": f"Victim drank from a poisoned stream, where traces of {weapon} were later found.",
                "supporting_evidence": observations["water_test_results"] + [weapon, "container_with_residue_near_bank"],
                "score": 0
            }
#33. Survival Gear Sabotage – Broken Climbing Rope:
            theory = {
                "hypothesis": f"Victim fell after climbing gear was sabotaged with a {weapon} or corrosive agent, suggesting premeditation.",
                "supporting_evidence": observations["frayed_rope_analysis"] + [weapon, "discrepancies_in_partner_statements"],
                "score": 0
            }
#34. Boiled Food Poisoning in Survival Camp:
            theory = {
                "hypothesis": f"Victim was poisoned with a {weapon} added to a shared pot of food during a survival training session.",
                "supporting_evidence": observations["shared_utensils_tested_positive"] + [weapon, "symptoms_in_others_present"],
                "score": 0
            }
#35. Abandoned Urban Ruins – Trap in Collapsed Building
            theory = {
                "hypothesis": f"Victim was struck with a {weapon} and left in a partially collapsed building to make the death appear accidental.",
                "supporting_evidence": observations["rubble_placement_inconsistent"] + [weapon, "blood_on_exposed_rebar"],
                "score": 0
            }
#36. Abandoned Urban – Gang Setup
            theory = {
                "hypothesis": f"Victim was lured into the abandoned warehouse and attacked with a {weapon}, possibly as part of a gang-related message.",
                "supporting_evidence": observations["spray_paint_tags"] + [weapon, "burnt_items_near_scene"],
                "score": 0
            } 
#37. Deep Caves – Fall with Foul Play
            theory = {
                "hypothesis": f"Victim was hit with a {weapon} and pushed into a cave shaft, possibly to disguise the murder as a spelunking accident.",
                "supporting_evidence": observations["helmet_with_cracks"] + [weapon, "scuff_marks_near_edge"],
                "score": 0
            } 
#38. Deep Caves – Oxygen Supply Cut
            theory = {
                "hypothesis": f"Victim’s air tank was tampered with using a {weapon}, causing suffocation deep inside the cave system.",
                "supporting_evidence": observations["cut_air_hose"] + [weapon, "conflicting_witness_routes"],
                "score": 0
            } 
#39. Icy Tundra – Blunt Trauma in Blizzard
            theory = {
                "hypothesis": f"Victim was struck with a {weapon} during a blizzard, and the low visibility helped the assailant escape unseen.",
                "supporting_evidence": observations["fractures_in_skull"] + [weapon, "partially_covered_tracks"],
                "score": 0
            } 
#40. Arctic Research Base – Ice Axe Altercation
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} during a dispute at an isolated arctic research base, and the incident was staged as an accident.",
                "supporting_evidence": observations["base_log_tampering"] + [weapon, "security_cam_disconnected_before_event"],
                "score": 0
            }
#41. Virtual Environment – Avatar Termination via Exploit
            theory = {
                "hypothesis": f"Victim’s avatar was targeted using a {weapon}-like virtual exploit, which caused neural shock in the real world.",
                "supporting_evidence": observations["glitched_game_logs"] + [weapon, "biosensor_spike_during_event"],
                "score": 0
            }
#42. Virtual Reality – Code Injection Sabotage
            theory = {
                "hypothesis": f"Victim was exposed to a deadly stimulus in VR via a {weapon}-coded file, suggesting deliberate tampering with simulation rules.",
                "supporting_evidence": observations["malicious_patch_file"] + [weapon, "neural_interface_log_errors"],
                "score": 0
            }
#43. Apocalyptic Wasteland – Resource Conflict
            theory = {
                "hypothesis": f"Victim was killed with a {weapon} over a fight for resources, likely water or food, in a lawless post-collapse zone.",
                "supporting_evidence": observations["empty_supplies"] + [weapon, "territory_markings"],
                "score": 0
            }
#44. Apocalyptic Wasteland – Makeshift Weapon Ambush
            theory = {
                "hypothesis": f"Victim was ambushed with a handcrafted {weapon} in a scavenged trap while traveling alone through ruins.",
                "supporting_evidence": observations["trap_spring_points"] + [weapon, "scavenger_trail"],
                "score": 0
            }
#45. Ritualistic Scene – Symbolic Weapon Use
            theory = {
                "hypothesis": f"Victim was killed with a {weapon} as part of a ritualistic act, indicated by markings and symbolic arrangements at the scene.",
                "supporting_evidence": observations["symbol_drawings_in_blood"] + [weapon, "burnt_offerings_nearby"],
                "score": 0
            }
#46. Psychological Crime – Delusional Attack
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} by someone experiencing a severe psychological break, who believed the victim posed a threat.",
                "supporting_evidence": observations["hallucination_journal_entries"] + [weapon, "lack_of_logical_motive"],
                "score": 0
            }
#47. Time-Travel Paradox – Victim Killed by Future Self
            theory = {
                "hypothesis": f"Victim was murdered by their future self using a {weapon} in an attempt to prevent a paradox from occurring.",
                "supporting_evidence": observations["chronal_displacement_anomalies"] + [weapon, "discrepancies_in_time_record"],
                "score": 0
            }
#48. Time-Travel Paradox – Loop Trap
            theory = {
                "hypothesis": f"Victim’s death was engineered in a time loop, where a {weapon} was used in multiple timelines to ensure the same outcome.",
                "supporting_evidence": observations["time_anomaly_signatures"] + [weapon, "looped_physical_evidence"],
                "score": 0
            }
#49. Dream-State Crime – Murder in Lucid Dream
            theory = {
                "hypothesis": f"Victim was attacked in a lucid dream state, where a {weapon} was used to cause real-world harm while they were trapped in a dream.",
                "supporting_evidence": observations["dream_journal_entries"] + [weapon, "neuroimaging_patterns_of_dream_reality_overlap"],
                "score": 0
            }
#50. Dream-State Crime – Sleep Paralysis Weapon Attack
            theory = {
                "hypothesis": f"Victim experienced sleep paralysis while being assaulted with a {weapon}, and the trauma was mistaken for a nightmare.",
                "supporting_evidence": observations["vocal_tremors_during_sleep"] + [weapon, "bruises_formed_during_paralysis"],
                "score": 0
            }
#51. Multi-Layered Conspiracy – False Flag Operation
            theory = {
                "hypothesis": f"Victim was targeted as part of a multi-layered conspiracy where they were framed as a criminal, leading to their execution with a {weapon}.",
                "supporting_evidence": observations["disguised_identity_documents"] + [weapon, "witness_testimonies_inconsistent_with_scene"],
                "score": 0
            }
#52. Multi-Layered Conspiracy – Political Scapegoat Execution
            theory = {
                "hypothesis": f"Victim was executed as a scapegoat in a political conspiracy, with the use of a {weapon} to ensure a clean, controlled narrative.",
                "supporting_evidence": observations["blackmail_papers"] + [weapon, "strategic_alibis_of_involved_parties"],
                "score": 0
            }
#1. AI Rebellion – Targeted Elimination by Rogue Unit
            theory = {
                "hypothesis": f"Victim was terminated using a {weapon} by an autonomous AI unit acting outside its programmed parameters.",
                "supporting_evidence": observations["unauthorized_AI_protocol_logs"] + [weapon, "robot_movement_outside_assigned_zone"],
                "score": 0
            }
#2. AI-Controlled Environment Trap
            theory = {
                "hypothesis": f"Victim was killed using an environmental {weapon} activated by a smart system hijacked by a rogue AI.",
                "supporting_evidence": observations["system_override_alerts"] + [weapon, "last_user_command_does_not_match_log"],
                "score": 0
            }
#3. Haunted-Tech – Possessed Device Homicide
            theory = {
                "hypothesis": f"Victim was electrocuted through a smart device modified or 'possessed' to deliver a fatal charge using a {weapon}-level current.",
                "supporting_evidence": observations["EM_field_spikes_near_device"] + [weapon, "unexplainable_device_activity_before_death"],
                "score": 0
            }
#4. Haunted-Tech – Audio-Induced Madness
            theory = {
                "hypothesis": f"Victim experienced a psychological break due to subliminal messages transmitted via a haunted audio system, ultimately leading to self-harm with a {weapon}.",
                "supporting_evidence": observations["distorted_audio_logs"] + [weapon, "residual_thermal_energy_signature"],
                "score": 0
            }
 #5. Genetic Memory Trigger – Ancestral Trauma-Induced Homicide
            theory = {
                "hypothesis": f"Victim was killed by someone whose genetic memory was triggered by a shared ancestral conflict, leading to a rage-induced attack with a {weapon}.",
                "supporting_evidence": observations["memory_trigger_sequence"] + [weapon, "overlapping_genetic_markers"],
                "score": 0
            }
 #6. Genetic Memory Loop – History Repeating by Design
            theory = {
                "hypothesis": f"Victim's death mirrored an identical historical murder using a {weapon}, suggesting a repeating genetic behavior pattern stored in memory.",
                "supporting_evidence": observations["crime_scene_matches_ancient_case"] + [weapon, "gene_expression_during_event"],
                "score": 0
            }
 #here’s a fresh batch of car crime theories using your exact format. These include scenarios like tampered brakes, remote hijacking, and staged accidents:
 #7. Brake Line Tampering
            theory = {
                "hypothesis": f"Victim's car brakes were intentionally tampered with using a {weapon}, causing a fatal crash on a downhill slope.",
                "supporting_evidence": observations["cut_brake_line"] + [weapon, "tool_marks_on_master_cylinder"],
                "score": 0
            }
 #8.Remote Control Hijack
            theory = {
                "hypothesis": f"Victim’s vehicle was hacked and remotely controlled to crash, using a {weapon}-like exploit in the car's onboard system.",
                "supporting_evidence": observations["anomalous_steering_input_logs"] + [weapon, "unmatched_signal_frequency"],
                "score": 0
            }
 #9. Staged Accident – Side-Swipe Setup
            theory = {
                "hypothesis": f"Victim was deliberately run off the road using a {weapon} vehicle in a staged side-swipe collision.",
                "supporting_evidence": observations["paint_transfer_from_other_vehicle"] + [weapon, "lack_of_skid_marks"],
                "score": 0
            }
 #10. Trunk Ambush
            theory = {
                "hypothesis": f"Victim was attacked with a {weapon} while accessing their trunk, likely ambushed from behind during routine vehicle use.",
                "supporting_evidence": observations["blood_in_trunk_area"] + [weapon, "footprints_behind_vehicle"],
                "score": 0
}
 #11. Poisoned Cabin Air
            theory = {
                "hypothesis": f"A toxic substance was dispersed into the car’s air vents using a {weapon}, incapacitating the victim while driving.",
                "supporting_evidence": observations["chemical_traces_in_air_filters"] + [weapon, "victim_disorientation_before_crash"],
                "score": 0
            }
 #12. Explosive Device Under Chassis
            theory = {
                "hypothesis": f"A {weapon} was attached beneath the car, remotely detonated as the vehicle reached a specific location.",
                "supporting_evidence": observations["blast_pattern_under_chassis"] + [weapon, "remote_detonation_signal_detected"],
                "score": 0
            }
#1–10: Mechanical Tampering
            theory = {
                "hypothesis": f"Victim’s brake lines were cut using a {weapon}, leading to loss of control on a steep road.",
                "supporting_evidence": observations["cut_brake_line"] + [weapon, "tool_marks_on_cylinder"],
                "score": 0
            }
            theory = {
                "hypothesis": f"The fuel line was pierced with a {weapon}, causing a fire post-ignition.",
                "supporting_evidence": observations["fuel_leak_origin"] + [weapon, "burn_patterns_under_vehicle"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Steering column was sabotaged using a {weapon}, locking the wheel during a turn.",
                "supporting_evidence": observations["damage_to_steering_mechanism"] + [weapon, "lack_of_skid_marks"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim's tires were slashed with a {weapon}, forcing them to stop and be ambushed.",
                "supporting_evidence": observations["tire_puncture_patterns"] + [weapon, "tracks_leading_to_ambush_point"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Accelerator pedal was jammed using a {weapon} part, preventing deceleration.",
                "supporting_evidence": observations["pedal_wedge_evidence"] + [weapon, "high_speed_impact_analysis"],
                "score": 0
            }
            theory = {
                "hypothesis": f"The engine was rigged with a {weapon} to explode upon reaching high temperature.",
                "supporting_evidence": observations["engine_block_shrapnel"] + [weapon, "heat_trigger_signatures"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Transmission fluid was replaced with a corrosive {weapon}-based liquid to disable controls mid-drive.",
                "supporting_evidence": observations["chemical_corrosion_inside_gearbox"] + [weapon, "fluid_container_in_trunk"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Suspension bolts were loosened using a {weapon}, causing destabilization on turns.",
                "supporting_evidence": observations["missing_bolts"] + [weapon, "unusual_body_roll"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Exhaust system was blocked with a {weapon}, causing toxic gas buildup inside.",
                "supporting_evidence": observations["carbon_monoxide_in_cabin"] + [weapon, "melted_polymer_near_exhaust"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A {weapon} was wedged under the hood to prevent safe steering movement during ignition.",
                "supporting_evidence": observations["indentation_in_steering_gear"] + [weapon, "object_imprints_on_hood_liner"],
                "score": 0
            }
 #11–20: Remote Control & Tech Hacks
            theory = {
                "hypothesis": f"Vehicle was hacked using a {weapon}-based exploit, redirecting GPS and crashing into a wall.",
                "supporting_evidence": observations["corrupted_gps_log"] + [weapon, "external_device_signal_trace"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Car doors were locked remotely using a {weapon} to trap victim before crash.",
                "supporting_evidence": observations["electronic_lock_override_log"] + [weapon, "no_external_force_entry"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Infotainment system was used to distract victim by deploying a {weapon}-style visual attack.",
                "supporting_evidence": observations["glitched_screen_recording"] + [weapon, "eye_movement_data"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Vehicle’s automated lane system was overridden using a {weapon} to guide it into oncoming traffic.",
                "supporting_evidence": observations["lane_assist_overload_log"] + [weapon, "collision_trajectory_analysis"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A virus disguised as a software update was uploaded using a {weapon} device to disable safety systems.",
                "supporting_evidence": observations["unauthorized_usb_access"] + [weapon, "event_log_with_firmware_signature"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A {weapon} was used to jam emergency braking radar sensors, leading to a fatal rear-end crash.",
                "supporting_evidence": observations["sensor_error_log"] + [weapon, "crash_point_unexpected_delay"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A fake over-the-air update disguised as a recall introduced a {weapon}-class bug to disable collision warning.",
                "supporting_evidence": observations["firmware_check_failed"] + [weapon, "unauthorized_manufacturer_signature"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Steering assist was remotely locked at high speed using a {weapon}-grade signal emitter.",
                "supporting_evidence": observations["remote_input_log_mismatch"] + [weapon, "steering_motor_lock_readout"],
                "score": 0
            }
            theory = {
                "hypothesis": f"The car’s microphone system was hacked to eavesdrop and track the victim’s route using a {weapon}.",
                "supporting_evidence": observations["microphone_feedback_loop"] + [weapon, "background_noise_analysis"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A {weapon} signal repeater was used to clone the key fob and unlock the vehicle remotely before planting evidence.",
                "supporting_evidence": observations["rf_signal_repeat_patterns"] + [weapon, "victim_fob_still_secure"],
                "score": 0
            }
#: Direct Assaults and Ambushes
            theory = {
                "hypothesis": f"Victim was shot with a {weapon} through the driver-side window during a stoplight ambush.",
                "supporting_evidence": observations["glass_fragment_trajectory"] + [weapon, "bullet_entry_angle"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was pulled from the vehicle and assaulted with a {weapon} in a parking lot.",
                "supporting_evidence": observations["drag_marks_on_ground"] + [weapon, "defensive_wounds_analysis"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A {weapon} was used to shatter the windshield and attack the victim inside the car.",
                "supporting_evidence": observations["windshield_impact_pattern"] + [weapon, "blood_spray_inside_cabin"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was poisoned via spiked beverage left in the car by a person using a {weapon}-coated container.",
                "supporting_evidence": observations["residue_in_cupholder"] + [weapon, "toxicology_report"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was lured to vehicle under false pretense, then attacked with a {weapon} inside passenger seat.",
                "supporting_evidence": observations["fake_note_on_dashboard"] + [weapon, "blood_on_passenger_mat"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A {weapon} was hidden beneath the driver’s seat and activated remotely as victim entered.",
                "supporting_evidence": observations["device_wiring_under_seat"] + [weapon, "timing_with_door_sensor"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was forced into car trunk and suffocated using a {weapon}-based gas delivery system.",
                "supporting_evidence": observations["scratches_inside_trunk"] + [weapon, "gas_canister_residue"],
                "score": 0
            }
            theory = {
                "hypothesis": f"Victim was struck by a {weapon} while exiting vehicle, likely ambushed from behind.",
                "supporting_evidence": observations["blood_on_door_frame"] + [weapon, "entry_point_alignment"],
                "score": 0
            }
            theory = {
                "hypothesis": f"A pre-installed {weapon} in the dashboard detonated after ignition, targeting the victim directly.",
                "supporting_evidence": observations["blast_origin_from_dashboard"] + [weapon, "electrical_timer_circuit"],
                "score": 0
            }
        theory = {
                "hypothesis": f"The rearview mirror was modified to inject a blinding flash from a {weapon} source, causing the crash.",
                "supporting_evidence": observations["scorch_marks_on_mirror"] + [weapon, "burned_retina_signs"],
                "score": 0
            }
 #: Staged & Insurance-Driven Crimes
        theory = {
                "hypothesis": f"The accident was staged using a {weapon} vehicle to claim insurance; victim was unaware they were marked.",
                "supporting_evidence": observations["identical_claims_by_other_driver"] + [weapon, "pre-crash_contact_logs"],
                "score": 0
            }
        theory = {
                "hypothesis": f"A {weapon} was planted in the car to make it appear as if the victim was armed and aggressive during a traffic stop.",
                "supporting_evidence": observations["inconsistent_fingerprint_patterns"] + [weapon, "recording_of_planting_event"],
                "score": 0
            }
        theory = {
                "hypothesis": f"The vehicle was deliberately driven into a wall by another party using the victim’s identity and a forged license with a {weapon}.",
                "supporting_evidence": observations["fake_id_near_crash_site"] + [weapon, "witness_description_mismatch"],
                "score": 0
            }
        theory = {
                "hypothesis": f"Victim's car was switched with a rigged duplicate using a {weapon}-equipped tow truck before the crash.",
                "supporting_evidence": observations["vin_number_discrepancy"] + [weapon, "tow_marks_on_ground"],
                "score": 0
            }
        theory = {
                "hypothesis": f"Victim staged their own crash with a {weapon} to fake death and escape fraud investigation.",
                "supporting_evidence": observations["blood_type_does_not_match_victim"] + [weapon, "recent_large_withdrawals"],
                "score": 0
            }
        theory = {
                "hypothesis": f"A {weapon}-coated wire was used to disable the airbags before orchestrated collision.",
                "supporting_evidence": observations["airbag_module_opened"] + [weapon, "disconnected_sensor_logs"],
                "score": 0
            }
        theory = {
                "hypothesis": f"Crash was meant to look accidental, but a {weapon} residue shows chemical ignition of fuel line.",
                "supporting_evidence": observations["chemical_traces_near_gas_tank"] + [weapon, "fire_origin_analysis"],
                "score": 0
            }
        theory = {
                "hypothesis": f"A stolen car was crashed intentionally and left with the victim inside to make the death appear random; keys planted using a {weapon}.",
                "supporting_evidence": observations["entry_log_discrepancy"] + [weapon, "fob_tampering"],
                "score": 0
            }
        theory = {
                "hypothesis": f"Victim was tied to the driver’s seat with {weapon} material and driven off a cliff while unconscious.",
                "supporting_evidence": observations["binding_marks_on_wrists"] + [weapon, "lack_of_braking_reaction"],
                "score": 0
            }
        theory = {
                "hypothesis": f"Victim was coerced into driving a car loaded with illegal items, with a {weapon} as leverage, leading to fatal pursuit.",
                "supporting_evidence": observations["threat_messages_on_phone"] + [weapon, "contraband_recovered"],
                "score": 0
            }
 #: Miscellaneous & Unusual Scenarios
        theory = {
                "hypothesis": f"Victim was intentionally locked in the vehicle during a heatwave, with windows sealed using a {weapon} adhesive.",
                "supporting_evidence": observations["sealant_residue_on_windows"] + [weapon, "body_temperature_analysis"],
                "score": 0
            }
        theory = {
            "hypothesis": f"Victim was electrocuted by a rigged seat circuit connected to a {weapon}-modified battery.",
            "supporting_evidence": observations["burn_marks_on_seat"] + [weapon, "wiring_diagram_anomalies"],
            "score": 0
        }
        theory = {
            "hypothesis": f"A strong {weapon} was used to magnetically disable vehicle controls at high speed.",
            "supporting_evidence": observations["distorted_control_module_readings"] + [weapon, "metal_shard_patterns"],
            "score": 0
        }
        theory = {
            "hypothesis": f"Victim was kidnapped from their vehicle after being gassed through the air vents using a {weapon}-based sedative.",
            "supporting_evidence": observations["sedative_trace_in_filter"] + [weapon, "unlocked_door_sequence"],
            "score": 0
        }
        theory = {
            "hypothesis": f"The rear tires were replaced with faulty ones using a {weapon}-equipped jack during valet service, leading to a blowout crash.",
            "supporting_evidence": observations["inconsistent_tire_serials"] + [weapon, "valet_service_log"],
            "score": 0
        }
        theory = {
            "hypothesis": f"A {weapon} was installed in the vehicle’s undercarriage to track and intercept the victim in a remote location.",
            "supporting_evidence": observations["tracker_logs"] + [weapon, "interception_timing_with_gps_path"],
            "score": 0
        }
        theory = {
            "hypothesis": f"Victim was misled by fake signage and GPS updates into entering a construction pit set with a {weapon}.",
            "supporting_evidence": observations["gps_override_data"] + [weapon, "fake_road_sign_materials"],
            "score": 0
        }
        theory = {
            "hypothesis": f"A {weapon}-based smoke bomb was set off in the cabin mid-drive, causing panic and crash.",
            "supporting_evidence": observations["smoke_residue_on_dashboard"] + [weapon, "open_window_escape_attempt"],
            "score": 0
        }
        theory = {
            "hypothesis": f"The trunk was loaded with a {weapon}-heavy object rigged to roll forward and crush victim during a sharp stop.",
            "supporting_evidence": observations["trunk_weight_distribution"] + [weapon, "impact_angle_to_seatback"],
            "score": 0
        }
        theory = {
            "hypothesis": f"Victim’s car was rerouted via spoofed GPS to an isolated area where attackers used a {weapon} to ambush them.",
            "supporting_evidence": observations["gps_fake_waypoint_logs"] + [weapon, "footprints_near_crash_site"],
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
print("No error found..........................")