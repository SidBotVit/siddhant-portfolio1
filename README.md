
# Sidhant Malik — Live Portfolio (Streamlit)

A live, interactive portfolio optimized for interviews — showcasing CS + Electrical projects, timelines, and downloadable resumes (CS + Hyundai/Electrical). Built with **Streamlit**, deployable in minutes.

## ✨ Highlights
- Clean UI with **dark/light toggle**, glassmorphism, smooth hero animation (Lottie)
- **Projects gallery** with filters + search
- **Experience & achievements** sections
- Inline **PDF viewers** + download buttons for both resumes
- Visitor counter (via CountAPI) and basic SEO tags injection
- Mobile friendly and fast to load

## 🚀 One-click Deploy (Streamlit Community Cloud)
1. Push this folder to a new GitHub repo (public).
2. Go to https://streamlit.io/cloud — New App → select your repo.
3. **Main file:** `app.py`  (Python 3.10+).  
4. Add the following **Python packages** automatically from `requirements.txt`.
5. Deploy. Done!

## 🧰 Local Dev
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Structure
```
.
├─ app.py
├─ projects.json
├─ requirements.txt
├─ styles.css
├─ .streamlit/
│  └─ config.toml
└─ assets/
   ├─ Resume_CS_Meta.pdf
   └─ Resume_Electrical_Hyundai.pdf
```

## 🙌 Credits
- Lottie animation courtesy of lottiefiles.com (placeholder link in code; replace if you prefer)
- CountAPI for lightweight visit counter
