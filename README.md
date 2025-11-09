<h1 align="center">🏋️‍♂️ Adaptix</h1>

<p align="center">
  <b>AI-Powered Fitness Tracking Platform</b><br>
  Track workouts, log progress, explore exercises, and get AI-driven insights.<br>
  <i>Modular • Maintainable • Scalable</i>
</p>

---

## 🚀 Overview

**Adaptix** is a full-stack fitness platform designed to help users:
- Track sets, reps, weights, and RPE
- Explore a detailed exercise library with muscle breakdowns
- Build and log personalized workout routines
- Visualize long-term progress through analytics dashboards

Future phases integrate **AI** for personalized training — routine generation, form explanations, and performance insights.

---

## 🧠 Tech Stack

| Layer | Technologies |
|:------|:--------------|
| **Frontend** | [Next.js 15 (App Router)](https://nextjs.org/), [TypeScript](https://www.typescriptlang.org/), [TailwindCSS](https://tailwindcss.com/), [shadcn/ui](https://ui.shadcn.com/), [Recharts](https://recharts.org/) |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/), [Pydantic v2](https://docs.pydantic.dev/latest/), [PostgreSQL](https://www.postgresql.org/), [SQLModel](https://sqlmodel.tiangolo.com/), [JWT Auth](https://jwt.io/) |
| **Infrastructure** | Docker • GitHub Actions (CI/CD) • Vercel • Railway/Fly.io/Render • Neon or Supabase |

---

## 🧩 Architecture

adaptix/
├── backend/
│ ├── auth/
│ ├── exercises/
│ ├── workouts/
│ ├── logging/
│ ├── analytics/
│ └── ai/ # (Future phase)
│
├── frontend/
│ ├── app/
│ ├── components/
│ ├── lib/
│ └── styles/
│
├── docker/
│ ├── Dockerfile.backend
│ ├── Dockerfile.frontend
│ └── docker-compose.yml
│
└── README.md

yaml
Copy code

Each backend module includes:
- `routers.py` → API endpoints  
- `models.py` → ORM models  
- `schemas.py` → Pydantic data validation  
- `services.py` → Business logic  

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/adaptix.git
cd adaptix
2️⃣ Backend Setup
bash
Copy code
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
3️⃣ Frontend Setup
bash
Copy code
cd frontend
npm install
npm run dev
4️⃣ Access the App
Frontend: http://localhost:3000

Backend API: http://localhost:8000/docs

🧪 Testing
Backend (pytest):

bash
Copy code
pytest -v
Frontend (React Testing Library / Playwright):

bash
Copy code
npm run test
📈 Development Roadmap
Phase	Focus	Description
1	Setup	Repo, Docker, CI/CD
2	Auth	JWT login/register, user roles
3	Exercises	Library + filters
4	Routine Builder	Custom templates
5	Logger	Set-by-set progress tracking
6	Analytics	Charts + summaries
7	Polish	UI cleanup, landing page
8	AI	Routine generation, insights
9	Mobile	React Native / Flutter client

🤖 Future AI Features
“Build me a routine for strength or hypertrophy.”

“Explain what muscles this workout hits.”

“Suggest adjustments based on my progression.”

“Identify weak points from my training history.”

These will be powered by custom Python AI services, embeddings, and PGVector for personalized insights.

👥 Team
Role	Member
Lead Developer	Joel
Backend Architecture	FastAPI + Modular Routers
Frontend Development	Next.js + Tailwind
Future Expansion	AI + Mobile Integration

🧾 License
This project is licensed under the MIT License — see LICENSE for details.

<p align="center"> ⭐ <b>Star this repo</b> if you find Adaptix interesting! <br>Follow along as it evolves into a full AI-powered fitness tracker. </p> ```
