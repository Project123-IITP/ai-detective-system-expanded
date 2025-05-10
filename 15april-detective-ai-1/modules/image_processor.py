from ultralytics import YOLO
from datetime import datetime

# Load fine-tuned crime-scene-specific model
model = YOLO("model/best.pt")

CRIME_LABELS = {
    0: "bloodied_knife",
    1: "broken_window",
    2: "overturned_chair",
    3: "blood_on_bed"
}

def process_image(image_path):
    print(f"[YOLO] Analyzing image: {image_path}")
    results = model(image_path)

    print("\n[DEBUG] YOLO Detections:")
    objects = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = CRIME_LABELS.get(cls_id, f"class_{cls_id}")
        conf = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        print(f"- {label} ({conf:.2f}) at ({center_x:.0f}, {center_y:.0f})")
        objects.append({
            "label": label,
            "confidence": round(conf, 2),
            "position": (round(center_x), round(center_y))
        })

    return {
        "image_path": image_path,
        "objects": objects,
        "timestamp": datetime.now().isoformat(),
        "location": "Unknown (YOLO model does not infer location)"
    }
