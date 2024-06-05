import streamlit as st
import folium
from streamlit.components.v1 import html

# Setze den Titel der Streamlit-Anwendung
st.title("Interaktive Karte mit Streamlit und Folium")

# Erstelle eine Basis-Karte
map_center = [48.8566, 2.3522]  # Koordinaten für Paris
m = folium.Map(location=map_center, zoom_start=12)

# Füge Marker zur Karte hinzu
folium.Marker([48.8566, 2.3522], popup="Paris", tooltip="Klicken für mehr Info").add_to(m)
folium.Marker([48.8584, 2.2945], popup="Eiffelturm", tooltip="Klicken für mehr Info").add_to(m)
folium.Marker([48.853, 2.3499], popup="Notre-Dame", tooltip="Klicken für mehr Info").add_to(m)

# Speichere die Karte in einer HTML-Datei
m.save("map.html")

# Lese die HTML-Datei und zeige sie in Streamlit an
with open("map.html", "r", encoding="utf-8") as f:
    map_html = f.read()

# Zeige die HTML-Karte in der Streamlit-Anwendung
html(map_html, height=500)
