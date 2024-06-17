import streamlit as st
import folium
from streamlit.components.v1 import html
import branca
import streamlit.components.v1 as components

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.set_page_config(page_title="Gottesacker Herrnhut", layout="wide")

# Seitenleiste mit Links zu verschiedenen Seiten erstellen
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Gehe zu", ["Karte", "Analyse"])

# Seiteninhalt basierend auf der Auswahl des Benutzers
if selection == "Karte":
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
                st.image("Gottesacker_Julius_Titz/Hansen.jpg", width=150, use_column_width="always", caption= "© Julius Titzt")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/524")
                folium.Marker([51.019574, 14.748516], popup="Hans Hansen. Stein: 6, Reihe: R3, Feld: B2").add_to(m)
       
     elif option == "Knud Andersen":
                st.subheader("Knud Andersen")
                st.image("Gottesacker_Julius_Titz/Andersen.jpeg", width=350, use_column_width="always", caption= "© Julius Titzt")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766116418/66")
                folium.Marker([51.019529, 14.748889], popup="Knud Andersen. Stein: 7, Reihe: R3, Feld: B2").add_to(m)
        
     elif option== "Johann Sebald Ringmacher": 
               st.subheader("Johann Sebald Ringmacher")
               st.image("Gottesacker_Julius_Titz/Ringmacher.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/743")
               folium.Marker([51.019477, 14.748506], popup="Johann Sebald Ringmacher. Stein: 1, Reihe: R1, Feld: B3").add_to(m)
        
     elif option == "Abraham Dürninger":
               st.subheader("Abraham Dürninger")
               st.image("Gottesacker_Julius_Titz/20240525_160853.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/182")
               folium.Marker([51.019577, 14.748488], popup="Abraham Dürninger. Stein: 7, Reihe: R3, Feld: B2").add_to(m)
        
     elif option == "Anna Magdalena Elisabeth Weiss":
                st.subheader("Anna Magdalena Elisabeth Weiss")
                st.image("Gottesacker_Julius_Titz/S3R215.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
                st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1745048901/837")
                folium.Marker([51.019115, 14.748836], popup="Anna Magdalena Elisabeth Weiss. Stein: 15, Reihe: R2, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Benigna Schüz":
               st.subheader("Benigna Schüz")
               st.image("Gottesacker_Julius_Titz/S1R103.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766025684/140")
               folium.Marker([51.019103, 14.748604], popup="Benigna Schüz. Stein: 6, Reihe: R5, Feld: B3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Christa Dorothea Lintrup":
               st.subheader("Christa Dorothea Lintrup")
               st.image("Gottesacker_Julius_Titz/S1R83.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766034756/143")
               folium.Marker([51.019112, 14.748551], popup="Christa Dorothea Lintrup. Stein: 3, Reihe: R10, Feld: S1", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Dorothea Maria Ahlsleb":
               st.subheader("Dorothea Maria Ahlsleb")
               st.image("Gottesacker_Julius_Titz/20240525_154421.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/394")
               folium.Marker([51.019036, 14.748669], popup="Dorothea Maria Ahlsleb. Stein: 1, Reihe: R1, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Maria Luley":
               st.subheader("Maria Luley")
               st.image("Gottesacker_Julius_Titz/S3R47.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/628")
               folium.Marker([51.019057, 14.748774], popup="Maria Luley. Stein: 7, Reihe: R4, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Maria Magdalena Bezold":
               st.subheader("Maria Magdalena Bezold")
               st.image("Gottesacker_Julius_Titz/S3R411.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125816/180")
               folium.Marker([51.019082, 14.748807], popup="Maria Magdalena Bezold. Stein: 11, Reihe: R4, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Maria Magdalena Richter":
               st.subheader("Maria Magdalena Richter")
               st.image("Gottesacker_Julius_Titz/S1R813.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766115837/28") 
               folium.Marker([51.019203, 14.748634], popup="Maria Magdalena Richter. Stein: 3, Reihe: R8, Feld: S1", icon=folium.Icon(color='red')).add_to(m)
        
     elif option == "Mädgen Cornelia Louisa von Goldenberg":
               st.subheader("Mädgen Cornelia Louisa von Goldenberg")
               st.image("Gottesacker_Julius_Titz/S3R12.jpg", width=350, use_column_width="always", caption= "© Julius Titzt")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766125301/527") 
               folium.Marker([51.019050, 14.748683], popup="Mädgen Cornelia Louisa von Goldenberg. Stein: 2, Reihe: R1, Feld: S3", icon=folium.Icon(color='red')).add_to(m)
       
        
     elif option == "Gottfried Clemens":
               st.subheader("Gottfried Clemens")
               st.link_button("Digitalisat", "http://digital.slub-dresden.de/id1766148077/273") 
               folium.Marker([51.019578, 14.748048], popup="Gottfried Clemens. Stein: 25, Reihe: R5, Feld: B3").add_to(m)

          
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
    
    # Die gegebenen Daten
    
    words = [
       dict(text="Robinhood", value=16000, color="#b5de2b", country="US", industry="Cryptocurrency"),
       dict(text="Personio", value=8500, color="#b5de2b", country="DE", industry="Human Resources"),
       dict(text="Boohoo", value=6700, color="#b5de2b", country="UK", industry="Beauty"),
       dict(text="Deliveroo", value=13400, color="#b5de2b", country="UK", industry="Delivery"),
       dict(text="SumUp", value=8300, color="#b5de2b", country="UK", industry="Credit Cards"),
       dict(text="CureVac", value=12400, color="#b5de2b", country="DE", industry="BioPharma"),
       dict(text="Deezer", value=10300, color="#b5de2b", country="FR", industry="Music Streaming"),
       dict(text="Eurazeo", value=31, color="#b5de2b", country="FR", industry="Asset Management"),
       dict(text="Drift", value=6000, color="#b5de2b", country="US", industry="Marketing Automation"),
       dict(text="Twitch", value=4500, color="#b5de2b", country="US", industry="Social Media"),
       dict(text="Plaid", value=5600, color="#b5de2b", country="US", industry="FinTech"),
       ]
    # Extrahiere die Texte und Werte für die Wordcloud
    texts = [word['text'] for word in words]
    values = [word['value'] for word in words]
    
    # Erstelle die Wordcloud
    wordcloud_data = {texts[i]: values[i] for i in range(len(texts))}
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(wordcloud_data)
    
    # Streamlit-Anwendung
    st.title('Interactive Wordcloud')
    
    # Zeige die Wordcloud an
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()
    
    # Zeige zusätzliche Informationen
    st.subheader('Wordcloud Details:')
    for word in words:
            st.write(f"- **{word['text']}**: Mentions: {word['value']}, Country: {word['country']}, Industry: {word['industry']}")
