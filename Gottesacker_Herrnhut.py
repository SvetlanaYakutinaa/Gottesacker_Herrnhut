import streamlit as st

import folium

import json
from streamlit.components.v1 import html

# Lade die JSON-Daten
with open("/Users/svetlana/Desktop/Gottesacker_Herrnhut/Daten.json") as f: 
    data = json.load(f)

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
          m = folium.Map(location=start_coordinates, zoom_start=18)

          for point in data:
              popup_text = f"{point['name']}<br>{point['Uhrheberecht']}<br><img src='{point['bild']}' width='150'>"
              
              folium.Marker(
                  location=[point['latitude'], point['longitude']],
                  popup=popup_text
              ).add_to(m) 

          # Speichere die Karte in einer HTML-Datei
          m.save("map.html")

          # Lese die HTML-Datei und zeige sie in Streamlit an
          with open("map.html", "r", encoding="utf-8") as f:
              map_html = f.read()

          # Zeige die HTML-Karte in der Streamlit-Anwendung
          html(map_html, height=700)


elif selection == "Analyse":
    st.title("Analyse")
    st.write("In Arbeit")


   




   


