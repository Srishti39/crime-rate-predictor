# Crime Rate Predictor — India (2025 Forecast)

The **Crime Rate Predictor** is a Python-based application that forecasts future crime trends in major Indian cities using historical data and machine learning. It provides valuable insights through visualizations and helps raise awareness with safety tips.

---

## 🔍 Features

- Predicts crime statistics for **Theft, Assault, Robbery, and Murder**.
- Forecasts crime cases for the year **2025** using historical trends.
- Allows analysis for both **individual cities** and **all cities** collectively.
- Displays results with **line plots**, **bar charts**, and **pie charts**.
- Highlights the **most and least predicted crimes** per city.
- Offers **precautionary safety tips**.
- Supports **interactive plots** via Plotly (if installed).

---

## 🧰 Tech Stack

|    Technology     |               Purpose                         |
|------------------ |---------------------------------------------- |
| **Python 3.x**    | Core programming language                     |
| **Pandas**        | Data loading and manipulation                 |
| **NumPy**         | Numerical array handling                      |
| **Scikit-learn**  | Linear Regression model for prediction        |
| **Matplotlib**    | Static visualizations (line, bar, pie charts) |
| **Plotly**        | Interactive visualizations (bar charts)       |
| **CSV (Data)**    | Stores historical crime records               |

---

## 📁 Project Structure

Crime detection
1. data/crime_data.csv                 # Historical crime data
2. logic/predictor.py                  # Data loading and prediction logic
3. logic/visualizer.py                 # Crime trend plotting functions
4. logic/combined_visualizer.py        # Combined crimes visualization (bar & pie charts)
5. main_app.py                         # Main application script with user interface
6. README.md                           # Project overview and instructions

---

## ⚙️ Installation

1. **Clone this repository** or download the project files.

2. *(Optional but recommended)* Create and activate a virtual environment:

        ```bash
        python -m venv venv
        
        # On Windows
        venv\Scripts\activate
        
        # On macOS/Linux
        source venv/bin/activate

3. Install the required dependencies:
        
        pip install pandas numpy scikit-learn matplotlib plotly

---

## 🚀 Usage

Run the main script:
    python main_app.py

You will be guided to:
1. Choose between analyzing a single city or all cities.
2. Select the crime type or opt for a combined analysis.
3. View predicted crime cases for 2025 with visual outputs.
4. Read safety tips at the end for user awareness.

---

## 🧠 How It Works

1. Loads historical crime data from a CSV file.
2. Trains a Linear Regression model to learn city-wise trends.
3. Predicts crime counts for the year 2025.
4. Visualizes predictions using static and optional interactive charts.
5. Highlights maximum and minimum predicted crimes for comparison.
6. Enhances social awareness by suggesting basic precautions.
