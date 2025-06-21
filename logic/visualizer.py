import matplotlib.pyplot as plt

def plot_prediction(X, y, predicted_trend, future_year, future_value, city, crime_type):
    plt.figure(figsize=(7, 4))
    plt.scatter(X, y, color='blue', label='Actual')
    plt.plot(X, predicted_trend, color='green', label='Trend')
    plt.scatter(future_year, future_value, color='red', label=f'{future_year} Prediction')

    plt.title(f'{crime_type} Prediction - {city}')
    plt.xlabel('Year')
    plt.ylabel(f'{crime_type} Cases')
    plt.legend()
    plt.tight_layout()
    plt.show()
