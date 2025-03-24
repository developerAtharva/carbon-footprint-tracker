# 🌿 Carbon Footprint Tracker

A **Flask web app** that helps users calculate and track their daily **carbon footprint** based on their lifestyle choices.

## 🚀 Features
- 🔑 **User Authentication** (Signup/Login)
- 🌍 **Carbon Footprint Calculator** (Transport, Electricity, Diet, etc.)
- 📊 **Dashboard** with Personalized Recommendations
- 🎨 **Beautiful UI** with Flask and CSS

## 🌎 Live Demo
🔗 [https://your-app-name.onrender.com](https://your-app-name.onrender.com)

## 🛠️ Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/developerAtharva/carbon-footprint-tracker.git
cd carbon-footprint-tracker
```

### **2️⃣ Create and Activate a Virtual Environment**
- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory and add:
```
SECRET_KEY=your_very_secret_key
```

### **5️⃣ Run the Flask App**
```bash
python app.py
```

### **6️⃣ Open in Browser**
```
http://127.0.0.1:5000
```

---

## 📂 Project Structure
```
carbon-footprint-tracker/
│── static/              # CSS, JS, Images
│── templates/           # HTML Templates
│── app.py               # Flask App
│── models.py            # Database Models
│── forms.py             # Flask Forms
│── routes.py            # Application Routes
│── config.py            # Configuration File
│── requirements.txt     # Dependencies
│── README.md            # Project Documentation
```

---

## 🚀 Deployment Guide
This app is deployed on **Render**. To deploy manually:
1. **Push changes to GitHub**:
   ```bash
   git add .
   git commit -m "Updated app"
   git push origin main
   ```
2. **Go to [Render.com](https://dashboard.render.com/)** → New Web Service
3. **Connect your GitHub repo**
4. **Set Environment Variables** (SECRET_KEY)
5. **Set Start Command**:
   ```bash
   gunicorn app:app
   ```
6. **Click Deploy 🚀**

---

## 📽️ Demo Video
📺 [Watch the demo here](#) *(Upload to YouTube or Google Drive and add the link here)*

---

## 🤝 Contributing
1. Fork the repo
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m "Added new feature"`
4. Push to the branch: `git push origin feature-branch`
5. Create a **Pull Request**

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

🚀 **Built with Flask, CSS, and a passion for sustainability!** 🌍

