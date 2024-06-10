import streamlit as st
import folium
from streamlit.components.v1 import html
import json
from folium import IFrame
import branca
import streamlit.components.v1 as components


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

        folium.Marker([51.019529, 14.748889], popup="Knud Andersen. Stein: 7, Reihe: R3, Feld: B2").add_to(m)
        folium.Marker([51.019574, 14.748516], popup="Hans Hansen. Stein: 6, Reihe: R3, Feld: B2").add_to(m)
        folium.Marker([51.019477, 14.748506], popup="Johann Sebald Ringmacher. Stein: 1, Reihe: R1, Feld: B3").add_to(m)
        folium.Marker([51.019577, 14.748488], popup="Abraham Dürninger. Stein: 7, Reihe: R3, Feld: B2").add_to(m)
        folium.Marker([51.019103, 14.748604], popup="Benigna Schüz. Stein: 6, Reihe: R5, Feld: B3", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019112, 14.748551], popup="Christa Dorothea Lintrup. Stein: 3, Reihe: R10, Feld: S1", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019203, 14.748634], popup="Maria Magdalena Richter. Stein: 3, Reihe: R8, Feld: S1", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019115, 14.748836], popup="Anna Magdalena Elisabeth Weiss. Stein: 15, Reihe: R2, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019036, 14.748669], popup="Dorothea Maria Ahlsleb. Stein: 1, Reihe: R1, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019050, 14.748683], popup="Mädgen Cornelia Louisa von Goldenberg. Stein: 2, Reihe: R1, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019057, 14.748774], popup="Maria Luley. Stein: 7, Reihe: R4, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        folium.Marker([51.019082, 14.748807], popup="Maria Magdalena Bezold. Stein: 11, Reihe: R4, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
        # Speichere die Karte in einer HTML-Datei
        m.save("map.html")

        # Lese die HTML-Datei und zeige sie in Streamlit an
        with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

        # Zeige die HTML-Karte in der Streamlit-Anwendung
        st.components.v1.html(map_html, height=500)

        with st.container():
            st.title("Digitale Friedhof")
            
            st.write("Hans Hansen")
            st.image("Gottesacker_Julius_Titz/Hansen.jpg", width=150, use_column_width="always")
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/524")
            
            st.write("Knud Andersen")
            st.image("Gottesacker_Julius_Titz/Andersen.jpeg", width=150, use_column_width="always")
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766116418/66")
            
            st.write("Johann Sebald Ringmacher")
            st.image("Gottesacker_Julius_Titz/Hansen.jpg", width=150, use_column_width="always")
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/524")
            
            st.write("Johann Sebald Ringmacher")
            st.image("Gottesacker_Julius_Titz/Ringmacher.jpg", width=150, use_column_width="always")
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/743")
            
            st.write("Abraham Dürninger")
            st.image("Gottesacker_Julius_Titz/20240525_160853.jpg", length=350, use_column_width="always")
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/182")
            
            st.write("Johann Sebald Ringmacher")
            st.image("Gottesacker_Julius_Titz/Hansen.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/524")
            
            st.write("Benigna Schüz")
            st.image("Gottesacker_Julius_Titz/S1R103.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766025684/140")
            
            st.write("Christa Dorothea Lintrup")
            st.image("Gottesacker_Julius_Titz/S1R83.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766034756/143")
            
            st.write("Maria Magdalena Richter")
            st.image("Gottesacker_Julius_Titz/S1R813.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766115837/28")
            
            st.write("Anna Magdalena Elisabeth Weiss")
            st.image("Gottesacker_Julius_Titz/S3R215.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1745048901/837")
            
            st.write("Dorothea Maria Ahlsleb")
            st.image("Gottesacker_Julius_Titz/20240525_154421.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/394")
            
            st.write("Mädgen Cornelia Louisa von Goldenberg")
            st.image("Gottesacker_Julius_Titz/S3R12.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/527")
            
            st.write("Maria Luley")
            st.image("Gottesacker_Julius_Titz/S3R47.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/628")
            
            st.write("Maria Magdalena Bezold")
            st.image("Gottesacker_Julius_Titz/S3R411.jpg", width=350)
            st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/180")
            


elif selection == "Analyse":
    st.title("In Arbeit")
    
    