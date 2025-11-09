🏋️‍♂️ Adaptix

AI-Powered Fitness Tracking Platform

Adaptix is a full-stack fitness platform built to help users track workouts, log progress, explore exercises, and receive AI-powered insights.
It’s designed with long-term scalability in mind — modular, maintainable, and ready for mobile + AI integration.

🚀 Features
✅ Core Features

Exercise Library — Search and filter exercises by muscle group, equipment, and difficulty.

Routine Builder — Create, edit, and save custom workout routines.

Workout Logger — Log sets, reps, weights, RPE, and track performance over time.

Progress Dashboard — Visualize training volume, estimated 1RM, and consistency streaks.

🤖 AI-Powered Roadmap

“Build me a routine for ___ goal.”

“Explain what muscles this workout hits.”

“Suggest adjustments based on my progression.”

“Identify weak points from my training history.”

📱 Future Integration

Mobile App (React Native / Flutter) reusing the same FastAPI backend.

AI Coaching Service using vector embeddings and training history for personalized feedback.

🧠 Tech Stack
Frontend

Next.js 15 (App Router)

TypeScript

TailwindCSS

shadcn/ui
 for clean, modern components

Recharts
 for progress graphs

Backend

FastAPI
 — Python backend with modular routers

Pydantic v2
 — Data validation and typing

PostgreSQL
 — Database (via Neon or Supabase)

SQLModel / SQLAlchemy
 — ORM with migrations (Alembic)

JWT Authentication
 — Secure user sessions

Infrastructure

Docker — Consistent local and production environments

GitHub Actions — CI/CD pipelines for testing and deployment

Vercel — Frontend hosting

Railway / Fly.io / Render — Backend deployment

🧩 Architecture Overview
adaptix/
├── backend/
│   ├── auth/
│   ├── exercises/
│   ├── workouts/
│   ├── logging/
│   ├── analytics/
│   └── ai/                # (Future phase)
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── styles/
│
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
│
└── README.md


Each backend module has:

routers.py for endpoints

models.py for ORM models

schemas.py for Pydantic data validation

services.py for business logic

🧰 Setup Instructions
1. Clone the repository
git clone https://github.com/<your-username>/adaptix.git
cd adaptix

2. Backend Setup
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload

3. Frontend Setup
cd frontend
npm install
npm run dev

4. Access

Frontend: http://localhost:3000

Backend API: http://localhost:8000/docs

🧪 Testing

Adaptix uses pytest for backend and Playwright / React Testing Library for frontend.

# Backend
pytest -v

# Frontend
npm run test

🗺️ Development Roadmap
Phase	Focus	Description
1	Setup	Repo, Docker, CI/CD
2	Auth	JWT login/register, user roles
3	Exercise Library	Browse/filter exercises
4	Routine Builder	Save and manage workouts
5	Workout Logger	Track progress and notes
6	Analytics	Volume and performance stats
7	Polish	UI cleanup, landing page
8	AI	Routine generation, insights
9	Mobile	Companion app integration
👥 Team
Role	Member
Lead Developer	Joel
Backend Architecture	FastAPI Module Design
Frontend Development	Next.js + Tailwind
Future Expansion	AI + Mobile Integration
🧾 License

This project is licensed under the MIT License — see LICENSE
 for details.

⭐ Support the Project

If you find Adaptix interesting, consider giving the repo a star ⭐ and following the development roadmap as it evolves toward full AI-powered fitness tracking.
