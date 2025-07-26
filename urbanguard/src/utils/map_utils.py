import folium

def create_violation_map(lat, lon, label="Suspected Violation"):
    map_ = folium.Map(location=[lat, lon], zoom_start=17)
    folium.Marker([lat, lon], tooltip=label, icon=folium.Icon(color='red')).add_to(map_)
    return map_
