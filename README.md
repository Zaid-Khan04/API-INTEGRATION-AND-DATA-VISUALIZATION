# 🌤️ Weather Pro - Real-time Weather Dashboard:-
A professional weather dashboard providing real-time weather data and 7-day forecasts for any city worldwide. Features interactive visualizations and a modern, responsive design.

Weather Dashboard

<img width="1895" height="910" alt="image" src="https://github.com/user-attachments/assets/119fdd57-c566-4f30-9a0a-835e7b84cb22" />
<img width="1889" height="810" alt="image" src="https://github.com/user-attachments/assets/7eadf138-aa0c-4c52-8a08-b3be248994f7" />



## ✨ Features

- **Real-time Weather Data**: Current conditions including temperature, humidity, wind speed, pressure, and visibility
- **7-Day Forecast**: Daily predictions with high/low temperatures and weather icons
- **Interactive Charts**: Canvas-based visualizations for current conditions and temperature trends
- **Astronomical Data**: Sunrise/sunset times and wind direction
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Live Updates**: Auto-updating date/time display

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **API**: OpenWeatherMap API
- **Visualization**: HTML5 Canvas for charts
- **Python Script**: Matplotlib, Seaborn, Pandas (for additional analysis)

## 🚀 Quick Start

### 1. Get API Key
- Sign up at [OpenWeatherMap](https://openweathermap.org/api)
- Get your free API key
- Wait 10-20 minutes for activation

### 2. Setup Web Dashboard
1. Open `script.js`
2. Replace `'YOUR_API_KEY_HERE'` with your API key:
```javascript
const API_KEY = 'your_actual_api_key';
```
3. Double-click `index.html` to open in browser

### 3. Setup Python Script (Optional)
```bash
# Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add API key to config.py
# Run script
python weather_dashboard.py
```

## 📁 Project Structure
```
weather-pro/
├── index.html              # Main webpage
├── style.css               # Styling
├── script.js               # JavaScript logic
├── config.py               # Python API configuration
├── weather_dashboard.py    # Python visualization script
├── requirements.txt        # Python dependencies
└── README.md              # Documentation
```

## 💻 Usage

**Web Dashboard:**
- Open `index.html` in any modern browser
- Enter a city name and click "Search"
- View current weather and 7-day forecast

**Python Dashboard:**
```bash
python weather_dashboard.py
```
Generates static visualizations saved as `weather_dashboard.png`

## 🎨 Key Features

### Current Weather Display
- Large temperature display with "feels like" metric
- Wind speed, humidity, pressure, visibility
- Sunrise/sunset times
- Cloud coverage and wind direction

### 7-Day Forecast
- Daily weather predictions
- Temperature ranges (high/low)
- Weather condition icons
- Brief descriptions

### Data Visualizations
1. **Current Conditions Chart**: Bar chart of key metrics
2. **Temperature Trend**: Line graph showing 7-day temperature patterns

## 🐛 Troubleshooting

**Invalid API Key**: Wait 10-20 minutes after creation, verify no extra spaces

**City Not Found**: Check spelling, try format "City,CountryCode" (e.g., "London,UK")

**Charts Not Loading**: Check browser console, refresh page, clear cache

**Python Errors**: Ensure virtual environment is activated and dependencies installed

## 📊 API Endpoints
```
Current Weather: api.openweathermap.org/data/2.5/weather
Forecast: api.openweathermap.org/data/2.5/forecast
```

## 🔒 Security

- Never commit `config.py` with your API key
- Add `config.py` to `.gitignore`
- For production, use environment variables

## 📝 Assignment Completion

✅ Fetches data from public API (OpenWeatherMap)  
✅ Creates visualizations using Matplotlib/Seaborn  
✅ Includes Python script and web dashboard  
✅ Professional, functional implementation

## 🎯 Future Enhancements

- Hourly forecast
- Weather alerts
- Geolocation support
- Dark mode
- Celsius/Fahrenheit toggle
- Multiple city comparison

## 👨‍💻 Author

**Your Name**
- GitHub: [@Zaid-Khan04](https://github.com/Zaid-Khan04)
- Email: zk7193625@gmail.com

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for free weather API
- Modern weather apps for design inspiration

## 📄 License

MIT License - feel free to use this project for learning and development.

---

*Built with JavaScript, Python, and lots of ☕*
