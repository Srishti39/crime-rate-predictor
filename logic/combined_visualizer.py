import matplotlib.pyplot as plt
import os

# Optional Plotly
try:
    import plotly.graph_objects as go
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

def plot_combined_crimes(city, crime_values, save=False):
    labels = list(crime_values.keys())
    values = list(crime_values.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=['#4caf50', '#2196f3', '#ff9800', '#f44336'])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 5, f'{int(yval)}', ha='center')

    plt.title(f"{city} - Predicted Crimes in 2025", fontsize=14)
    plt.xlabel("Crime Type")
    plt.ylabel("Cases")
    plt.tight_layout()

    if save:
        os.makedirs("output", exist_ok=True)
        plt.savefig(f"output/{city}_bar_chart.png")
        print(f"✅ Saved bar chart: output/{city}_bar_chart.png")
    plt.show()

def plot_combined_pie(city, crime_values, save=False):
    labels = list(crime_values.keys())
    values = list(crime_values.values())
    colors = ['#4caf50', '#2196f3', '#ff9800', '#f44336']

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(f"{city} - Crime Share in 2025")
    plt.axis('equal')
    plt.tight_layout()

    if save:
        os.makedirs("output", exist_ok=True)
        plt.savefig(f"output/{city}_pie_chart.png")
        print(f"✅ Saved pie chart: output/{city}_pie_chart.png")
    plt.show()

def plot_side_by_side(city, crime_values, save=False):
    labels = list(crime_values.keys())
    values = list(crime_values.values())
    colors = ['#4caf50', '#2196f3', '#ff9800', '#f44336']

    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    axs[0].bar(labels, values, color=colors)
    axs[0].set_title(f"{city} - Crime Cases")
    axs[0].set_ylabel("Cases")
    axs[0].set_xlabel("Crime Type")
    for i, v in enumerate(values):
        axs[0].text(i, v + 5, str(int(v)), ha='center')

    axs[1].pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    axs[1].set_title(f"{city} - Crime Share")

    plt.tight_layout()
    if save:
        os.makedirs("output", exist_ok=True)
        file_path = f"output/{city}_side_by_side.png"
        plt.savefig(file_path)
        print(f"✅ Saved side-by-side chart: {file_path}")
    plt.show()

def plot_interactive(city, crime_values):
    if not HAS_PLOTLY:
        print("⚠️ Plotly not installed. Run: pip install plotly")
        return

    labels = list(crime_values.keys())
    values = list(crime_values.values())
    fig = go.Figure([go.Bar(x=labels, y=values, marker_color='indianred')])
    fig.update_layout(title=f"{city} - Interactive Crime Prediction (2025)",
                      xaxis_title="Crime Type",
                      yaxis_title="Cases")
    fig.show()
