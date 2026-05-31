import folium

def generate_map():
    # Create a map centered around Gujarat
    m = folium.Map(location=[23.0, 72.5], zoom_start=6)
    
    # Add a marker for the rainfall station
    folium.Marker(
        [23.0, 72.5], 
        popup="Gujarat Rainfall Station",
        tooltip="Click for info"
    ).add_to(m)
    
    # Save it to an HTML file
    output_file = "india_climate_map.html"
    m.save(output_file)
    print(f"Map successfully generated and saved to {output_file}")

if __name__ == "__main__":
    generate_map()
