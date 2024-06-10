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

        # Koordinaten für die Anfangsanzeige der Karte
        start_coordinates = (51.019419, 14.748778)
        m = folium.Map(location=start_coordinates, zoom_start=18)

        #folium.Marker([51.019529, 14.748889], popup="Knud Andersen").add_to(m)
        folium.Marker([51.019574, 14.748516], popup="Hans Hansen").add_to(m)
        folium.Marker([51.019477, 14.748506], popup="Johann Sebald Ringmacher").add_to(m)
        folium.Marker([51.019577, 14.748488], popup="Abraham Dürninger").add_to(m)
        folium.Marker([51.019103, 14.748604], popup="Benigna Schüz", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019112, 14.748551], popup="Christa Dorothea Lintrup", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019203, 14.748634], popup="Maria Magdalena Richter", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019115, 14.748836], popup="Anna Magdalena Elisabeth Weiss", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019036, 14.748669], popup="Dorothea Maria Ahlsleb", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019050, 14.748683], popup="Mädgen Cornelia Louisa von Goldenberg", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019057, 14.748774], popup=" Maria Luley", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019082, 14.748807], popup="Maria Magdalena Bezold", icon=folium.Icon(color='red')).add_to(m)
        #probe 
        folium.Marker([51.019529, 14.748889], popup='<a href="https://example.com">Klicken Sie hier für weitere Informationen</a>').add_to(m)
        #'<a href="https://example.com">Klicken Sie hier für weitere Informationen</a>'

        # Speichere die Karte in einer HTML-Datei
        m.save("map.html")

        # Lese die HTML-Datei und zeige sie in Streamlit an
        with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

        # Zeige die HTML-Karte in der Streamlit-Anwendung
        st.components.v1.html(map_html, height=500)

elif selection == "Analyse":
    st.title("In Arbeit")
    
    st.image("Gottesacker_Julius_Titz/Andersen.jpeg", width=300, caption="Bildunterschrift")