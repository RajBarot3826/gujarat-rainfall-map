import folium
import pandas as pd
from folium.plugins import MarkerCluster

def load_data():
    # Simulated average annual rainfall data for major Gujarat cities (in mm)
    data = {
        "Station": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar"],
        "Latitude": [23.0225, 21.1702, 22.3072, 22.3039, 21.7645],
        "Longitude": [72.5714, 72.8311, 73.1812, 70.8022, 72.1519],
        "Avg_Annual_Rainfall_mm": [800, 1200, 900, 600, 650],
        "Status": ["Active", "Active", "Active", "Active", "Active"]
    }
    return pd.DataFrame(data)

def get_color(rainfall):
    if rainfall < 700:
        return '#f39c12' # Orange
    elif rainfall < 1000:
        return '#27ae60' # Green
    else:
        return '#2980b9' # Blue

def generate_professional_map():
    df = load_data()
    
    # Initialize map centered on Gujarat with a professional map tile
    m = folium.Map(location=[22.2587, 71.1924], zoom_start=7, tiles='CartoDB positron')
    
    # Add title
    title_html = '''
             <h3 align="center" style="font-family: Arial, sans-serif; font-size:20px; font-weight:bold; margin-top: 20px;">
             <b>Gujarat Rainfall Monitoring Stations</b>
             </h3>
             '''
    m.get_root().html.add_child(folium.Element(title_html))
    
    # Create a marker cluster
    marker_cluster = MarkerCluster(name="Rainfall Stations").add_to(m)
    
    for idx, row in df.iterrows():
        # Construct professional HTML popup
        popup_html = f"""
        <div style="width: 200px; font-family: Arial, sans-serif;">
            <h4 style="margin-bottom: 5px; color: #2c3e50;">{row['Station']} Station</h4>
            <hr style="margin: 5px 0; border: 0; border-top: 1px solid #eee;">
            <p style="margin: 5px 0; font-size: 13px;"><b>Coordinates:</b> {row['Latitude']:.2f}, {row['Longitude']:.2f}</p>
            <p style="margin: 5px 0; font-size: 13px;"><b>Annual Rainfall:</b> {row['Avg_Annual_Rainfall_mm']} mm</p>
            <p style="margin: 5px 0; font-size: 13px;"><b>Status:</b> <span style="color: #27ae60; font-weight: bold;">{row['Status']}</span></p>
        </div>
        """
        
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=12,
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=f"{row['Station']} - Click for details",
            color=get_color(row['Avg_Annual_Rainfall_mm']),
            fill=True,
            fill_color=get_color(row['Avg_Annual_Rainfall_mm']),
            fill_opacity=0.7,
            weight=2
        ).add_to(marker_cluster)
        
    # Add layer control
    folium.LayerControl().add_to(m)
    
    output_file = "india_climate_map.html"
    m.save(output_file)
    print(f"Professional map generated: {output_file}")

if __name__ == "__main__":
    generate_professional_map()
