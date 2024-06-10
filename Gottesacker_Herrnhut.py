import streamlit as st
import folium
from streamlit.components.v1 import html
import json
from folium import IFrame
from streamlit_folium import folium_static

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

        folium.Marker([51.019529, 14.748889], popup="Knud Andersen").add_to(m)    
        
        # Bild-URL
        img_url = 'https://example.com/path/to/your/image.jpg'  # Ersetze durch die tatsächliche URL deines Bildes
        
        # HTML-Code für das Bild
        html = f'<img src="{img_url}" width="300" height="200">'
        
        # Erstelle ein IFrame-Objekt
        iframe = folium.IFrame(html, width=310, height=210)
        
        # Erstelle ein Popup mit dem IFrame
        popup = folium.Popup(iframe, max_width=310)
        
        # Erstelle den Marker mit dem Popup
        folium.Marker([51.019529, 14.748889], popup=popup).add_to(m)
        
        # Rendere die Karte in Streamlit
        folium_static(m)

        # Lese die HTML-Datei und zeige sie in Streamlit an
        with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

        # Zeige die HTML-Karte in der Streamlit-Anwendung
        st.components.v1.html(map_html, height=500)
        


elif selection == "Analyse":
    st.title("In Arbeit")
    
   
  
     
