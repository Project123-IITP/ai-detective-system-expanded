def get_legal_actions(best_theory):
    hypothesis = best_theory["hypothesis"].lower()
    ipc_sections = []
    steps = []
    departments = []

    if "knife" in hypothesis or "stab" in hypothesis:
        ipc_sections.extend(["IPC 302 - Murder", "IPC 326 - Causing grievous hurt with weapon"])
        steps.append("Secure weapon and check fingerprints")
        departments.extend(["Forensics", "Homicide Unit"])

    if "broken_window" in hypothesis:
        ipc_sections.append("IPC 457 - House-breaking by night")
        steps.append("Inspect entry point for evidence")
        departments.append("Crime Scene Unit")

    if "overturned_chair" in hypothesis:
        steps.append("Assess struggle evidence")
        departments.append("Field Forensics")

    return {
        "ipc_sections": ipc_sections,
        "recommended_steps": steps,
        "responsible_departments": departments
    }
