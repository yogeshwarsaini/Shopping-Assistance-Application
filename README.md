# 🛍 AI Shopping Assistant

An AI-powered shopping assistant built with **Python**, **Streamlit**, and **Google Gemini API**.  
This project allows users to interact with an AI model for product recommendations, price queries, and smart shopping assistance.

---

## 🚀 Features
- 💬 Chat with an AI shopping assistant in real time.
- 🔑 Secure integration with **Google Gemini API**.
- 🖼️ Product visualization with images.
- ⚡ Fast, lightweight, and easy to run locally.

---

## 📂 Project Structure
```
AI-Shopping-App/
│── app.py              # Main Streamlit application
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── /images             # Store product / demo images
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Shopping-App.git
cd AI-Shopping-App
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API Key
- Get your **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/).  
- Add it as environment variable:
  ```bash
  export GOOGLE_API_KEY="your_api_key_here"     # Linux/Mac
  set GOOGLE_API_KEY="your_api_key_here"        # Windows PowerShell
  ```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🎮 Usage
- Open the app in your browser (default: `http://localhost:8501`).
- Paste your **Gemini API Key** in the sidebar.
- Start chatting with the AI shopping assistant.
- Explore products and recommendations interactively.

---

## 📸 Screenshots
_Add screenshots of your app here_  

![Screenshot](images/demo.png)

---

## 🤝 Contributing
1. Fork the repo  
2. Create your feature branch (`git checkout -b feature-branch`)  
3. Commit changes (`git commit -m 'Add new feature'`)  
4. Push to branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author
**Yogeshwar Saini**  
📧 [your_email@example.com](mailto:your_email@example.com)  
🌐 [LinkedIn Profile](https://www.linkedin.com/)
