# DevPortfolioHub

<p align="center">
  <h1 align="center">DevPortfolioHub</h1>
  <p align="center">
    Modern Software Company Portfolio Platform powered by Django, FastAPI, Docker and AI
  </p>
</p>

---

## 🚀 Overview

DevPortfolioHub is an open-source portfolio platform designed for software companies to showcase their services, technical capabilities, development expertise, team members, and previous projects.

Unlike traditional portfolio websites, this platform combines a production-ready Django application with a dedicated AI microservice, modern frontend technologies, optimized database access patterns, and containerized deployment.

---

## ✨ Features

### Company Presentation

* Company introduction
* Services showcase
* Team profiles
* Project portfolio
* Lead generation forms
* Technology stack presentation

### Portfolio Management

* Dynamic project pages
* SEO-friendly URLs
* Unicode slug support
* Technology categorization
* Service categorization

### Team Showcase

* Team member profiles
* Skills management
* Interactive modals
* Dynamic frontend interactions

### AI Summarization Service

* FastAPI-powered API
* Hugging Face Transformers integration
* Asynchronous request handling
* Text summarization endpoint

---

# 🏗 Architecture

The platform uses a containerized architecture based on Docker Compose.

```text
                    ┌───────────────┐
                    │    Browser    │
                    └───────┬───────┘
                            │
                            ▼
                  ┌─────────────────┐
                  │      Nginx      │
                  │ Reverse Proxy   │
                  └───────┬─────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
 ┌─────────────────┐           ┌─────────────────┐
 │ Django +        │           │ FastAPI         │
 │ Gunicorn        │           │ Summarizer API  │
 │ Port 8000       │           │ Port 8001       │
 └────────┬────────┘           └─────────────────┘
          │
          ▼
 ┌─────────────────┐
 │ SQLite Database │
 └─────────────────┘
```

---

# 🔄 Reverse Proxy Layer

Nginx acts as the single entry point and intelligently routes requests.

### Django Application

```nginx
location / {
    proxy_pass http://django_app:8000;
}
```

Handles:

* Landing pages
* Portfolio pages
* Team pages
* Contact forms
* Project details

### AI Service

```nginx
location /api/summarize/ {
    proxy_pass http://summarizer_app:8001/summarize/;
}
```

Handles:

* Text summarization requests
* AI inference operations

### Static & Media Files

Static and uploaded media files are served directly by Nginx.

```nginx
location /static/ {
    alias /app/staticfiles/;
}

location /media/ {
    alias /app/media/;
}
```

Benefits:

* Faster delivery
* Reduced Django workload
* Better scalability

---

# ⚙ Backend Architecture

The core application is built with Django 5.

## Installed Applications

```text
apps/
│
├── core
├── portfolio
├── team
└── lab
```

### Responsibilities

| App       | Responsibility                      |
| --------- | ----------------------------------- |
| core      | Shared functionality                |
| portfolio | Projects, technologies and services |
| team      | Team management                     |
| lab       | Experimental features               |

---

# 🗄 Database Layer

Current implementation uses SQLite.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

The architecture is designed to allow migration to PostgreSQL in production environments with minimal configuration changes.

---

# 🚀 ORM Optimization

Database queries are optimized using Django ORM best practices.

### select_related()

Used for ForeignKey relationships.

```python
Project.objects.select_related("category")
```

### prefetch_related()

Used for ManyToMany relationships.

```python
TeamMember.objects.prefetch_related("skills")
```

Benefits:

* Prevents N+1 query issues
* Reduces database round trips
* Improves page rendering speed

---

# 🔗 SEO Friendly Routing

Projects use slug-based URLs.

Example:

```text
/projects/custom-crm-platform/
```

Unicode slugs are supported through regex routing.

```python
re_path(
    r"^projects/(?P<slug>[-\w\u0600-\u06FF]+)/$",
    views.project_detail
)
```

This enables:

* Persian URLs
* SEO optimization
* Human-readable routes

---

# 🤖 AI Summarization Service

A dedicated FastAPI application handles NLP workloads separately from Django.

## Technology Stack

* FastAPI
* Pydantic
* Hugging Face Transformers
* DistilBART

Model:

```text
sshleifer/distilbart-cnn-12-6
```

---

## Asynchronous API

```python
@app.post("/summarize")
async def summarize(data: SummaryRequest):
    ...
```

Benefits:

* High concurrency
* Non-blocking execution
* Better throughput

---

## Request Validation

Pydantic validates incoming requests.

```python
class SummaryRequest(BaseModel):
    text: str
```

This prevents:

* Invalid payloads
* Malformed requests
* Runtime failures

---

# 🐳 Docker Infrastructure

The entire platform is containerized.

Services:

```yaml
services:
  django_app:
  summarizer_app:
  nginx:
```

---

## Multi-Stage Build

Frontend assets are built using Node.js and copied into the final Python image.

### Stage 1

```dockerfile
FROM node:20-alpine AS frontend-builder
```

Responsibilities:

* Install npm dependencies
* Compile TailwindCSS
* Build frontend assets

### Stage 2

```dockerfile
FROM python:3.11-slim
```

Responsibilities:

* Install backend dependencies
* Collect static files
* Run Gunicorn

Benefits:

* Smaller production images
* Faster deployment
* Better layer caching

---

# 🧠 AI Model Preloading

To eliminate cold-start delays, the summarization model is downloaded during image build.

```dockerfile
RUN python download_model.py
```

Advantages:

* Faster startup
* Predictable deployments
* Reduced runtime initialization

---

# 🎨 Frontend Architecture

The frontend follows a hybrid SSR approach.

### Server-Side Rendering

Provided by Django Templates.

Benefits:

* Better SEO
* Faster initial page load
* Accessibility improvements

---

## Tailwind CSS

The project uses:

* Tailwind CSS
* PostCSS
* Custom Design Tokens

Example:

```html
<div class="flex items-center gap-4">
```

Benefits:

* Utility-first styling
* Smaller bundles
* Rapid development

---

## Alpine.js

Lightweight reactivity layer.

Used for:

* Team member modals
* Interactive UI components
* Client-side state management

Example:

```html
<div x-data="{ open: false }">
```

Advantages:

* Tiny footprint
* No SPA complexity
* Seamless Django integration

---

# 🌐 Interactive 3D Hero Section

The homepage includes a Three.js-powered hero section.

Technologies:

* Three.js
* WebGL
* Vertex Shaders
* Fragment Shaders
* Noise Functions

Features:

* Real-time rendering
* Interactive mouse response
* GPU acceleration
* Dynamic animations

---

# 🛠 Technology Stack

## Backend

* Django 5
* Gunicorn
* FastAPI
* Pydantic

## Database

* SQLite

## Frontend

* Tailwind CSS
* Alpine.js
* Three.js
* PostCSS

## Infrastructure

* Docker
* Docker Compose
* Nginx

## AI

* Hugging Face Transformers
* DistilBART
* PyTorch

---

# 🚀 Local Development

Clone the repository:

```bash
git clone https://github.com/amirhd4/Dev-Portfolio-Hub.git
cd Dev-Portfolio-Hub
```

Start all services:

```bash
docker compose up --build
```

Detached mode:

```bash
docker compose up -d --build
```

Stop services:

```bash
docker compose down
```

---

# 📡 Available Endpoints

| Service        | URL                                  |
| -------------- | ------------------------------------ |
| Website        | http://localhost:8087                |
| Admin Panel    | http://localhost:8087/admin          |
| Summarizer API | http://localhost:8087/api/summarize/ |

---

# 📈 Performance Highlights

* Reverse Proxy Architecture
* Dedicated AI Service
* ORM Query Optimization
* Static File Offloading
* Multi-Stage Docker Builds
* AI Model Preloading
* Lightweight Frontend Stack
* Async FastAPI Processing

---

# 📄 License

Released under the MIT License.

Open-source, extensible, and production-ready.
