# 📦 **DraftLine Data Model Overview**

Here is a detailed **relational data model** for the DraftLine NIL Management Platform, designed for a PostgreSQL-compatible backend (e.g., Supabase):

---

### 🗂️ Key Entities:

- `users` – athlete or brand accounts
- `athlete_profiles` – extended data specific to athletes
- `brand_profiles` – extended data specific to brands
- `nil_deals` – active or past sponsorship deals
- `deliverables` – posts or tasks tied to deals
- `payments` – income entries from NIL deals
- `activities` – synced cycling performance data (Strava/Garmin)
- `analytics` – Google Analytics stats for athlete pages
- `public_pages` – public profile metadata + CTA tracking
- `media_kits` – AI-generated pitch decks
- `utm_links` – trackable links for campaign attribution
- `ai_suggestions` – content or partner suggestions from AI

---

## 📘 Entity Definitions

### `users`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Unique user ID |
| email | VARCHAR | Auth email |
| role | ENUM | 'athlete' | 'brand' | 'admin' |
| password_hash | TEXT | (if not using SSO) |
| created_at | TIMESTAMP | Account creation time |
| last_login | TIMESTAMP | Last activity |

---

### `athlete_profiles`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK, FK → users.id) | Matches user |
| full_name | VARCHAR | Athlete name |
| bio | TEXT | Personal description |
| school | VARCHAR | College or club name |
| sport_type | ENUM | 'road' | 'mtb' | 'gravel' etc. |
| strava_id | VARCHAR | External ID |
| garmin_id | VARCHAR | Optional |
| site_url | TEXT | Personal blog or NIL page |
| google_analytics_id | TEXT | GA4 property ID |

---

### `brand_profiles`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK, FK → users.id) | Matches user |
| brand_name | VARCHAR | Company or sponsor name |
| website | TEXT | Brand website |
| industry | VARCHAR | Apparel, Nutrition, etc. |

---

### `nil_deals`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Deal ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| brand_id | UUID (FK) | FK → brand_profiles.id |
| title | VARCHAR | Deal name |
| start_date | DATE | Contract start |
| end_date | DATE | Contract end |
| payment_total | NUMERIC | Expected payment |
| status | ENUM | 'active' | 'completed' | 'cancelled' |
| contract_url | TEXT | Signed PDF or file location |

---

### `deliverables`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Deliverable ID |
| deal_id | UUID (FK) | FK → nil_deals.id |
| type | ENUM | 'post' | 'story' | 'video' | 'event' |
| due_date | DATE | Deadline |
| status | ENUM | 'pending' | 'complete' | 'overdue' |
| link | TEXT | URL to content if available |
| caption | TEXT | Required text for post |

---

### `payments`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Payment ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| brand_id | UUID (FK) | FK → brand_profiles.id |
| deal_id | UUID (FK) | Optional link to deal |
| method | ENUM | 'paypal' | 'venmo' | 'stripe' | 'other' |
| amount | NUMERIC | Amount received |
| payment_date | DATE | Date of transaction |
| category | VARCHAR | Optional (bonus, base, gift, etc.) |

---

### `activities`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Activity ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| strava_id | TEXT | External activity ID |
| distance_km | FLOAT | Ride distance |
| elevation_m | FLOAT | Elevation gain |
| duration_min | FLOAT | Total time |
| ride_type | ENUM | 'race' | 'training' | 'commute' |
| ride_date | TIMESTAMP | Date of activity |

---

### `analytics`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Entry ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| pageviews | INT | Total pageviews from GA |
| bounce_rate | FLOAT | % bounce rate |
| session_duration | FLOAT | Avg session duration (seconds) |
| timestamp | TIMESTAMP | Recorded date/time |

---

### `public_pages`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Page ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| slug | VARCHAR | Custom path for public profile |
| views | INT | View counter |
| inquiries | INT | Total booking CTA submissions |
| last_updated | TIMESTAMP | Cache/SEO metadata |

---

### `utm_links`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Tracking ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| campaign_name | VARCHAR | UTM source |
| link | TEXT | Full destination URL |
| clicks | INT | Tracked clicks |
| conversions | INT | Tracked conversion actions |

---

### `media_kits`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Kit ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| generated_on | TIMESTAMP | Date created |
| download_url | TEXT | PDF or hosted version of media kit |
| views | INT | Viewed by brands |

---

### `ai_suggestions`

| Field | Type | Description |
| --- | --- | --- |
| id | UUID (PK) | Suggestion ID |
| athlete_id | UUID (FK) | FK → athlete_profiles.id |
| suggestion_type | ENUM | 'content' | 'brand' | 'post_timing' |
| value | TEXT | Suggestion body |
| status | ENUM | 'new' | 'dismissed' | 'applied' |
| created_at | TIMESTAMP | Timestamp |

---

## 🧠 Notes on Extensions

- All date/time fields are stored in UTC with user-local time support at the UI layer.
- This schema is built for **Supabase** (PostgreSQL) but works with any SQL backend.
- Consider implementing **Row-Level Security (RLS)** to isolate user/brand data.
