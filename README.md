# 🔐 Phishing Website Detection Tool

A real-time phishing URL detection tool built in Python using a GUI interface. This tool helps users identify suspicious or malicious URLs to avoid phishing scams.

---

## 🎯 Objective

Detect phishing websites using rule-based logic such as:

- URL structure validation 
- DNS resolution check 
- HTTP/HTTPS status 
- SSL certificate validation 

---

## ✨ Features

- ✅ Real-time phishing detection
- 📡 DNS & protocol checks
- 🔒 SSL certificate validation
- 🌓 Dark/Light theme toggle
- 🎨 Stylish Tkinter-based GUI

---

## 📁 Folder Structure

phishing-detector/
├── assets/                 # Folder containing background image
│   └── bg.png
├── phishing_gui_app.py     # Main GUI application file
├── url_checker.py          # URL analysis wrapper
├── utils.py                # Utility functions
├── requirements.txt        # Dependencies list
├── README.md               # Project documentation
└── .gitignore              # Files to exclude from Git


---

## ⚙️ Setup Instructions

### 🔽 1. Clone the Repository

\`\`\`bash
git clone https://github.com/your-username/phishing-detector.git
cd phishing-detector
\`\`\`

> Replace \`your-username\` with your actual GitHub username.

---

### 🧪 2. Create a Virtual Environment (Optional but Recommended)

\`\`\`bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

---

### 📦 3. Install Required Packages

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

### 🚀 4. Run the Application

\`\`\`bash
python3 phishing_gui_app.py
\`\`\`

---

## 🧰 Technologies Used

- **Python 3**
- **Tkinter** – GUI library
- **Regex, socket, ssl, http.client** – Backend logic
- **Pillow** – For image handling in GUI

---

## 📌 Requirements (from \`requirements.txt\`)

\`\`\`
Pillow
\`\`\`

> Add more if your project grows (e.g., scikit-learn for ML in the future).


This project is intended for educational use only.
Use responsibly and never to harm or deceive others.
