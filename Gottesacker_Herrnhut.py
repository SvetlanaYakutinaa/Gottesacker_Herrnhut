import streamlit as st
import folium
from streamlit.components.v1 import html
import branca
import streamlit.components.v1 as components



st.set_page_config(page_title="Gottesacker Herrnhut", layout="wide")

# Seitenleiste mit Links zu verschiedenen Seiten erstellen
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Gehe zu", ["Karte", "Analyse"])

# Seiteninhalt basierend auf der Auswahl des Benutzers
if selection == "Karte":
     
     add_selectbox = st.sidebar.radio(
        "Wählen Sie aus",
        ("Digitalisat", "Text", "XML")
    )

     if add_selectbox == "Digitalisat":
            names_d = ["Knud Andersen", "Hans Hansen", "Herrmann Reinhard Schick", "Gottfried Clemens", 
            "Johann Sebald Ringmacher", "Abraham Dürninger", "Benigna Schüz", 
            "Christa Dorothea Lintrupin", "Maria Magdalena Richter", 
            "Anna Magdalena Elisabeth Weiss", "Dorothea Maria Ahlsleb", 
            "Mädgen Cornelia Louisa von Goldenberg", "Maria Luley", "Maria Magdalena Bezold"]
            for name in names_d:
                    st.sidebar.write(name)
     elif add_selectbox == "Text" or "XML":
             names_a = ["Anna Magdalena Elisabeth Weiss", "Knud Andersen", "Christa Dorothea Lintrupin", "Maria Magdalena Richter", "Gottfried Clemens", "Johann Sebald Ringmacher", "Benigna Schüz"]
             for name in names_a:
                     st.sidebar.write(name)
                  

     with st.container():
        
        st.title("Gottesacker Herrnhut")
        
        # Koordinaten für die Anfangsanzeige der Karte
        start_coordinates = (51.019419, 14.748778)
        m = folium.Map(location=start_coordinates, zoom_start=18)
        
        if 'visibility' not in st.session_state:
               st.session_state.visibility = "visible"
               
        if 'disabled' not in st.session_state:
               st.session_state.disabled = False


     option = st.selectbox(
               "Wählen Sie den Name",
               ("Knud Andersen", "Hans Hansen", "Herrmann Reinhard Schick", "Gottfried Clemens", "Johann Sebald Ringmacher", "Abraham Dürninger", "Benigna Schüz", "Christa Dorothea Lintrup", "Maria Magdalena Richter", "Anna Magdalena Elisabeth Weiss", "Dorothea Maria Ahlsleb", "Mädgen Cornelia Louisa von Goldenberg", "Maria Luley", "Maria Magdalena Bezold"),
               label_visibility=st.session_state.visibility,
               disabled=st.session_state.disabled,
               )
     if option == "Hans Hansen":
                st.subheader("Hans Hansen")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/524")
                st.image("Gottesacker_Julius_Titz/Hansen.jpg", width=150, use_column_width="always", caption= "© Julius Titz")
                folium.Marker([51.019574, 14.748516], popup="Hans Hansen. Stein: 6, Reihe: R3, Feld: B2").add_to(m)
       
     elif option == "Knud Andersen":
                st.subheader("Knud Andersen")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766116418/66")
                
                with open("Text/männlich/02541.txt", "rb") as file:
                       btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="02541.txt"
                       )
                with open("XML/02541.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="02541.xml"
                       )
        
                st.image("Gottesacker_Julius_Titz/Andersen.jpeg", width=350, use_column_width="always", caption= "© Julius Titz")
                folium.Marker([51.019529, 14.748889], popup="Knud Andersen. Stein: 7, Reihe: R3, Feld: B2").add_to(m)
                
     elif option== "Johann Sebald Ringmacher": 
               st.subheader("Johann Sebald Ringmacher")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/743")
               with open("Text/männlich/03277.txt", "rb") as file:
                       btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="03277.txt"
                       )
               with open("XML/03277.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="03277.xml"
                       )
               st.image("Gottesacker_Julius_Titz/Ringmacher.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019477, 14.748506], popup="Johann Sebald Ringmacher. Stein: 1, Reihe: R1, Feld: B3").add_to(m)
        
     elif option == "Abraham Dürninger":
               st.subheader("Abraham Dürninger")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/182")
               st.image("Gottesacker_Julius_Titz/20240525_160853.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019577, 14.748488], popup="Abraham Dürninger. Stein: 7, Reihe: R3, Feld: B2").add_to(m)
        
     elif option == "Anna Magdalena Elisabeth Weiss":
                st.subheader("Anna Magdalena Elisabeth Weiss")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1745048901/837")
                with open("Text/weiblich/00196.txt", "rb") as file:
                        btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="00196.txt"
                       )
                with open("XML/00196.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="00196.xml"
                       )
                st.image("Gottesacker_Julius_Titz/S3R215.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
                folium.Marker([51.019115, 14.748836], popup="Anna Magdalena Elisabeth Weiss. Stein: 15, Reihe: R2, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Benigna Schüz":
               st.subheader("Benigna Schüz")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766025684/140")
               with open("Text/weiblich/00977.txt", "rb") as file:
                       btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="00977.txt"
                       )
               with open("XML/00977.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="00977.xml"
                       )
               st.image("Gottesacker_Julius_Titz/S1R103.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019103, 14.748604], popup="Benigna Schüz. Stein: 6, Reihe: R5, Feld: B3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Christa Dorothea Lintrupin":
               st.subheader("Christa Dorothea Lintrupin")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766034756/143")
               with open("Text/weiblich/01789.txt", "rb") as file:
                       btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="01789.txt"
                       )
               with open("XML/01789.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="01789.xml"
                       )
               st.image("Gottesacker_Julius_Titz/S1R83.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019112, 14.748551], popup="Christa Dorothea Lintrup. Stein: 3, Reihe: R10, Feld: S1", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Dorothea Maria Ahlsleb":
               st.subheader("Dorothea Maria Ahlsleb")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/394")
               st.image("Gottesacker_Julius_Titz/20240525_154421.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019036, 14.748669], popup="Dorothea Maria Ahlsleb. Stein: 1, Reihe: R1, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Maria Luley":
               st.subheader("Maria Luley")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/628")
               st.image("Gottesacker_Julius_Titz/S3R47.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019057, 14.748774], popup="Maria Luley. Stein: 7, Reihe: R4, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Maria Magdalena Bezold":
               st.subheader("Maria Magdalena Bezold")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/180")
               st.image("Gottesacker_Julius_Titz/S3R411.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019082, 14.748807], popup="Maria Magdalena Bezold. Stein: 11, Reihe: R4, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
               
        
     elif option == "Maria Magdalena Richter":
               st.subheader("Maria Magdalena Richter")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766115837/28") 
               
               with open("Text/weiblich/02445.txt", "rb") as file:
                       btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="02445.txt"
                       )
               with open("XML/02445.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="02445.xml"
                       )
               st.image("Gottesacker_Julius_Titz/S1R813.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019203, 14.748634], popup="Maria Magdalena Richter. Stein: 3, Reihe: R8, Feld: S1", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Mädgen Cornelia Louisa von Goldenberg":
               st.subheader("Mädgen Cornelia Louisa von Goldenberg")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/527") 
               st.image("Gottesacker_Julius_Titz/S3R12.jpg", width=350, use_column_width="always", caption= "© Julius Titz")
               folium.Marker([51.019050, 14.748683], popup="Mädgen Cornelia Louisa von Goldenberg. Stein: 2, Reihe: R1, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
       
        
     elif option == "Gottfried Clemens":
               st.subheader("Gottfried Clemens")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766148077/273") 
               folium.Marker([51.019578, 14.748048], popup="Gottfried Clemens. Stein: 25, Reihe: R5, Feld: B3").add_to(m)
               with open("Text/männlich/05198.txt", "rb") as file:
                       btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="05198.txt"
                       )

               with open("XML/05198.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="05198.xml"
                       )

          
     elif option == "Herrmann Reinhard Schick":
               st.subheader("Herrmann Reinhard Schick")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766115837/419") 
               folium.Marker([51.019360, 14.748201], popup="Herrmann Reinhard Schick. Stein: 10, Reihe: R7, Feld: B1").add_to(m)
     
     # Speichere die Karte in einer HTML-Datei
     m.save("map.html")

     # Lese die HTML-Datei und zeige sie in Streamlit an
     with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

     # Zeige die HTML-Karte in der Streamlit-Anwendung
     st.components.v1.html(map_html, height=500)
     
elif selection == "Analyse":
    st.title("In Arbeit")

    st.image('wordcloud_w.png', caption='WordCloud von Frauen')

    st.image('wordcloud_m.png', caption='WordCloud von Männern')

    st.image('grafik.png', caption='Häufigkeit der Top 50 Lemmata - Männer vs. Frauen')