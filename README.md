

# ⚡ NeuralTrade: AI-Powered Stock Market Prediction
**Predicting next-day stock price trends using advanced Machine Learning, Technical Indicators & Macroeconomic Data.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![XGBoost](https://img.shields.io/badge/XGBoost-171515.svg?style=flat&logo=xgboost&logoColor=white)](https://xgboost.ai/)
[![Pandas](https://img.shields.io/badge/Pandas-150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)



</div>

---

## 🎯 Project Objective
**NeuralTrade** is a Python-driven AI platform engineered to forecast next-day stock price trends. This project aims to build a machine learning model that predicts stock market trends using historical stock market data along with educational and economic indicators. By reducing the technological asymmetry between institutional and retail investors, it provides a structured, data-driven probability estimate for market direction.

---

## ✨ Interactive Dashboard
The prediction system is deployed via a web application built on Streamlit. It replicates the look and feel of professional trading terminals, featuring a premium dark financial aesthetic, a live market ticker, and interactive Plotly donut charts to visualize ensemble confidence.

<!-- <div align="center">
  <img src="https://images.unsplash.com/photo-1642543492481-44e81e391452?q=80&w=2070&auto=format&fit=crop" width="48%" alt="Trading Dashboard" style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
  <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop" width="48%" alt="Data Analytics" style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
</div> -->

---

## 🧠 Machine Learning Models Explained
To ensure absolute predictive rigor, this project evaluated six different machine learning classifiers using a comprehensive 19-point feature vector. Here is a breakdown of every model tested on the held-out test set of 1,000 records:

| Algorithm | Accuracy | F1-Score | Model Explanation & Performance |
| :--- | :---: | :---: | :--- |
| 🏆 **XGBoost** | **89.2%** | **89.3%** | **The Deployed Champion.** XGBoost builds deep trees that carve the feature space into complex decision regions and corrects its errors sequentially. It achieved the highest accuracy by effectively capturing non-linear interactions among momentum signals, volatility estimates, and macroeconomic variables. |
| 🚀 **CatBoost** | **88.6%** | **88.6%** | A highly competitive gradient boosting algorithm. It uses ordered boosting to break the circular information flow (target leakage) during training, which is particularly valuable when data has a natural temporal order like daily stock records. |
| ⚡ **LightGBM** | **88.1%** | **88.0%** | Designed for training speed at scale, LightGBM swaps level-wise tree growth for a leaf-wise approach. It approximates data distribution using histograms, making it exceptionally fast for large financial datasets. |
| 🌳 **Random Forest** | **87.4%** | **87.5%** | A classical ensemble method that builds a large forest of independent decision trees and aggregates their votes. While it performs solidly, it is structurally outpaced by the sequential error-correction of gradient boosting methods. |
| 🌲 **Decision Tree** | **79.3%** | **79.1%** | A foundational algorithm that splits data based on feature thresholds. While highly interpretable, single trees are notoriously unstable and prone to high variance on noisy equity data. |
| 📐 **Logistic Regression** | **74.6%** | **74.5%** | The baseline model. Because it is constrained to a linear decision surface, it fundamentally underperforms, proving that equity market direction is driven by multiplicative variables that do not combine linearly. |

---

## 🔬 Dataset Sources & Feature Engineering

### 🌐 Data Sources
* **Yahoo Finance**
* **World Bank Open Data**
* **Reserve Bank of India (RBI)**
* **Kaggle**

### ⚙️ The 19-Point Feature Vector
The models were trained on a highly curated dataset integrating four critical domains:
1.  **Daily Price and Volume:** Intraday minimum/maximums, opening/closing prices, and total shares traded.
2.  **Technical Moving Averages:** 10-day and 50-day simple moving averages to capture short and medium-term trend regimes.
3.  **Short-Term Momentum:** Directional conviction of buyers/sellers and rolling standard deviation of recent daily returns.
4.  **Macroeconomic Variables:** India's annualized GDP growth rate, Consumer Price Index inflation rate, national unemployment percentage, adult literacy rate, and government education expenditure. 

---

## 🛠️ Project Modules
The project follows a rigorous CRISP-DM framework, executed through the following modules:
1.  **Data Collection:** Gathering OHLCV and macroeconomic inputs.
2.  **Data Preprocessing:** Missing value handling, scaling with `StandardScaler`, and stratified train-test splitting.
3.  **Exploratory Data Analysis (EDA):** Overlaying moving averages and analyzing price distribution histograms.
4.  **Feature Engineering:** Constructing the 19-element vector and computing derived features.
5.  **Machine Learning Model Training:** 5-fold cross-validated `GridSearchCV`.
6.  **Model Evaluation:** Competitive benchmarking across Accuracy, Precision, Recall, and F1-Scores.
7.  **Prediction System:** Deploying the serialized XGBoost artifact (`final_stock_model.pkl`).
8.  **Deployment:** Interactive web application powered by Streamlit.

---

## 💻 Technologies Used
* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **TensorFlow**
* **Matplotlib & Seaborn**
* **Jupyter Notebook**
* **Streamlit & Plotly**

---

## 👤 Author
**Mugdha Hazra**

