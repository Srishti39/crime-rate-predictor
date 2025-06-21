import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
def load_data(path='data/crime_data.csv'):
    return pd.read_csv(path)

# Predict crime cases for a given city, crime type and year
def predict_crime(data, city, crime_type, future_year):
    city_data = data[data['City'] == city]
    X = city_data[['Year']]
    y = city_data[crime_type]

    model = LinearRegression()
    model.fit(X, y)

    future_df = pd.DataFrame(np.array([[future_year]]), columns=['Year'])
    prediction = model.predict(future_df)

    return int(prediction[0]), model.predict(X)
