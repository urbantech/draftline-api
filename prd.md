# 🛠️ Product Requirements Document (PRD): DraftLine – NIL Management for Cyclists

## 🌟 Product Overview

**DraftLine** is a lightweight NIL (Name, Image, Likeness) management platform built specifically for student and amateur cyclists. It provides end-to-end tooling for managing sponsorships, personal branding, and career planning while offering a public-facing profile and performance integrations.

Targeted for high school, collegiate, and early-career athletes, DraftLine combines NIL income tracking, content planning, sponsor reporting, and athlete discovery pages to bridge the gap between athlete development and professional opportunity.

---

## 👤 Target Personas

### 🧍‍♀️ 1. "Mariah the College Cyclist"

- Age: 21
- Role: Collegiate endurance cyclist
- Goals: Gain gear sponsors, manage content, prep for post-college career
- Pain Points: Lacks marketing skills, overwhelmed with tax/NIL logistics

### 🧍 2. "Ty the Club Team Racer"

- Age: 17
- Role: High school rider in national development circuit
- Goals: Visibility for brand support, wants pro team exposure
- Pain Points: Doesn’t know how to reach brands or track performance value

### 🧍‍♀️ 3. "Jenna the MTB Creator"

- Age: 19
- Role: Downhill/MTB influencer
- Goals: Monetize content, attract non-endemic sponsors
- Pain Points: Needs content planning, analytics, and creator tools

---

## 🧩 Feature Specs

### 🎯 Core Modules

### 1. Deal Manager

- Add/edit NIL deals (brand, deliverables, duration, payment)
- Track deliverables and deadlines
- Document upload and digital contract vault
- Renewal reminders

### 2. Campaign Calendar

- Content planner w/ tagging system for brands
- Auto-reminders for scheduled posts
- Suggested content from AI assistant

### 3. NIL Income + Tax Tracker

- Link payment services (Stripe, Venmo, PayPal)
- Categorize income per sponsor or type
- Exportable tax summaries and write-off recommendations

### 4. Performance Integration

- Strava + Garmin sync
- Visual ride highlights (PRs, race results)
- Sponsor deliverables based on milestone triggers (e.g. 100 mi/month)

### 5. Google Analytics Sync

- OAuth connection to user-owned Google Analytics site (GA4)
- Display user site/pageview traffic in dashboard
- Attribution and link tracking for sponsored content
- Auto-generated sponsor reports

### 6. Public NIL Profile Page

- Custom URL: `draftline.io/{username}`
- Bio, team/school, current sponsors
- Embedded Strava activity + content feed
- Audience + web traffic stats
- Booking CTA: "Send Offer" form w/ smart form builder

### 7. AI NIL Coach

- Suggests new brands, partnership follow-ups, pitch improvements
- Analyzes best times to post based on engagement data
- Helps build 1-pager media kits using performance + engagement data

### 8. Brand Discovery + Booking Portal

- Brand-side interface to search/filter athletes
- View anonymized performance insights
- Create/send NIL offer packages
- CRM-style tracker for past campaigns

---

## 🧱 Technical Stack

### Frontend

- React + Tailwind CSS
- Next.js (for SEO-optimized profile pages)
- TypeScript

### Backend

- FastAPI (Python)
- Supabase (PostgreSQL + Auth)

### Integrations

- **Strava API** – Performance sync
- **Garmin API** – Optional ride data
- **Google Analytics API** – GA4 site traffic & link tracking
- **Stripe, PayPal, Venmo** – NIL payment tracking
- **OpenAI/Ollama** – AI assistant
- **Calendly/Sendgrid** – Optional for scheduling + notifications

---

## 📅 Roadmap

### **Sprint 1: Athlete Onboarding + Deal Tracker**

- Auth system, profile creation, deal logging
- Add/edit/delete deals with deadlines
- Basic dashboard UI

### **Sprint 2: Strava Integration + Performance Dashboard**

- Strava OAuth & ride feed integration
- Performance summary widgets (PRs, milestones)

### **Sprint 3: Campaign Calendar + Content Planner**

- Post scheduler, brand tagging, deadline reminders
- AI post suggestions (MVP version)

### **Sprint 4: NIL Income + Tax Tools**

- Manual payment tracking + categorization
- Exportable tax summary (CSV)
- Income dashboard + sponsor breakdown

### **Sprint 5: Google Analytics Integration**

- OAuth for GA4
- Traffic summary + UTM link tracking
- Attribution reports for brands

### **Sprint 6: Public NIL Profile Pages**

- Dynamic SSR pages via Next.js
- Strava content embeds, content gallery
- Offer contact form

### **Sprint 7: Brand Dashboard + Offer Builder**

- Brand-side UI + athlete discovery filters
- Offer builder + CRM tracker

### **Sprint 8: AI Assistant**

- Suggest NIL outreach, optimize post time
- Build pitch decks/media kits from athlete data

---

## 📊 KPIs

- % athletes with active NIL profiles
- Monthly NIL deals managed
- Sponsor-to-athlete conversion rate
- Avg earnings tracked per athlete
- Daily active athletes + brands
- Feedback/NPS from athletes and sponsors

---

## 🔚 Summary

DraftLine creates a modern NIL experience for cyclists by combining sports performance, personal branding, and business tooling into one integrated platform. With AI features and Google Analytics insight, athletes stay organized while brands get unmatched visibility and tools to engage the next generation of endurance sport talent.

> Optional Future Add-On: Roblox NIL Arena, or career transition tools for athletes with upskilling partners like Coursera or CompTIA.
> 

[📦 **DraftLine Data Model Overview**](https://www.notion.so/DraftLine-Data-Model-Overview-1ffed4666fc38029b461c74a48ebc2ed?pvs=21)

[🏁 1-Day Agile Sprint Plan – **DraftLine MVP Core (Sprint 1)**](https://www.notion.so/1-Day-Agile-Sprint-Plan-DraftLine-MVP-Core-Sprint-1-1ffed4666fc38025b4f0f1002040d29c?pvs=21)

[📚 DraftLine MVP Agile Backlog](https://www.notion.so/DraftLine-MVP-Agile-Backlog-1ffed4666fc380e890fbcf2d72235fbc?pvs=21)

[Backlog JSON](https://www.notion.so/Backlog-JSON-1ffed4666fc380d1bce8d0eaa96d2ea4?pvs=21)

[🌐 DraftLine Frontend PRD – Machine-Readable Specification (MVP)](https://www.notion.so/DraftLine-Frontend-PRD-Machine-Readable-Specification-MVP-1ffed4666fc3809480e3efd3f2a1838f?pvs=21)
