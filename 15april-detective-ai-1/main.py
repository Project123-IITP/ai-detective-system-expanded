from modules.image_processor import process_image
from modules.observation_extractor import extract_observations
from modules.case_matcher import match_previous_cases
from modules.theory_generator import generate_and_evaluate_theories
from modules.scene_reconstructor import reconstruct_scene
from modules.legal_advisor import get_legal_actions
import os

def run_pipeline(image_path):
    print("[1] Processing crime scene image...")
    scene_data = process_image(image_path)

    print("[2] Extracting observations and investigation parameters...")
    observations = extract_observations(scene_data)

    print("[3] Matching similar previous cases...")
    matched_cases = match_previous_cases(observations)

    print("[4] Generating and evaluating theories...")
    best_theory = generate_and_evaluate_theories(observations, matched_cases)

    print("[5] Reconstructing the crime scene...")
    reconstruction = reconstruct_scene(best_theory)

    print("[6] Compiling legal actions and investigation steps...")
    legal_report = get_legal_actions(best_theory)

    return {
        "scene_data": scene_data,
        "observations": observations,
        "matched_cases": matched_cases,
        "best_theory": best_theory,
        "reconstruction": reconstruction,
        "legal_report": legal_report,
    }

if __name__ == "__main__":
    image_path = input("Enter the full path to the crime scene image: ").strip()
    if not os.path.isfile(image_path):
        print("❌ The file does not exist. Exiting.")
        exit(1)
    results = run_pipeline(image_path)
    print("\n\n--- Final Crime Scene Report ---")
    for key, value in results.items():
        print(f"\n>> {key.upper()}\n{value}")
