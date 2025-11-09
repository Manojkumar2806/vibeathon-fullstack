# ⚡ HeatX – Industrial Energy Intelligence Platform

> ![FastAPI](https://img.shields.io/badge/FastAPI-%23009688.svg?style=for-the-badge\&logo=fastapi\&logoColor=white)
> ![Next.js](https://img.shields.io/badge/Next.js-%23000000.svg?style=for-the-badge\&logo=nextdotjs\&logoColor=white)
> ![TailwindCSS](https://img.shields.io/badge/TailwindCSS-%2338B2AC.svg?style=for-the-badge\&logo=tailwind-css\&logoColor=white)
> ![Framer Motion](https://img.shields.io/badge/FramerMotion-%23E4405F.svg?style=for-the-badge\&logo=framer\&logoColor=white)
> ![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge\&logo=python\&logoColor=white)
> ![Scikit-learn](https://img.shields.io/badge/ScikitLearn-%23F7931E.svg?style=for-the-badge\&logo=scikitlearn\&logoColor=white)
> ![Blockchain](https://img.shields.io/badge/Blockchain-%23000000.svg?style=for-the-badge\&logo=ethereum\&logoColor=white)
> ![MongoDB](https://img.shields.io/badge/MongoDB-%2347A248.svg?style=for-the-badge\&logo=mongodb\&logoColor=white)
> ![Vercel](https://img.shields.io/badge/Vercel-%23000000.svg?style=for-the-badge\&logo=vercel\&logoColor=white)

 

---

## 🌍 What is HeatX?

*HeatX* is an AI-driven Industrial Energy Intelligence Platform that transforms wasted heat from manufacturing units into usable electricity — autonomously and sustainably.
It optimizes energy recovery, predicts output, and enables *real-time carbon credit tracking* through a secure blockchain-integrated *Carbon Credit Trading System (CCTS)*.

> 💡 Think of HeatX as the “Brain of Industrial Sustainability” — turning lost heat into value while reducing carbon emissions.

---

## 🎯 Why HeatX?

Every year, industries lose up to *60% of their thermal energy*.
*HeatX* bridges the gap between energy wastage and green recovery, empowering industries to:

* ♻ Convert waste heat into electricity automatically
* 🔋 Predict real-time energy potential using ML models
* 🧠 Self-optimize dynamically with localized models
* 🪙 Trade carbon credits securely through blockchain

> “AI meets Energy. Blockchain meets Sustainability.”

---

## 🔗 Live Demos & Resources

* 🌐 *Frontend (Next.js)* → [Visit HeatX Dashboard](https://your-heatx-app.vercel.app/)
* ⚙ *Backend (FastAPI)* → [HeatX Energy API](http://localhost:8000/docs)
* 📦 *CCTS Integration* → /ccts/mint, /ccts/transfer, /ccts/tx/{id}
* 🧠 *Model Insight* → /analyze route for regression-based predictions

## 📸 UI Showcase

| ![WhatsApp Image 2025-11-09 at 03 07 34\_7d8c10fd](https://github.com/user-attachments/assets/db820d0f-ee06-4412-99ef-136e1874b004) | ![WhatsApp Image 2025-11-09 at 04 37 18\_6a5d2228](https://github.com/user-attachments/assets/bac0bb8e-9e4d-4e9d-ac1c-56e400bdad5d) | ![WhatsApp Image 2025-11-09 at 04 37 19\_342c2e90](https://github.com/user-attachments/assets/a97477a2-7583-4a91-882b-c59bb24e88df) |
| :---------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------: |
|                                                      Heat Conversion Dashboard                                                      |                                                   Blockchain Carbon Credit System                                                   |                                                    AI Model Analysis and Insights                                                   |


## 🧠 Core Workflow

```
graph TD
  A[Heat Sensors] --> B[FastAPI Backend]
  B --> C[ML Model - Gradient Boosting Regressor]
  C --> D[Prediction & Efficiency Analysis]
  D --> E[HeatX Dashboard (Next.js + Tailwind)]
  E --> F[CCTS Blockchain System]
  F --> G[Carbon Credit Minting & Tracking]
```


### ⚙ Backend Architecture

| *Component*       | *Description*                                                 |
| ----------------- | ------------------------------------------------------------- |
| *FastAPI*         | High-performance backend API for prediction & analytics       |
| *Scikit-Learn*    | Gradient Boosting Regression model for heat-energy prediction |
| *CCTS Blockchain* | HMAC-authenticated carbon credit ledger system                |
| *Pandas*          | Data handling and model preprocessing                         |
| *Uvicorn*         | ASGI server for fast concurrent requests                      |

---

### 🗾 Sample Model Output

```json
{
  "r2_train": 0.9525,
  "r2_test": 0.9517,
  "cv_scores": [0.9498, 0.9401, 0.9502, 0.9478, 0.9520],
  "cv_mean": 0.9480,
  "feature_importances": [0.8270, 0.1586, 0.0084, 0.0058]
}
```

---

## 💻 Frontend (Next.js + TailwindCSS)

### ✨ Key Highlights

* ⚡ Real-time AI Analytics Dashboard
* 🌡 Gradient KPI Cards for Heat, Power, CO₂ Reduction, Efficiency
* 📈 Framer Motion animated charts
* 🔗 CCTS page integrated with blockchain API
* 🧱 Scrollable glassmorphic UI

### Tech Stack Summary

| Tech Stack              | Use Case                                        |
| ----------------------- | ----------------------------------------------- |
| Next.js 14 (App Router) | Routing, server-side rendering, API integration |
| TailwindCSS             | Modern, adaptive UI styling                     |
| Framer Motion           | Interactive UI transitions                      |
| Axios                   | Backend API communication                       |

---

## 🔗 CCTS (Carbon Credit Trading System)

A blockchain-inspired carbon ledger that:

* 🪙 Mints new credits for verified energy recovery
* 🔄 Transfers credits between organizations
* 🔐 Uses HMAC-SHA256 signature verification for secure transactions

**Example Mint Request:**

```bash
curl -X POST "http://localhost:8000/ccts/mint" \
  -H "x-signature: 45027022edc6e784eb1a80f0817e4ba49561f9e90caf3279bea47ce19157e95d" \
  -H "Content-Type: application/json" \
  -d '{"org_id":"f2f4ee17-c04a-47a9-a88a-40eaafd1e03a","amount":1000,"metadata":{"source":"waste-heat-recovery","period":"Q4-2025"}}'
```

**Response:**

```json
{
  "status": "ok",
  "org_id": "f2f4ee17-c04a-47a9-a88a-40eaafd1e03a",
  "delta": 1000
}
```

---

## 🛠 Installation Guide

### 🧩 Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Visit the app locally → [http://localhost:3000](http://localhost:3000)

---

### 🔐 Environment Setup

**.env.local (Frontend)**

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

**ccts/orgs.json Example**

```json
[
  {
    "org_id": "ded8e831-95e5-4751-8a71-ac7fb1a35f2b",
    "name": "GreenCement Pvt Ltd"
  },
  {
    "org_id": "f2f4ee17-c04a-47a9-a88a-40eaafd1e03a",
    "name": "EcoSteel India"
  }
]
```

---

## ⚡ Core Features

| *Feature*                | *Description*                                        |
| ------------------------ | ---------------------------------------------------- |
| 🔥 Real-Time Monitoring  | Tracks heat, power, efficiency, and CO₂ metrics      |
| 🧠 AI-Driven Predictions | Gradient Boosting Regressor for accurate forecasting |
| 🪙 CCTS Integration      | Blockchain-secured carbon credit transactions        |
| ⚙ Model Insights         | R², CV Scores, and Feature Importance visualization  |
| 💬 System Status         | Live operational metrics and health indicators       |
| 🪞 Responsive UI         | Sleek, adaptive, scrollable interface                |

---

## 🚀 Future Roadmap

* 🚀 IoT Sensor Integration for live industrial data
* 🧬 Region-specific Small Language Models (SLMs)
* 🔗 Public Blockchain-based ESG Verification Explorer
* 📊 Sustainability Scoring Dashboard for corporations

---

## 👨‍💻 Team Vibe Mafia

| *Name*             | *Role*                                 | *Responsibility*                                        |
| ------------------ | -------------------------------------- | ------------------------------------------------------- |
| Shaik Uzair Ahmed  | Blockchain & Backend Developer         | Architected backend, AI pipeline, and blockchain system |
| Sayed Nowshad      | Frontend Developer & Blockchain Expert | Built UI & blockchain validation layer                  |
| Manoj Kumar Pendem | AI Engineer                            | Model integration, UI testing, and deployment support   |

---

## 🦯 Mission Statement

“Transforming industrial waste heat into sustainable, verifiable energy —
powered by AI and blockchain, for a greener future.”

---

## 🪙 License

Team Vibe Mafia License © 2025 — HeatX Industrial Energy Intelligence
