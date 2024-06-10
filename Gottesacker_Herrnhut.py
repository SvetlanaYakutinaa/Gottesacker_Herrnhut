import streamlit as st
import folium
from streamlit.components.v1 import html
import json
from folium import IFrame
import branca

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
        
        # HTML-Code für das Popup mit der JPEG-Datei
        html = """
        <h1>Ein Bild in einem Popup</h1><br>
        <img src="Gottesacker_Julius_Titz/Andersen.jpeg" alt="Dein Bild" width="400" height="300">
        <p>
        Hier ist etwas Beispieltext.
        </p>
        """
        
        # IFrame erstellen
        iframe = branca.element.IFrame(html=html, width=500, height=350)
        
        # Popup mit dem IFrame erstellen
        popup = folium.Popup(iframe, max_width=500)
        
        # Marker mit Popup zur Karte hinzufügen 
        #Marker mit Popup zur Karte hinzufügen
        marker_coordinates = [51.019529, 14.748889]  # Koordinaten des Markers
        folium.Marker(marker_coordinates, popup=popup).add_to(m)

        # Speichere die Karte in einer HTML-Datei
        m.save("map.html")

        # Lese die HTML-Datei und zeige sie in Streamlit an
        with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

        # Zeige die HTML-Karte in der Streamlit-Anwendung
        st.components.v1.html(map_html, height=500)


       
     


elif selection == "Analyse":
    st.title("In Arbeit")
    
   
  
     
