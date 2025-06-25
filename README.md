# 🔭 Laser Tracking Simulator

A simulation project for detecting and centring a laser beam in noisy video frames using computer vision and feedback control — inspired by real-world satellite optical communication challenges.

## 🚀 What it does
- Simulates noisy video of a laser spot (like a beacon from a satellite).
- Detects the spot using OpenCV-based blob detection.
- Uses a simulated fast steering mirror (FSM) with PID control to keep the laser centred.
- Plots tracking error, response time, and other performance metrics.

## 📦 Requirements
- Python 3.8+
- OpenCV
- Matplotlib
- Pillow

Install with:
```bash
pip install -r requirements.txt

