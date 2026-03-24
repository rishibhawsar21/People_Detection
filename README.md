#  People Tracking & Counting System

A real-time **People Detection, Tracking, and Counting System** built using **Python, OpenCV, and DeepSort**.
This project detects people in a video, assigns unique IDs, and counts how many people move in or out of a defined region.

---

## 🚀 Features

* 🎯 Real-time **Person Detection**
* 🔄 **Multi-object tracking** using DeepSort
* 🆔 Unique ID assigned to each person
* ➕ **In/Out Counting System**
* ⚡ Efficient and optimized tracking pipeline
* 📦 Modular and clean code structure

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **DeepSort (deep_sort_realtime)**
* **NumPy**

---

## 📁 Project Structure

```
People_detection/
│
├── main.py                  # Main execution file
├── src/
│   ├── detector.py          # Person detection logic
│   ├── tracker.py           # DeepSort tracking logic
│   ├── counter.py           # In/Out counting logic
│   └── utils/
│       └── visualization.py # Drawing bounding boxes & UI
│
├── videos/                  # Input videos (not uploaded to GitHub)
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## 📊 How It Works

1. **Detection**
   Detects people in each frame using a detection model.

2. **Tracking (DeepSort)**

   * Assigns a unique ID to each detected person
   * Tracks movement across frames

3. **Counting Logic**

   * Defines a virtual line
   * Counts people moving **IN** or **OUT**

---

## 📸 Output Example

* Bounding boxes around people
* Unique IDs displayed
* Real-time IN / OUT counter

---


## 🔥 Future Improvements

* ✅ Replace DeepSort with ByteTrack
* ✅ Add YOLOv8 for better detection
* ✅ Deploy as a web app
* ✅ Add real-time webcam support

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 📬 Contact

If you have any questions or suggestions, feel free to connect!

---
