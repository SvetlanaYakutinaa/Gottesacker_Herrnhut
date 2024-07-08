import streamlit as st
import folium
from streamlit.components.v1 import html
import branca
import streamlit.components.v1 as components
import os


#Erstellung Webseite
st.set_page_config(page_title="Gottesacker Herrnhut", layout="wide")

# Erstellung einer Seitenleiste mit Links zu verschiedenen Seiten 
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Gehen Sie zu", ["Digitaler Gottesacker", "Analyse"])

###################### Seite "Digitaler Gottesacker"

if selection == "Digitaler Gottesacker":
     
     #################### Siedebar

     add_selectbox = st.sidebar.radio(
        "Dateiformat auswählen und Namensliste erhalten",
        ("Digitalisat", "Text und XML"),
        index=None
    )

     if add_selectbox == "Digitalisat":
            names_d = ["Knud Andersen", "Hans Hansen", "Herrmann Reinhard Schick", "Gottfried Clemens", 
            "Johann Sebald Ringmacher", "Abraham Dürninger", "Benigna Schüz", 
            "Christa Dorothea Lintrupin", "Maria Magdalena Richter", 
            "Anna Magdalena Elisabeth Weiss", "Dorothea Maria Ahlsleb", 
            "Mädgen Cornelia Louisa von Goldenberg", "Maria Luley", "Maria Magdalena Bezold"]
            for name in names_d:
                    st.sidebar.write(name)
     elif add_selectbox == "Text und XML":
             names_a = ["Herrmann Reinhard Schick", "Anna Magdalena Elisabeth Weiss", "Knud Andersen", "Christa Dorothea Lintrupin", "Maria Magdalena Richter", "Gottfried Clemens", "Johann Sebald Ringmacher", "Benigna Schüz"]
             for name in names_a:
                     st.sidebar.write(name)
                  
################################## 
                     
     with st.container():
        
        st.title("Gottesacker Herrnhut")
        
        # Koordinaten für die Anfangsanzeige der Karte
        start_coordinates = (51.019419, 14.748778)
        m = folium.Map(location=start_coordinates, zoom_start=18)
        
        if 'visibility' not in st.session_state:
               st.session_state.visibility = "visible"
               
        if 'disabled' not in st.session_state:
               st.session_state.disabled = False

############################## Inhalt
        st.write("Text")

        st.image("plan_gottesacker_hrrh.jpeg", caption= "Abbild 1: Plan des Gottesackers Herrnhut, 1822")
        st.link_button("Quelle", "https://digital.staatsbibliothek-berlin.de/werkansicht?PPN=PPN657385352&PHYSID=PHYS_0115&DMDID=")
        st.Links("Quelle", "https://digital.staatsbibliothek-berlin.de/werkansicht?PPN=PPN657385352&PHYSID=PHYS_0115&DMDID=")
############################## Kodierung von Auswahlmöglichkeit von Personen und ihrem Inhalt
                
     option = st.selectbox( 
             "Wählen Sie bitte einen Name aus",
               ("Knud Andersen", "Hans Hansen", "Herrmann Reinhard Schick", "Gottfried Clemens", 
            "Johann Sebald Ringmacher", "Abraham Dürninger", "Benigna Schüz", 
            "Christa Dorothea Lintrupin", "Maria Magdalena Richter", 
            "Anna Magdalena Elisabeth Weiss", "Dorothea Maria Ahlsleb", 
            "Mädgen Cornelia Louisa von Goldenberg", "Maria Luley", "Maria Magdalena Bezold"),
        index = None,
        placeholder = "Wählen Sie einen Name aus",
               label_visibility=st.session_state.visibility,
               disabled=st.session_state.disabled,
               )
     
     #################################### Personen und Inhalt

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
                with open("Text/männlich/02490.txt", "rb") as file:
                        btnn = st.download_button(
                               label="Download Text",
                               data= file,
                               file_name="02490.txt"
                       )
                with open("XML/02490.xml", "rb") as file:
                       btn = st.download_button(
                               label="Download XML",
                               data= file,
                               file_name="02490.xml"
                       ) 
                folium.Marker([51.019360, 14.748201], popup="Herrmann Reinhard Schick. Stein: 10, Reihe: R7, Feld: B1").add_to(m)

################################   Kartevisualisierung 
                   
     # Speichere die Karte in einer HTML-Datei
     m.save("map.html")

     # Lese die HTML-Datei und zeige sie in Streamlit an
     with open("map.html", "r", encoding="utf-8") as f:
            map_html = f.read()

     # Zeige die HTML-Karte in der Streamlit-Anwendung
     st.components.v1.html(map_html, height=500)

############################## Kodierung der Seite "Analyse"
# die Analyse wurde in den separaten Jupyter - Notebooks durchgefürt
# Notebooks sind im Repositorium zugänglich
          
elif selection == "Analyse":
    st.title("Analyse") 
    
    st.write("""Die folgende Analyse untersucht die Lebensbeschreibungen von acht Mitgliedern der Herrnhuter Brüdergemeine. 
             Es handelt sich um vier Frauen und vier Männer. Die Texte stammen aus den Jahren 1770 bis 1806 und wurden nach 
             dem Zufallsprinzip für die Analyse ausgewählt.""")
    st.write ("""Zunächst wurden die Digitalisate mit dem Tool eScriptorium 
             transkribiert und die Texte normalisiert, um eine konsistente Analyse zu ermöglichen. 
             Die Analyse wurde mit Hilfe von Python-Skripten durchgeführt und sollte die Frage beantworten: Wie unterscheiden 
             sich die Lebensbeschreibungen von Männern und Frauen in Bezug auf Textlänge, Satzlänge, häufigste Wörter/Wortarten und Inhalt.
             """)
    st.write("""Die häufigsten Wörter in den Lebensbeschreibungen wurden analysiert und in Form einer Wortwolke visualisiert (Abb. 1 und 2).
             Zunächst wurde eine Liste von häufig vorkommenden Wörtern erstellt, die keine signifikante Information enthalten 
             (z.B.: ja, weil, was, wo, derselbe usw.) und aus der Analyse ausgeschlossen. Dies ermöglichte es, sich auf die für 
             den Inhalt relevanten Wörter zu konzentrieren. Die Visualisierung wurde für die Texte von Frauen und Männern getrennt
             erstellt, wobei Wörter, die mindestens dreimal in den Texten vorkamen, in die Wortwolke aufgenommen wurden. 
             Die einzelnen Wörter wurden je nach Häufigkeit unterschiedlich groß dargestellt.""")
    
    st.image('Output/wordcloud_w.png', caption='Abbild 1: WordCloud von Frauen')
    
    st.image('Output/wordcloud_m.png', caption='Abbild 2: WordCloud von Männern')

    st.write("""Da die AutorInnen von Lebensbeschreibungen stark auf ihre eigenen Erfahrungen
              und ihr eigenes Leben fokussiert sind, findet sich in den Texten häufig der Gebrauch von Pronomina 
             (vgl. Abb. 1 und 2). Sowohl männliche als auch weibliche AutorInnen sprechen oft über Gott,
              den Heiland und Herrnhut. Dies weist auf die Textsorte und den Glauben als zentralen Bestandteil ihres Lebens hin.
              """)
    st.write("""Männliche Autoren berichten besonders häufig über ihre Reiseerfahrungen,
              was sich in der Verwendung von Begriffen wie "Reisen" oder "Reise" widerspiegelt.
              Zudem finden sich in den männlichen Texten häufig Berichte über ihre Bildungserfahrungen 
             (vgl. Abb. 2). Frauen hingegen thematisieren häufig Kinder und soziale Aktivitäten wie den Chor (vgl. Abb. 1).""")
    
    st.write("Abbild 3 veranschaulicht den Vergleich der Worthäufigkeit zwischen Männern und Frauen.")

    st.image('Output/grafik.png', caption='Abbild 3: Häufigkeit der Top 50 Lemmata (Männer vs. Frauen)')

    st.write("""Die durchschnittliche Textlänge (Abb. 4) der von uns 
             transkribierten und untersuchten Lebensbeschreibungen
              unterscheidet sich signifikant zwischen den Geschlechtern. 
             Während die Texte von Frauen im Durchschnitt etwas weniger als 
             900 Wörter aufweisen, sind die Texte der Männer mit ca. 2100 
             Wörtern mehr als 2x so lang. Diese Ergebnisse sind keineswegs 
             repräsentativ für die Gesamtheit der Lebensbeschreibungen, eine 
             klare Tendenz ist in unserer zufällig ausgewählten Stichprobe von 
             acht Texten jedoch erkennbar. Während zwei von Männern verfasste Texte mehr als 2500 Wörter umfassen, 
             beinhaltet der längste Text einer Frau nur etwas mehr als 1000 Wörter.
 """)

    st.image ("Output/textlänge.png", caption="Abbild 4: Durchschnittliche Textlänge")

    st.write("""Interessanterweise  zeigt sich ein ganz ähnliches Diagramm auch bei der durchschnittlichen Satzlänge.
              Obwohl ein kürzerer Text nicht zwingend mit kürzeren durchschnittlichen Sätzen korrelieren müsste, sind 
             auch hier die durchschnittlichen Sätze der Männer mit 108 Wörtern etwa 2,5 mal so lang wie die Sätze der Frauentexte mit 38 Wörtern.""")

    st.image("Output/satzlänge.png", caption= "Abbild 5: Durchschnittliche Satzlänge")

    st.write("""Insgesamt verwenden Männer und Frauen in unserer Stichprobe ähnlich häufig die verschiedenen Wortarten (Abb. 6). 
             Es gibt jedoch ein paar Ausnahmen. Deutlich häufiger als Männer verwenden Frauen Pronomina. Vorherrschend sind 
             hier “ich”, “sie”, “ihr” und “mir”, wie auch in der Wortwolke (Abb. 1 und 2) erkennbar ist. 
             Ebenfalls etwas häufiger kommen in den weiblichen Texten Hilfsverben vor. Bei den von Männern 
             verfassten Texten kommen dagegen häufiger Eigennamen vor.""")

    st.image("Output/POS.png", caption= "Abbild 6: Relative Häufigkeit der verschiedenen Wortarten (Männer vs. Frauen)")



