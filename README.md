# 🔍 Port & Service Enumeration Tool

A lightweight, full-stack network utility that scans specified ports on a target IP or domain, detects open/closed status, and retrieves service banners. Built with a **Flask backend** and a **responsive HTML/JS frontend**, this tool is ideal for learning and demonstrating core cybersecurity and networking concepts.

---

## 🚀 Features

- ✅ TCP port scanning using Python sockets
- ✅ Banner grabbing for HTTP services (`GET /` probing)
- ✅ Dynamic frontend with real-time results
- ✅ CORS-enabled Flask API for smooth integration
- ✅ Color-coded status indicators (Open with banner, Open without banner, Closed)

---

## 🧠 Technologies Used

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask, Flask-CORS  
- **Networking:** `socket`, `connect_ex`, `recv`, HTTP probing

---

## 📸 Sample Output

| Port | Status | Banner |
|------|--------|--------|
| 5000 | OPEN   | Werkzeug/3.1.3 Python/3.12.6 |
| 21   | CLOSED | None |
| 8080 | OPEN   | SimpleHTTP/0.6 Python/3.12.6 |

---
