# Cancer-Detection


---


# 🩺 Breast Cancer Detection using Logistic Regression

This project builds a **Machine Learning model** to predict whether a tumor is **malignant** or **benign** using the **Breast Cancer Wisconsin Dataset**. It also includes a **Plotly-based interactive dashboard** for data exploration and visual insights.

---

## 📊 Demo Dashboard
> Coming Soon – will be hosted via Streamlit or Dash

---

## 🚀 Project Highlights

- 🔍 **Exploratory Data Analysis (EDA)**  
- 🧪 **Logistic Regression Classifier**
- 📈 **ROC Curve**, **Confusion Matrix**, and **Classification Report**
- 🖼️ **Plotly/Dash Dashboard** for interactive visualization
- 💾 Dataset: [`Breast Cancer Wisconsin (Diagnostic)` on Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)

---

## 📁 Folder Structure

```

Cancer-Detection/
│
├── app.py                   # Plotly Dashboard (Dash App)
├── playground.ipynb        # Colab/EDA Notebook
├── model.pkl               # Trained ML model
├── cancer\_data.csv         # Dataset file
├── requirements.txt        # All dependencies
└── README.md               # Project info

````

---

## 🧠 ML Pipeline

1. **Data Preprocessing**
   - Handling missing values
   - Feature scaling (StandardScaler)
2. **Model Training**
   - Logistic Regression
3. **Evaluation**
   - Accuracy, Confusion Matrix, ROC-AUC
4. **Dashboard**
   - Visualize predictions interactively

---

## 📊 Sample Visuals

- Confusion Matrix with Heatmap  
- ROC Curve  
- Scatter Matrix & Feature Correlations  
- Live Prediction Dashboard

---

## 📦 Requirements

Install all required libraries:
```bash
pip install -r requirements.txt
````

Or manually install:

```bash
pip install pandas scikit-learn matplotlib seaborn plotly dash
```

---

## ▶️ How to Run

### 🔬 Jupyter Notebook (EDA + Model)

```bash
jupyter notebook playground.ipynb
```

### 🌐 Dash App

```bash
python app.py
```

It will start a server on `http://127.0.0.1:8050`.

---

## ✍️ Author

**Siddhant**
📧 \[[YourEmail@example.com](mailto:YourEmail@example.com)]
🔗 [GitHub](https://github.com/siddhant1729)

---

## ⭐ Give a Star

If you like this project, consider ⭐ starring the repo!

```

---

Would you like me to:
- Include the **Streamlit** version?
- Add a **badge section** (like GitHub stars, license, etc.)?
- Generate a `requirements.txt` for you?

Let me know!
```
