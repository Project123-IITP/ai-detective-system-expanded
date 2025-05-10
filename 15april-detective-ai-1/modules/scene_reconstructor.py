def reconstruct_scene(best_theory):
    hypothesis = best_theory["hypothesis"]
    evidence = best_theory.get("supporting_evidence", [])

    if len(evidence) < 2:
        return "Not enough evidence to reconstruct the scene based on the current theory."

    reconstruction_story = (
        f"Reconstruction based on best theory:\n"
        f"According to the analysis, the {evidence[-2]} was likely used by the perpetrator after entering through the {evidence[-1]}.\n"
        f"The crime resulted in the following signs of violence: {', '.join(evidence[:-2])}.\n"
        f"Conclusion: {hypothesis}"
    )
    return reconstruction_story
