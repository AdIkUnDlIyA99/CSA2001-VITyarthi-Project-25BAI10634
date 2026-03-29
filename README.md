# 🎮 GameMatch AI — Game Recommendation System

> **VITyarthi Fundamentals in AI and ML**
> Subject Code: **CSA2001**
> Student: **Aditya Kundliya**
> Registration Number: **25BAI10634**

---

## 📌 Project Overview

**GameMatch AI** is a web-based game recommendation system that suggests PC games based on the user's hardware specifications and preferred genre. The user selects their RAM, Processor, Graphics Card, and Genre from dropdowns — and the system fetches real, highly-rated matching games from the **RAWG Video Games Database API**, along with a performance compatibility label based on the user's GPU and the game's release year.

---

## 🗂 Repository Structure

```
Game-Recommender_AI/
│
├── Backend/
│   ├── app.py               # FastAPI backend — handles API calls and recommendation logic
│   └── requirements.txt     # Python dependencies
│
└── Frontend/
    └── index.html           # Frontend UI — dropdowns, results, game cards with cover images
```

---

## 🧠 How It Works

1. User selects their **RAM**, **Processor**, **Graphics Card**, and **Genre** from the dropdowns
2. The frontend sends a `POST` request to the **FastAPI backend** at `http://localhost:8000/recommend`
3. The backend:
   - Maps the selected genre to a **RAWG API genre slug**
   - Fetches the **top-rated PC games** in that genre from RAWG
   - Calculates a **performance label** (Runs Great / Runs Well / Runs OK / May Struggle) by comparing the GPU tier against the game's release year demand
4. Results are returned to the frontend and displayed as **game cards** with cover images, ratings, developer info, and performance labels

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript (Vanilla) |
| Backend | Python, FastAPI, Uvicorn |
| Game Data | RAWG Video Games Database API (Free) |
| HTTP Client | Python `requests` library |

---

## 🚀 Setup & Execution

### Step 1 — Get a Free RAWG API Key

1. Go to 👉 [https://rawg.io/apidocs](https://rawg.io/apidocs)
2. Click **"Get API Key"**
3. Sign up for a free account (no credit card required)
4. Copy your API key

### Step 2 — Paste the API Key into the Backend

Open `Backend/app.py` and find this line near the top:

```python
RAWG_API_KEY = "YOUR_RAWG_API_KEY_HERE"
```

Replace `YOUR_RAWG_API_KEY_HERE` with your actual key:

```python
RAWG_API_KEY = "abc123youractualkey"
```

Save the file.

### Step 3 — Install Dependencies

Open a terminal (PowerShell or Command Prompt), navigate to the Backend folder:

```bash
cd Desktop/Game-Recommender_AI/Backend
```

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4 — Start the Backend Server

```bash
python -m uvicorn app:app --reload
```

You should see this output confirming the server is running:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process using StatReload
```

> ⚠️ Keep this terminal window open while using the app. If you close it, the backend stops.

### Step 5 — Open the Frontend

Navigate to the `Frontend` folder and double-click `index.html` to open it in your browser.

Or right-click `index.html` → **Open with** → **Chrome / Edge / Firefox**

---

## 🎮 How to Use the App

Once the backend is running and `index.html` is open in your browser:

1. **Select your RAM** from the dropdown (e.g. `16 GB`)
2. **Select your Processor** from the dropdown (e.g. `Intel Core i5-12400H (12th Gen)`)
3. **Select your Graphics Card** from the dropdown
   - If you have no dedicated GPU (laptop with integrated graphics), select **"No Dedicated GPU (Integrated Graphics)"**
4. **Select your preferred Genre** (e.g. `First-Person Shooter (FPS)`, `RPG`, `Battle Royale`, etc.)
5. Click the **"FIND MY GAMES"** button
6. Wait a moment while the backend fetches results from RAWG
7. Your **6 recommended games** will appear as cards showing:
   - 🖼 Game cover image
   - 🎮 Title and genre tags
   - ⭐ Metacritic rating
   - 📅 Release year
   - 🏢 Developer
   - 💻 Performance label based on your GPU

---

## 🔍 Performance Labels Explained

| Label | Meaning |
|---|---|
| ✅ Runs Great | Your GPU is well above what the game needs |
| 🟢 Runs Well | Your GPU comfortably handles the game |
| 🟡 Runs OK | Your GPU meets the game's requirements |
| 🔴 May Struggle | Your GPU may have difficulty running this game smoothly |

> Performance is estimated by comparing your GPU's power tier against the game's release year demand. Newer games require more powerful hardware.

---

## 🛠 Troubleshooting

| Problem | Fix |
|---|---|
| `uvicorn` not recognized | Use `python -m uvicorn app:app --reload` instead |
| `pip install -r requirements` fails | Make sure to include `.txt`: `pip install -r requirements.txt` |
| "No games found for this genre" | Your RAWG API key is missing or invalid — check Step 2 |
| "Cannot reach the backend" error in browser | Make sure the backend terminal is still running |
| Frontend shows blank / no results | Open browser DevTools (F12) → Console tab for error details |

---

## 📦 Dependencies (`requirements.txt`)

```
fastapi
uvicorn
requests
```

---

*Submitted as part of the VITyarthi Fundamentals in AI and ML course — CSA2001*
*Aditya Kundliya | 25BAI10634*
