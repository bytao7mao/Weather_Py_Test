# 🌦️ Weather Automation System — Full Architecture & Service Explanation

Your Weather Automation System uses several services working together to automate fetching weather data and sending you an email report.  
Here is the full breakdown in a **clear, stylish, emoji-rich Markdown format**.

---

# 🧱 1. GitHub — Your Code Source

GitHub is the **central place where your project lives**.

### What GitHub does:
- 🗂️ Stores your Python weather script (`main.py`)
- 🔐 Stores credentials securely (via Jenkins credentials)
- 🔄 Provides Jenkins with repository access
- 🚀 (Optional) Triggers Jenkins via webhook

### **GitHub’s Job**  
📌 *Hold your code and allow Jenkins to download it whenever the pipeline runs.*

---

# ⚙️ 2. Jenkins (Docker) — The Automation Engine

Jenkins is the **heart of your CI/CD pipeline**.

### What Jenkins does:
- 🐳 Runs inside a Docker container  
- 📥 Clones your GitHub repo  
- 🐍 Runs your Python weather script  
- 📧 Sends the weather email  
- 📊 Shows pipeline logs  

### Jenkins Pipeline Steps:
1. 📥 Checkout GitHub repo  
2. 📦 Install dependencies  
3. ▶️ Run Python script  
4. ✉️ Send weather email  

### **Jenkins’ Job**  
📌 *Automate the entire workflow and run it reliably, every time.*

---

# 🌍 3. ngrok — Secure Public Access to Jenkins

Jenkins normally runs at:

```
http://localhost:8080
```

This is **only accessible from your computer**.  
To access Jenkins remotely, you use:

### `ngrok http 8080`

ngrok creates a public URL:

```
https://xxxxx.ngrok-free.app → http://localhost:8080
```

### **ngrok’s Job**  
📌 *Let you access Jenkins from the internet safely, without port forwarding.*

---

# 🐍 4. Python Weather Script — The Core Logic

Your script performs the actual weather work:

### What `main.py` does:
- ☁️ Calls OpenWeather API  
- 🌡️ Retrieves temperature, humidity, pressure, wind  
- 📄 Logs output in Jenkins console  
- ✉️ Sends weather report via Gmail SMTP  

### **Python’s Job**  
📌 *Fetch weather data and send it to your email.*

---

# ☁️ 5. OpenWeather API — Weather Data Provider

Your script calls:

```
api.openweathermap.org/data/2.5/weather?q=BUCHAREST&appid=API_KEY&units=metric
```

The API returns:
- 🌡️ Temperature  
- 💧 Humidity  
- 💨 Wind speed  
- 🌥️ Description  
- 📈 Pressure  

### **OpenWeather’s Job**  
📌 *Provide real-time weather data.*

---

# ✉️ 6. Gmail SMTP — Sends the Email

Your script logs into Gmail using:

- 📧 Your Gmail address  
- 🔑 Gmail App Password  
- 🔐 SSL connection (port 465)

Then sends a weather report email.

### **Gmail’s Job**  
📌 *Deliver your weather notification directly to your inbox.*

---

# 🌐 7. GitHub Pages — Your Documentation Website

You created a documentation site stored in:

```
/docs
```

GitHub Pages hosts it automatically at:

👉 **https://bytao7mao.github.io/Weather_Py_Test/**

### **GitHub Pages’ Job**  
📌 *Present your project documentation using Jekyll and Markdown.*

---

# 🔄 Full System Flow (Emoji Diagram)

```
          🐙 GitHub Repo
                │
           (clone / fetch)
                ▼
   🐳 Jenkins (Docker Container)
                │
          runs pipeline
                ▼
      🐍 Python Weather Script
                │
        🌐 OpenWeather API
                ▼
         📧 Gmail SMTP Server
                │
      sends email notification
                ▼
             📬 Your Inbox

External Access:
You → 🔗 ngrok → Jenkins UI
```

---

# 🎯 Summary — Responsibilities of Each Service

| Service | Role |
|--------|------|
| 🐙 **GitHub** | Stores your code & credentials |
| 🐳 **Jenkins** | Runs pipeline and automates script |
| 🔗 **ngrok** | Exposes Jenkins securely to the internet |
| 🐍 **Python** | Fetches weather + sends email |
| ☁️ **OpenWeather API** | Provides weather data |
| ✉️ **Gmail SMTP** | Sends the email |
| 🌐 **GitHub Pages** | Hosts your documentation site |

---

# 🏁 Final Outcome

You built a production-style CI pipeline that:

✔ Automates weather data collection  
✔ Sends an email every time the pipeline runs  
✔ Uses ngrok for secure public access  
✔ Stores source code in GitHub  
✔ Documents the project using GitHub Pages  
✔ Runs everything inside Docker containers  

This is **full DevOps automation**, and you implemented it end-to-end.
