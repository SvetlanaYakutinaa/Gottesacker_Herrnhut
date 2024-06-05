import streamlit as st
import folium
from streamlit.components.v1 import html

st.title("Karte des Gottesackers Herrnhut")

map_center = [51.019419, 14.748778]
m = folium.Map(location=map_center, zoom_start=19)


folium.Marker([51.05853, 14.4437662], popup="Andersen").add_to(m)

m.save("mape.html")

# Lese die HTML-Datei und zeige sie in Streamlit an
with open("map.html", "r", encoding="utf-8") as f:
    map_html = f.read()

# Zeige die HTML-Karte in der Streamlit-Anwendung
html(map_html, height=500)

