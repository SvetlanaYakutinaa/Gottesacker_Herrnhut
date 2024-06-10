import streamlit as st
import folium
from streamlit.components.v1 import html
import pandas as pd
import streamlit_pandas as sp
import json

st.set_page_config(page_title="Gottesacker Herrnhut", layout="wide")

# Seitenleiste mit Links zu verschiedenen Seiten erstellen
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Gehe zu", ["Karte", "Analyse"])

# Seiteninhalt basierend auf der Auswahl des Benutzers aktualisieren
if selection == "Karte":

    # Die Karte auf der Webseite posten
    with st.container():
        st.title("Karte des Gottesackers Herrnhut")
        
        # Koordinaten für die Anfangsanzeige der Karte (zum Beispiel: Berlin)
        start_coordinates = (51.019419, 14.748778)
        m = folium.Map(location=start_coordinates, zoom_start=18)

        # Speichere die Karte in einer HTML-Datei
        m.save("map.html")

        # Lese die HTML-Datei und zeige sie in Streamlit an
        with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

        # Zeige die HTML-Karte in der Streamlit-Anwendung
        st.components.v1.html(map_html, height=500)
        
        json_data = load_json_data("Daten.json")
        
        for item in json_data:
            folium.Marker(
                location=[item["latitude"], item["longitude"]],
                popup=f"""
                <strong>Name:</strong> {item['name']}<br>
                <strong>Datum:</strong> {item['Datum']}<br>
                <strong>Stein:</strong> {item['Stein']}<br>
                <strong>Reihe:</strong> {item['Reihe']}<br>
                <strong>Feld:</strong> {item['Feld']}<br>
                <strong>Index der Gemein-Nachrichten (ab 1765):</strong> {item['Index der Gemein-Nachrichten (ab 1765)']}<br>
                <strong>URL Index:</strong> <a href="{item['URL_Index']}" target="_blank">Link</a><br>
                <strong>Digitalisat:</strong> <a href="{item['Digitalisat']}" target="_blank">Link</a><br>
                <strong>Bild:</strong> <img src="{item['bild']}" width="100"><br>
                <strong>Urheberrecht:</strong> {item['Uhrheberecht']}
                """,
                tooltip=item["name"]
                
            ).add_to(m)


elif selection == "Analyse":
    st.title("In Arbeit")
    
   
  
     
