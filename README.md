# 🎮 GameMatch AI — CLI Edition  

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-green)
![API](https://img.shields.io/badge/API-RAWG-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Course](https://img.shields.io/badge/CSA2001-AI%20%26%20ML-purple)

> 🚀 A smart CLI-based Game Recommendation System that suggests games based on your PC specs and predicts performance.

---

## 👤 Student Details  

- **Name:** Aditya Kundliya  
- **Registration Number:** 25BAI10634  
- **Course:** B.Tech CSE (AI & ML)  
- **Subject:** Fundamentals in AI and ML  
- **Subject Code:** CSA2001  
- **Submission Platform:** VITyarthi  

---

## 🧠 Project Overview  

GameMatch AI is a **Command Line Interface (CLI)** application that:
- 🎮 Recommends games based on your **system configuration**
- ⚙️ Uses **RAM + CPU + GPU weighted scoring**
- 📊 Predicts real-world performance
- 🌐 Fetches live game data using an external API  

---

## ✨ Features  

- 🖥️ Fully CLI-based (No GUI required)  
- ⚡ Fast and lightweight  
- 🧩 Multi-parameter evaluation system  
- 🎯 Intelligent performance prediction  
- 🌍 Real-time game data from API  

---

## 🏗️ Repository Structure  

```
Game-Recommender/
│
├── cli.py              # 🚀 Entry point (CLI app)
├── utils.py            # 🧠 Core logic & scoring system
├── requirements.txt    # 📦 Dependencies
└── README.md           # 📄 Documentation
```

---

## 🚀 Getting Started  

### 1️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Application  
```bash
python cli.py
```

---

## 🧾 Example Usage  

### 🔽 Input  
```
Enter RAM: 16 GB  
Enter CPU: i5 12th gen  
Enter GPU: RTX 4090  
Enter Genre: Indie  
```

### 🔼 Output  
```
🎮 Hades  
   Released in 2020 — Runs great  
   ⭐ 4.4/5 | 2020  
```

---

## 🧮 Performance Calculation  

The system computes a **System Power Score** using:

| Component | Weight |
|----------|--------|
| GPU      | 50% ⚡ |
| CPU      | 30% 🧠 |
| RAM      | 20% 💾 |

### 🎯 Output Labels:
- 🟢 Runs great  
- 🟡 Runs well  
- 🟠 Runs OK  
- 🔴 May struggle  

---

## 🌐 API Integration  

- RAWG Video Games Database API  
  → Used for fetching game details like ratings, release year, and genres  

---

## 📸 CLI Preview  

```
🎮 GameMatch AI (CLI Mode)

Enter RAM: 16 GB
Enter CPU: i5
Enter GPU: RTX 3060
Enter Genre: Action

🔥 Recommendations:

🎮 Red Dead Redemption 2
   Released in 2018 — Runs well
   ⭐ 4.6/5 | 2018
```

---

## 💡 Key Highlights  

- ✅ Meets **CLI-based project requirement**  
- 🧠 Implements **AI-style decision logic**  
- 🧩 Modular and scalable code structure  
- ⚙️ Real-world system simulation  

---

## 🏁 Conclusion  

This project demonstrates how **basic AI/ML concepts** like scoring, classification, and recommendation systems can be applied to build a practical CLI-based application.

---

## ⚠️ Important Notes  

- 🔑 Add your RAWG API key in `utils.py`  
- 🌐 Requires internet connection  
- 🧪 Input format should be reasonable (e.g., “16 GB”, “RTX 3060”)  

---

## ⭐ If you like this project  
Give it a ⭐ on GitHub — it helps!
