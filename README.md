# Gujarat Rainfall Monitoring Visualization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Folium](https://img.shields.io/badge/Folium-Mapping-success)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-red)

A geospatial data visualization project mapping annual average rainfall across key monitoring stations in Gujarat, India. This project demonstrates modern data handling and interactive web-map generation using Python, making it an excellent baseline for environmental data analysis.

## 🚀 Features

- **Interactive Mapping:** Built with `folium` using CartoDB Positron tiles for a clean, modern aesthetic.
- **Data Integration:** Utilizes `pandas` to manage and process rainfall data points.
- **Rich Popups:** Formatted HTML popups providing detailed station metadata (coordinates, annual rainfall, operational status).
- **Marker Clustering:** Dynamic clustering for better UX when navigating large datasets.
- **Data-Driven Styling:** Marker colors dynamically adjust based on rainfall volume.

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RajBarot3826/gujarat-rainfall-map.git
   cd gujarat-rainfall-map
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate the visualization:**
   ```bash
   python main.py
   ```

4. **View the result:**
   Open the generated `india_climate_map.html` in any modern web browser.

## 📊 Data Points Included
The initial analysis covers major urban and geographical hubs:
- Ahmedabad
- Surat
- Vadodara
- Rajkot
- Bhavnagar

*Note: The current iteration utilizes simulated historical data for demonstration purposes. It can easily be extended to parse live API feeds or CSV datasets.*
