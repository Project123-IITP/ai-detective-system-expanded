# 🕵️ AI Detective System (Final Version)

This project is a generative AI system designed to analyze crime scene images, extract observations, match with previous cases, generate investigation theories, reconstruct scenes, and recommend legal actions based on IPCs.

## 🚀 How to Run

### Option 1: Docker
```bash
docker build -t ai-detective .
docker run -it --rm -v "$(pwd):/app" ai-detective
```

### Option 2: Local Python
```bash
pip install -r requirements.txt
python main.py
```

When prompted, enter:
```
/app/WhatsApp Image 2025-04-11 at 17.06.45.jpeg
```

## 🤖 Powered by:
- YOLOv8 (fine-tuned for crime scene detection)
- Custom logic for theory evaluation and IPC recommendation
