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

# Seiteninhalt basierend auf der Auswahl des Benutzers
if selection == "Karte":
     with st.container():
        
        # Koordinaten für die Anfangsanzeige der Karte
        start_coordinates = (51.019419, 14.748778)
        m = folium.Map(location=start_coordinates, zoom_start=18)
        
        if 'visibility' not in st.session_state:
               st.session_state.visibility = "visible"
               
        if 'disabled' not in st.session_state:
               st.session_state.disabled = False


     option = st.selectbox(
               "Wählen Sie den Name",
               ("Knud Andersen", "Hans Hansen", "Johann Sebald Ringmacher", "Abraham Dürninger", "Benigna Schüz", "Christa Dorothea Lintrup", "Maria Magdalena Richter", "Anna Magdalena Elisabeth Weiss", "Dorothea Maria Ahlsleb", "Mädgen Cornelia Louisa von Goldenberg", "Maria Luley", "Maria Magdalena Bezold"),
               label_visibility=st.session_state.visibility,
               disabled=st.session_state.disabled,
               )
     if option == "Hans Hansen":
                st.subheader("Hans Hansen")
                st.image("Gottesacker_Julius_Titz/Hansen.jpg", width=150, use_column_width="always", caption= "© Julius Titzt")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/524")
     elif option == "Knud Andersen":
                st.subheader("Knud Andersen")
                st.image("Gottesacker_Julius_Titz/Andersen.jpeg", width=350, use_column_width="always", caption= "© Julius Titzt")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766116418/66")
                folium.Marker([51.019529, 14.748889], popup="Knud Andersen. Stein: 7, Reihe: R3, Feld: B2").add_to(m)
        
     elif option== "Johann Sebald Ringmacher": 
               st.subheader("Johann Sebald Ringmacher")
               st.image("Gottesacker_Julius_Titz/Ringmacher.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/743")
     elif option == "Abraham Dürninger":
               st.subheader("Abraham Dürninger")
               st.image("Gottesacker_Julius_Titz/20240525_160853.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/182")
     elif option == "Anna Magdalena Elisabeth Weiss":
                st.subheader("Anna Magdalena Elisabeth Weiss")
                st.image("Gottesacker_Julius_Titz/S3R215.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1745048901/837")
     elif option == "Benigna Schüz":
               st.subheader("Benigna Schüz")
               st.image("Gottesacker_Julius_Titz/S1R103.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766025684/140")
     elif option == "Christa Dorothea Lintrup":
               st.subheader("Christa Dorothea Lintrup")
               st.image("Gottesacker_Julius_Titz/S1R83.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766034756/143")
     elif option == "Dorothea Maria Ahlsleb":
               st.subheader("Dorothea Maria Ahlsleb")
               st.image("Gottesacker_Julius_Titz/20240525_154421.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/394")
     elif option == "Maria Luley":
               st.subheader("Maria Luley")
               st.image("Gottesacker_Julius_Titz/S3R47.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/628")
     elif option == "Maria Magdalena Bezold":
               st.subheader("Maria Magdalena Bezold")
               st.image("Gottesacker_Julius_Titz/S3R411.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/180")
     elif option == "Maria Magdalena Richter":
               st.subheader("Maria Magdalena Richter")
               st.image("Gottesacker_Julius_Titz/S1R813.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766115837/28")
     elif option == "Mädgen Cornelia Louisa von Goldenberg":
               st.subheader("Mädgen Cornelia Louisa von Goldenberg")
               st.image("Gottesacker_Julius_Titz/S3R12.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/527")
            
    

     
     # Speichere die Karte in einer HTML-Datei
     m.save("map.html")

     # Lese die HTML-Datei und zeige sie in Streamlit an
     with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

     # Zeige die HTML-Karte in der Streamlit-Anwendung
     st.components.v1.html(map_html, height=500)


elif selection == "Analyse":
    st.title("In Arbeit")
    
    