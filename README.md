<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0f1e,50:7c1d1d,100:ef4444&height=200&section=header&text=Hand%20Volume%20Controller&fontSize=42&fontColor=ffffff&fontAlignY=40&desc=Vision-Based%20Audio%20Control%20%E2%80%A2%20OpenCV%20%E2%80%A2%20Gesture%20HCI&descAlignY=60&descSize=16&animation=fadeIn" />

<br/>

[![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Bhogi123-T/Hand-volume-controller)
[![OpenCV](https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://github.com/Bhogi123-T/Hand-volume-controller)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://github.com/Bhogi123-T/Hand-volume-controller)

[![Author](https://img.shields.io/badge/Author-Bhogeswara%20Rao%20T-ef4444?style=flat-square)](https://github.com/Bhogi123-T)
[![File](https://img.shields.io/badge/Core%20File-hand__volume__control.py-ef4444?style=flat-square&logo=python)](https://github.com/Bhogi123-T/Hand-volume-controller/blob/main/hand_volume_control.py)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

</div>

---

## 📌 Overview

**Hand Volume Controller** is a computer vision application that maps the distance between your thumb and index finger to your system's volume level — in real time, through your webcam. Simply pinch closer to lower the volume, spread wider to raise it. No keyboard shortcut. No mouse scroll. Just your hand.

The entire system lives in a single, clean Python file: `hand_volume_control.py`.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔊 Touch-Free Volume Control | Adjust system volume with hand gestures — no hardware needed |
| ✋ Vision-Based Gesture Mapping | Thumb-to-index finger distance maps directly to volume percentage |
| ⚡ Real-Time Response | Minimal latency between gesture and volume change |
| 🎯 High Accuracy | Stable landmark tracking prevents jitter and accidental spikes |
| 🧹 Single-File Architecture | Entire system in `hand_volume_control.py` — clean and simple |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 100% |
| Computer Vision | OpenCV (`cv2`) |
| Hand Tracking | MediaPipe |
| Volume Control | Pycaw (Windows) / osascript (macOS) |
| Math | NumPy — distance & interpolation |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Bhogi123-T/Hand-volume-controller.git
cd Hand-volume-controller

# Install dependencies
pip install opencv-python mediapipe numpy pycaw comtypes

# Run
python hand_volume_control.py
```

> **macOS users:** Replace `pycaw` with `osascript` integration.  
> **Linux users:** Use `amixer` or `pactl` for volume control.

---

## 🤚 How the Gesture Works

```
Webcam captures hand
        ↓
MediaPipe detects thumb tip (landmark 4)
        and index finger tip (landmark 8)
        ↓
NumPy calculates Euclidean distance between them
        ↓
Distance interpolated → Volume range (0% to 100%)
        ↓
Pycaw sets system volume instantly
```

| Hand Position | Volume |
|--------------|--------|
| Fingers fully spread | 🔊 100% |
| Mid-spread | 🔉 50% |
| Pinched together | 🔇 0% (Mute) |

---

## ⚙️ Requirements

```
Python 3.7+
opencv-python
mediapipe
numpy
pycaw (Windows) / osascript (macOS)
comtypes (Windows)
```

---

## 🤝 Contributing

Pull requests are welcome. Ideas: add brightness control, media playback gestures, or multi-hand support.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ef4444,100:0a0f1e&height=100&section=footer&animation=fadeIn" />

**Built by [Bhogeswara Rao T](https://github.com/Bhogi123-T) · Chennai, India**

</div>
