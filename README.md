# 🌦️ Weather Automation Pipeline  
### ✨ Fully Automated Weather Report Emailer Using Jenkins, Python, Docker & Nginx (Infrastructure)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Jenkins](https://img.shields.io/badge/Jenkins-Pipeline-red.svg)
![Docker](https://img.shields.io/badge/Docker-Container-blue.svg)
![Nginx](https://img.shields.io/badge/Nginx-Reverse_Proxy-green.svg)
![GitHub](https://img.shields.io/badge/GitHub-Private_Repo-black.svg)
![Security](https://img.shields.io/badge/Secure-Secrets%20via%20Jenkins%20Credentials-green)
![Status](https://img.shields.io/badge/Build-Success-brightgreen)

</div>

---

# 🌐 Project Logo

```
 __        __   _                            _             
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___       
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \     
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |    
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/     

Weather CI Automation Pipeline
```

---

# 📊 CI/CD Pipeline Diagram

```
┌────────────────┐      ┌───────────────────┐      ┌──────────────────────────┐
│ Private GitHub │ ---> │ Jenkins Pipeline  │ ---> │ Python Weather Script    │
│ Repository     │      │ (Docker Container)│      │ (API + Email Sender)     │
└────────────────┘      └───────────────────┘      └──────────────────────────┘
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │ Gmail SMTP Delivery │
                      └─────────────────────┘
```

---

# 📄 GitHub Pages Documentation

A full GitHub Pages site can be hosted at:

```
https://<your-github-username>.github.io/<repository-name>/
```

To set up GitHub Pages:

1. Go to **Repo → Settings → Pages**
2. Select branch: `master` or `main`
3. Select folder: `/docs`
4. Click **Save**

You can create a `docs/` folder and include additional documentation:
- `docs/index.md`
- `docs/architecture.md`
- `docs/pipeline.md`

---

# 📌 Overview

This project automates real-time weather retrieval and sends email updates using **Jenkins CI**, **Python**, **Gmail App Password**, and a **private GitHub repository**.  
All sensitive secrets are securely managed using **Jenkins Credentials**, never in source code.

---

# 🚀 Features

- Automated weather email alerts  
- Secure secret handling (API keys, Gmail passwords)  
- Jenkins running inside Docker  
- Optional Nginx reverse proxy for external exposure  
- Private GitHub integration using PAT  
- Production-grade environment variable secret injection  
- Scripted email delivery using Gmail App Passwords  

---

# 🧱 Tech Stack

| Component | Purpose |
|----------|---------|
| **Python 3.13** | Weather script logic |
| **Jenkins Pipeline** | Automation workflow |
| **Docker** | Containerized Jenkins |
| **Nginx (optional)** | Reverse proxy for Jenkins |
| **OpenWeather API** | Weather data |
| **Gmail SMTP** | Email delivery |
| **GitHub Private Repo** | Code storage |
| **Jenkins Credentials** | Secret management |

---

# 🔐 Security Model

- No secrets stored in GitHub  
- Secrets injected at runtime via Jenkins environment variables  
- Gmail App Password used for secure SMTP login  
- OpenWeather API key hidden from codebase  

Environment variables used:

```
WEATHER_API_KEY
GMAIL_USERNAME
gmailAppPassword
```

---

# 📬 Email Example

Delivered message:

```
Subject: Weather news from tao!
Body:
In BUCHAREST the weather is 5°C with clear sky.
```

---

# 📂 Project Structure

```
Weather_Py_Test/
│
├── main.py
├── README.md
└── (Jenkins-managed folders)
```

---

# 📈 Example Jenkins Output

```
Temperature: 5 °C
Wind: 1.54
Pressure: 1017
Humidity: 78
Description: clear sky
Email sent!
Finished: SUCCESS
```

---

# 💬 Author

**Marius Nicolae**  
Automated CI Weather Pipeline

LinkedIn: https://www.linkedin.com/in/nicolae-marius-37b344144/
Testing text
