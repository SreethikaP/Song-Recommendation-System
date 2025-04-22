# 🎵 Spotify Song Recommendation System

An AI-powered system that recommends similar songs based on Spotify audio features using KMeans Clustering.

🚀 **Live Demo**: (Coming Soon After Deployment)

---

## 📚 Project Description

This project clusters Spotify tracks based on audio features like danceability, energy, valence, etc., and recommends similar tracks to users. Built with end-to-end MLOps practices including:

- Data Ingestion
- Feature Scaling
- Model Training and Experiment Tracking (MLflow)
- Recommendation Engine
- Streamlit Frontend App
- Deployment to Hugging Face Spaces
- CI/CD Pipeline (GitHub Actions)

---

## 🛠 Technologies Used
- **Python**
- **Pandas, NumPy, Scikit-learn**
- **MLflow** (Experiment Tracking)
- **Streamlit** (Frontend App)
- **Hugging Face Spaces** (Deployment)
- **GitHub Actions** (CI/CD)

---

## 📂 Project Structure
song-recommendation-system/
│── config/                       # Configuration files
│── src/
│   ├── pipeline/                  # Data ingestion, preprocessing, training
│   ├── components/                 # Model components
│   ├── utils/                       # Helper functions
│   ├── data/                        # Training datasets
│   ├── models/                      # Trained models
│   ├── mlruns/                      # MLflow experiment tracking
│── .github/workflows/deploy.yml     # CI/CD for auto deployment
│── requirements.txt                 # Required Python packages
│── app.py                           # Streamlit app
│── README.md                        # Project Documentation
---

## 🚀 How to Run Locally

1. Clone the Repository:
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Start MLflow Tracking Server:
```bash
mlflow ui
```

4. Train Model:
```bash
python src/pipeline/training_pipeline.py
```
5. Run Streamlit App:
```bash
streamlit run app.py
```


