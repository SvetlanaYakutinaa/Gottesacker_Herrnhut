import streamlit as st
import folium
from streamlit.components.v1 import html
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
        
        if json_data:
            for item in json_data:
                try:
                    # Überprüfen der notwendigen Felder
                    name = item.get("name", "Unbekannt")
                    latitude = item.get("latitude")
                    longitude = item.get("longitude")
                    if latitude and longitude:
                        folium.Marker(
                            location=[latitude, longitude],
                            popup=f"""
                            <strong>Name:</strong> {name}<br>
                            <strong>Datum:</strong> {item.get('Datum', 'Unbekannt')}<br>
                            <strong>Stein:</strong> {item.get('Stein', 'Unbekannt')}<br>
                            <strong>Reihe:</strong> {item.get('Reihe', 'Unbekannt')}<br>
                            <strong>Feld:</strong> {item.get('Feld', 'Unbekannt')}<br>
                            <strong>Index der Gemein-Nachrichten (ab 1765):</strong> {item.get('Index der Gemein-Nachrichten (ab 1765)', 'Unbekannt')}<br>
                            <strong>URL Index:</strong> <a href="{item.get('URL_Index', '#')}" target="_blank">Link</a><br>
                            <strong>Digitalisat:</strong> <a href="{item.get('Digitalisat', '#')}" target="_blank">Link</a><br>
                            <strong>Bild:</strong> <img src="{item.get('bild', '')}" width="100"><br>
                            <strong>Urheberrecht:</strong> {item.get('Uhrheberecht', 'Unbekannt')}
                            """,
                            tooltip=name
                        ).add_to(m)
                    else:
                        st.warning(f"Fehlende Koordinaten für {name}")
                except Exception as e:
                    st.error(f"Fehler beim Hinzufügen des Markers für {name}: {e}")
        else:
            st.error("Keine Daten in der JSON-Datei gefunden")
        
        # Speichere die Karte in einer HTML-Datei
        m.save("map.html")

        # Lese die HTML-Datei und zeige sie in Streamlit an
        with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

        # Zeige die HTML-Karte in der Streamlit-Anwendung
        st.components.v1.html(map_html, height=500)


elif selection == "Analyse":
    st.title("In Arbeit")
    
   
  
     
