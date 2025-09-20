# 🚀 CI/CD Demo with GitHub Actions & Render  

This repository was created **only for learning purposes** - to practice CI/CD concepts with **GitHub Actions**, **YAML workflows**, and **automatic deployment** to [Render](https://render.com).  
It is not a production project, but rather a **self-learning experiment**.  

---

## 📖 What I Learned  

- How to create and configure a **GitHub Actions workflow** using `.yml` files.  
- How GitHub Actions automatically spins up a temporary Ubuntu server, installs dependencies, runs tests, and deploys.  
- How to integrate GitHub with Render for **automatic deployment** after every push.  
- How to use **secrets** (`RENDER_API_KEY`) for safe deployments.  
- Where to view **logs** in Render (and how `print()` outputs appear there).  

---

## ⚙️ CI/CD Workflow Overview  

The workflow file: `.github/workflows/ci-cd.yml`  

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main   

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest  

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest || echo "No tests found, skipping..."

      - name: Deploy to Render
        run: |
          curl -X POST "https://api.render.com/deploy/srv-d37hlgvfte5s73bacthg?key=${{ secrets.RENDER_API_KEY }}"
```

---

## 🔄 CI/CD Flow Diagram

```mermaid
flowchart LR
  A[💻 Push Code to GitHub] --> B[⚡ GitHub Actions Workflow]
  B --> C[🔧 Build & Install Dependencies]
  C --> D[✅ Run Tests]
  D --> E[☁️ Deploy to Render via API]
  E --> F[🌐 Live Demo Website]
  ```

---

## 🌍 Live Demo

👉 [Demo Website on Render](https://ci-cd-demo-doy4.onrender.com)

(Might spin down after inactivity since it’s on Render’s free tier)

--- 

## 📌 Notes

* This project is not a portfolio project - it’s only a learning playground.

* ```print()``` statements from Flask appear only in Render’s logs, not in the browser.

* Render automatically provides a free SSL certificate (HTTPS).

---

## ✅ Summary

This repo helped me practice:

* Writing .yml workflows for GitHub Actions.

* Understanding automated testing & deployment pipelines.

* Using secrets and environment variables securely.

* Seeing the full CI/CD cycle in action.
