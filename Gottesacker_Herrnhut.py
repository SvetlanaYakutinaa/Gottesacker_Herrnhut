import streamlit as st
from streamlit_folium import st_folium
import folium
from streamlit.components.v1 import html

st.set_page_config(page_title="Gottesacker Herrnhut", layout="wide")

# Seitenleiste mit Links zu verschiedenen Seiten erstellen
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Gehe zu", ["Karte", "Analyse"])

# Seiteninhalt basierend auf der Auswahl des Benutzers aktualisieren
if selection == "Karte":

     # Die Karte auf der Webseite posten
     with st.container():
          st.title("Karte des Gottesackers in Herrnhut")
          
          # Koordinaten für die Anfangsanzeige der Karte (zum Beispiel: Berlin)
          start_coordinates = (51.019419, 14.748778)
          m = folium.Map(location=start_coordinates, zoom_start=12)

          # Speichere die Karte in einer HTML-Datei
          m.save("map.html")

          # Lese die HTML-Datei und zeige sie in Streamlit an
          with open("map.html", "r", encoding="utf-8") as f:
              map_html = f.read()

          # Zeige die HTML-Karte in der Streamlit-Anwendung
          html(map_html, height=500)

