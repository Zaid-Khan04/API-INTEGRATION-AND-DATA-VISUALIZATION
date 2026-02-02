import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import API_KEY

def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    # Extract the data we need
    weather_info = {
        'city': city,
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
        'description': data['weather'][0]['description']
    }
    return weather_info

# Fetch data for multiple cities
cities = ['London', 'New York', 'Tokyo', 'Paris', 'Mumbai', 'Sydney']
weather_data = []

for city in cities:
    print(f"Fetching weather for {city}...")
    weather_data.append(fetch_weather(city))
# Create a DataFrame(Table)
df = pd.DataFrame(weather_data)
print("\nWeather Data:")
print(df)

# Set style for better-looking plots
sns.set_style("whitegrid")

# Create a figure with multiple subplots (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Weather Dashboard - Multiple Cities', fontsize=16, fontweight='bold')

# 1. Temperature Comparison (Bar Chart)
axes[0, 0].bar(df['city'], df['temperature'], color='orange', alpha=0.7)
axes[0, 0].set_title('Temperature by City (°C)')
axes[0, 0].set_xlabel('City')
axes[0, 0].set_ylabel('Temperature (°C)')
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Humidity Comparison (Bar Chart)
axes[0, 1].bar(df['city'], df['humidity'], color='blue', alpha=0.7)
axes[0, 1].set_title('Humidity by City (%)')
axes[0, 1].set_xlabel('City')
axes[0, 1].set_ylabel('Humidity (%)')
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Wind Speed Comparison (Bar Chart)
axes[1, 0].bar(df['city'], df['wind_speed'], color='green', alpha=0.7)
axes[1, 0].set_title('Wind Speed by City (m/s)')
axes[1, 0].set_xlabel('City')
axes[1, 0].set_ylabel('Wind Speed (m/s)')
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Temperature vs Humidity (Scatter Plot)
axes[1, 1].scatter(df['temperature'], df['humidity'], s=200, color='red', alpha=0.6)
axes[1, 1].set_title('Temperature vs Humidity')
axes[1, 1].set_xlabel('Temperature (°C)')
axes[1, 1].set_ylabel('Humidity (%)')
# Add city labels to each point
for i, city in enumerate(df['city']):
    axes[1, 1].annotate(city, (df['temperature'][i], df['humidity'][i]), fontsize=9, ha='right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the dashboard as an image
plt.savefig('weather_dashboard.png', dpi=300, bbox_inches='tight')
print("\nDashboard saved as 'weather_dashboard.png'")

# Display the dashboard
plt.show()