import pandas as pd
from logic.predictor import load_data, predict_crime
from logic.visualizer import plot_prediction
from logic.combined_visualizer import plot_combined_crimes, plot_combined_pie


def welcome_message():
    print("\n📊 Welcome to the Crime Rate Predictor 📊")
    print("Predict future crime trends for Indian cities with visuals.\n")

def choose_mode():
    print("Choose mode:\n1. Individual City\n2. All Cities")
    choice = input("Enter 1 or 2: ")
    return choice.strip()

def select_city(data):
    cities = sorted(data['City'].unique())
    print("\nAvailable Cities:")
    for i, city in enumerate(cities):
        print(f"{i+1}. {city}")
    city_index = int(input("Enter the city number: ")) - 1
    return cities[city_index]

def select_crime_type():
    print("\nChoose a crime type:")
    print("1. Theft\n2. Assault\n3. Robbery\n4. Murder\n5. Combined")
    choice = input("Enter 1 to 5: ").strip()
    mapping = {
        "1": "Theft",
        "2": "Assault",
        "3": "Robbery",
        "4": "Murder",
        "5": "Combined"
    }
    return mapping.get(choice, "Theft")

def show_precautions():
    print("\n🔒 Precautionary Measures:")
    print("- Stay alert in public places.")
    print("- Avoid travelling alone at night.")
    print("- Install security systems at home.")
    print("- Always inform family when heading out.\n")

def main():
    welcome_message()
    data = load_data()
    mode = choose_mode()
    future_year = 2025

    if mode == '1':
        city = select_city(data)
        crime = select_crime_type()

        if crime != "Combined":
            pred_value, trend = predict_crime(data, city, crime, future_year)
            print(f"\nPredicted {crime} cases in {future_year} for {city}: {pred_value}")
            X = data[data['City'] == city][['Year']]
            y = data[data['City'] == city][crime]
            plot_prediction(X, y, trend, future_year, pred_value, city, crime)
        else:
            crimes = ['Theft', 'Assault', 'Robbery', 'Murder']
            values = {}
            for c in crimes:
                value, trend = predict_crime(data, city, c, future_year)
                values[c] = value
                X = data[data['City'] == city][['Year']]
                y = data[data['City'] == city][c]
                plot_prediction(X, y, trend, future_year, value, city, c)

            max_crime = max(values, key=values.get)
            min_crime = min(values, key=values.get)
            print(f"\n📈 Highest predicted crime in 2025: {max_crime} ({values[max_crime]})")
            print(f"📉 Lowest predicted crime in 2025: {min_crime} ({values[min_crime]})")
            plot_combined_crimes(city, values)
            plot_combined_pie(city, values)

    elif mode == '2':
        crime = select_crime_type()
        cities = sorted(data['City'].unique())

        for city in cities:
            if crime != "Combined":
                pred_value, trend = predict_crime(data, city, crime, future_year)
                print(f"\n{city}: Predicted {crime} cases in {future_year}: {pred_value}")
                X = data[data['City'] == city][['Year']]
                y = data[data['City'] == city][crime]
                plot_prediction(X, y, trend, future_year, pred_value, city, crime)
            else:
                crimes = ['Theft', 'Assault', 'Robbery', 'Murder']
                values = {}
                for c in crimes:
                    value, trend = predict_crime(data, city, c, future_year)
                    values[c] = value
                    X = data[data['City'] == city][['Year']]
                    y = data[data['City'] == city][c]
                    plot_prediction(X, y, trend, future_year, value, city, c)

                max_crime = max(values, key=values.get)
                min_crime = min(values, key=values.get)
                print(f"\n{city}: 📈 Highest predicted crime: {max_crime} ({values[max_crime]})")
                print(f"{city}: 📉 Lowest predicted crime: {min_crime} ({values[min_crime]})")
                plot_combined_crimes(city, values)
                plot_combined_pie(city, values)

    show_precautions()
    print("📬 For help, contact: support@srishtipanda.dev")
    print("© Copyright by Srishti Panda")

if __name__ == "__main__":
    main()
