# 🏁 1-Day Agile Sprint Plan – **DraftLine MVP Core (Sprint 1)**

**Sprint Theme:** 🚴 Athlete Onboarding + NIL Deal Tracker

---

### 🎯 **Sprint Goal**

Launch the core MVP flow: athletes can sign up, create a profile, and track their NIL deals and deliverables.

---

### 📦 **Scope of Sprint 1 (MVP Slice)**

| Feature | Description |
| --- | --- |
| 🧑‍💼 User Registration/Login | Sign up, sign in via email/password or Supabase Auth |
| 🧾 Athlete Profile Creation | Name, school, bio, sport type, avatar |
| 🤝 NIL Deal Creation | Create/edit NIL deals (title, brand, value, dates) |
| 📋 Deliverables Tracking | Add deliverables tied to deals (type, due date, status) |
| 🧮 Deal Dashboard | Table view of active deals + deliverables with simple status filters |

---

### 🛠️ **Tasks Breakdown by Role**

### 👨‍💻 Backend Engineer

| Task ID | Task Description | Est. Time |
| --- | --- | --- |
| BE1 | Set up FastAPI project with Supabase Postgres | 1h |
| BE2 | Create user + athlete profile models (CRUD APIs) | 1h |
| BE3 | Build `nil_deals` and `deliverables` models + routes | 1.5h |
| BE4 | Implement auth middleware + role protection | 1h |
| BE5 | Write unit tests for deal API endpoints | 1h |

---

### 🧑‍🎨 Frontend Engineer

| Task ID | Task Description | Est. Time |
| --- | --- | --- |
| FE1 | Set up React project with Tailwind + Auth context | 1h |
| FE2 | Build signup/login forms | 1h |
| FE3 | Create profile setup UI for athlete info | 1h |
| FE4 | Build deal creation/edit form | 1.5h |
| FE5 | Dashboard: list deals + deliverables (status icons) | 2h |
| FE6 | Toasts + error/success feedback | 0.5h |

---

### 🧪 QA/Tester (or Dev role with TDD)

| Task ID | Task Description | Est. Time |
| --- | --- | --- |
| QA1 | Manual test flows: signup → profile → add deal | 0.5h |
| QA2 | Test form validation (required fields, invalid data) | 0.5h |
| QA3 | Check RLS/auth boundaries per user | 0.5h |
| QA4 | Cross-browser test basic flows | 0.5h |

---

### 🧠 Product/UX (Optional Roles)

| Task ID | Task Description | Est. Time |
| --- | --- | --- |
| UX1 | Define profile field labels & guidance | 0.5h |
| UX2 | Approve copy for dashboard, deal form | 0.5h |

---

### 🧭 Sprint Timeline (Total: 8–10 hrs)

| Time Slot | Activity |
| --- | --- |
| **9:00 AM – 9:30** | Sprint Kickoff + Task Assignment |
| **9:30 – 12:00** | Parallel Dev: Backend + Frontend Setup |
| **12:00 – 1:00** | Lunch + Integration Checkpoint |
| **1:00 – 3:30** | Complete UI + API flows, connect DB + UI |
| **3:30 – 4:30** | Testing: manual, unit, integration |
| **4:30 – 5:00** | Internal Demo + Bug Fixes |
| **5:00 – 5:30** | Retro + Planning for Day 2 (Strava + Calendar) |

---

### ✅ Sprint Deliverables

- ✅ Authenticated athlete user flow
- ✅ Athlete profile creation
- ✅ NIL deal + deliverables UI
- ✅ MVP dashboard with deal tracking
- ✅ Unit tests + manual QA pass

---

### 📈 Success Criteria

- 100% pass on deal creation/test flow
- <500ms API latency for dashboard endpoints
- Zero auth leaks (test with multiple athlete accounts)
