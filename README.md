# 📸 WhatsApp Shift Reporting Automation

A Python automation tool that captures screenshots from a live web-based dashboard (e.g., PUXING system) and automatically sends them to a WhatsApp group or individual at scheduled times via WhatsApp Web.

---

## 🔧 Features

- ✅ Scheduled screenshot capture from a specific application or browser tab
- ✅ Image upload and captioned message via WhatsApp Web
- ✅ Fully automated with no user input after initial setup
- ✅ Customizable group name, caption, and schedule time
- ✅ Supports manual tab selection or fixed click positions

---

## 🖥️ Tech Stack

| Component       | Description                                   |
|----------------|-----------------------------------------------|
| **Python**      | Main programming language                     |
| `pyautogui`     | GUI automation (mouse clicks, typing, etc.)   |
| `pygetwindow`   | Focus and manipulate window applications      |
| `schedule`      | Schedule tasks at specific times              |
| `webbrowser`    | Open WhatsApp Web in default browser          |
| `datetime`, `os`| Standard libraries for file/time operations   |

---

## 📝 Prerequisites

Install the required libraries:

```bash
pip install pyautogui pygetwindow schedule
