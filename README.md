# ✈️ Jet Engine RUL Prediction (Predictive Maintenance)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://om-engine-predictor.streamlit.app/)

## 📌 Overview
This project predicts the **Remaining Useful Life (RUL)** of turbojet engines using sensor data from the NASA CMAPSS dataset. By analyzing trends in temperature, pressure, and vibration, the model accurately forecasts when an engine needs maintenance, helping to prevent catastrophic failures.

The solution is deployed as an interactive web application where users can upload sensor data and visualize engine health in real-time.

## 🚀 Key Results
* **Model:** Random Forest Regressor
* **Performance (FD001):** **RMSE ~19.00** (Improved from baseline of 50+)
* **Key Technique:** Implemented "RUL Clipping" (max RUL = 125) to align predictions with physical degradation limits.
* **Top Predictors:** Low-Pressure Turbine Outlet Temperature (Sensor 4) and HPT Outlet Pressure (Sensor 9).

## 📊 Domain Analysis & Generalization
A key part of this project was analyzing **Domain Shift**.
* **Success:** The model performs exceptionally well on Sea Level conditions (FD001).
* **Challenge:** When tested on **FD002** (6 different operating conditions), the RMSE rose to ~54.
* **Insight:** The model learned to associate high temperature with failure. In FD002, throttle changes cause temperature spikes that the model mistakes for degradation. This highlights the need for normalization across operating conditions in future iterations.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Machine Learning:** Scikit-Learn (Random Forest)
* **Data Processing:** Pandas, NumPy (Rolling Statistics Feature Engineering)
* **Deployment:** Streamlit Community Cloud
* **Serialization:** Joblib

## 📂 Project Structure
```text
├── app.py                       # Main Streamlit Application
├── cmapss_rf_model_rmse_19.joblib # Trained Random Forest Model
├── Sample_Engine_Data.csv       # Test file for the app
├── requirements.txt             # Dependencies
├── src/                         # Helper scripts
│   └── data_loader.py
└── notebooks/                   # Jupyter Notebooks for analysis
    └──exploration.ipynb
```
## 💻 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/pinocchio02/Predictive-Maintenance.git](https://github.com/pinocchio02/Predictive-Maintenance.git)
    cd Predictive-Maintenance
    ```

2.  **Create and Activate a Virtual Environment (Optional but Recommended)**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```
## 📈 Visualizations
The model successfully tracks the "Sawtooth" pattern of engine degradation:
* **Flat Top**: Represents healthy engines (clipped at 125 cycles).
* **Linear Drop**: Represents the active degradation phase leading to failure.

## 👨‍💻 Author
**OM**
* *Focus:* Data Science, Predictive Maintenance, JavaScript Animations
