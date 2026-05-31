# PROJECT FLOW DOCUMENT

## STEP 1 — Project Initialization

Completed:
- Installed Python
- Installed VS Code
- Installed Git
- Created virtual environment
- Installed required libraries (`pandas`, `numpy`, `yfinance`, `matplotlib`, `scikit-learn`, `joblib`, etc.)
- Initialized GitHub repository
- Created project folder structure (including `data/raw/` and `models/` directories)

## STEP 2 — Data Collection

Completed:
- Defined the target stock ticker (`RELIANCE.NS`).
- Connected to Yahoo Finance API using the `yfinance` library.
- Fetched historical OHLCV (Open, High, Low, Close, Volume) data spanning a 10-year period (2015-01-01 to 2025-01-01).
- Exported the fetched dataset to a local CSV file (`../data/raw/reliance_stock_data.csv`).

## STEP 3 — Data Preprocessing

Completed:
- Reloaded the raw CSV dataset into a Pandas DataFrame.
- Inspected the dataset's shape (2468 rows, 6 columns) and data types.
- Handled missing values (verified 0 nulls across all columns via `.isnull().sum()`).
- Formatted datatypes to ensure appropriate numerical processing for price/volume metrics.
- Generated statistical summaries using `.describe()` to understand distributions and potential outliers.

## STEP 4 — Exploratory Data Analysis (EDA)

Completed:
- Utilized `matplotlib` to visualize raw historical price trends.
- (Notebook implementation pending full feature distribution plots and correlation heatmaps)

## STEP 5 — Feature Engineering

Completed:
- Computed crucial technical indicators based on daily variations:
  - Calculated **Daily Return** percentage.
  - Formulated **Moving Averages** (e.g., 10-day `MA10` and 50-day `MA50`) to capture market momentum.
  - Calculated short-term price variance/volatility.
- Defined the target classification variable `Target` (1 for a positive next-day return, 0 for negative).
- Segregated the engineered dataset into feature vectors (`X`) and the target array (`y`).

## STEP 6 — Machine Learning Model Training

Completed:
- Imported `RandomForestClassifier` from `sklearn.ensemble`.
- Split the dataset chronologically (or via `train_test_split`) into Training and Testing subsets to prevent data leakage.
- Instantiated the Random Forest algorithm with a designated random state.
- Fit the model using the engineered training subset.

## STEP 7 — Model Evaluation

Completed:
- Executed `.predict()` on the unseen test dataset.
- Computed classification metrics (Accuracy, Precision, Recall, F1-Score).
- Extracted and ranked **Feature Importances** (`rf_model.feature_importances_`) to determine which metrics (e.g., MA10, Volatility) drove the model's predictions.

## STEP 8 — Serialization & Prediction System

Completed:
- Imported `joblib` for model persistence.
- Serialized the fully trained Random Forest model.
- Saved the artifact locally to `../models/final_stock_model.pkl` for immediate deployment/inference in the frontend application.

## Next Steps

- Integrate `app.py` frontend (Streamlit) using the exported `.pkl` model.
- Live deployment/cloud hosting.
