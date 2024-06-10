import streamlit as st
import folium
from streamlit.components.v1 import html
import pandas as pd
import streamlit_pandas as sp 

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
          html(map_html, height=500)


elif selection == "Analyse":
     st.title ("In Arbeit")
  
     file = "top_words.csv"
     df = pd.read_csv(file)
    
    # Erstelle Widgets für die Interaktion
     all_widgets = sp.create_widgets(df)
    
    # Wende Filter auf den DataFrame an
     res = sp.filter_df(df, all_widgets)
    
    # Zeige den Original-DataFrame an
     st.header("Original DataFrame")
     st.write(df)

    # Zeige den gefilterten DataFrame an
     st.header("Result DataFrame")
     st.write(res)