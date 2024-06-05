import streamlit as st
from streamlit_folium import st_folium
import folium
import streamlit.components.v1 as components
import json

st.set_page_config(page_title="Gottesacker Herrnhut", layout="wide")


# Seitenleiste mit Links zu verschiedenen Seiten erstellen
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Gehe zu", ["Gottesacker Herrnhut","Karte", "Hermann Reinhard Schick"])

# Seiteninhalt basierend auf der Auswahl des Benutzers aktualisieren
if selection == "Gottesacker Herrnhut":
     st.title("Gottesacker Herrnhut")
     st.write("Der Hutberg ist eng mit der Geschichte von Herrnhut verbunden. Im 18. Jahrhundert war die Gegend um Herrnhut arm und abgelegen, mit einem Basalthügel namens Hutberg im Nordosten. Das Dorf Berthelsdorf, am Fuß des Hügels gelegen, hatte während des Dreißigjährigen Krieges schwer gelitten. Das Gut Berthelsdorf war von wertlosem Wald umgeben.")
     #st.write("Der Zugang war wenig bekannt und der einzige Weg über die Herrenshut stellte einen unangenehmen Waldweg mit gefährlichen Stellen dar. Im Frühjahr 1722 fanden drei bedeutende Ereignisse statt, die den Beginn einer neuen Ära markierten. Am 19. Mai 1722 übernahm der fromme Reichsgraf Nikolaus Ludwig von Zinzendorf die Herrschaft über das Gut Berthelsdorf. Die erste Handlung des Grafen war die Wahl eines neuen Pfarrers für Berthelsdorf, Johann Andreas Rothe. Rothes Predigten zogen Gläubige aus der ganzen Region an und lösten eine Erweckungsbewegung aus.")
     #st.write("Die Lieder von Johann Andreas Rothe, einem evangelischen Christen, zeugen noch heute von seinem Zeugnis. Im Mai 1722 verließen Männer und Frauen ihre mährische Heimat, um auf dem Gut des jungen Grafen Zinzendorf eine Freistatt zu finden, in der sie ihren evangelischen Glauben ungehindert leben konnten. Am 8. Juni 1722 erreichten zwei Familien Neißer unter der Führung von Christian David Berthelsdorf. Der gräfliche Verwalter äußerte den Wunsch, die Fremden nicht im Dorf anzusiedeln, sondern auf der Herrenshut, um Verdienstmöglichkeiten zu schaffen.")
     #st.write("Am 17. Juni 1722 wurde der erste Baum zur Errichtung einer Siedlung auf dem Hutberg gefällt. Trotz der Sorgen einer mährischen Frau über die Versorgung in der Wüste sah Christian David die Erlaubnis, sich hier niederzulassen, als Antwort auf Gebete. Dies markierte den Beginn einer Reihe ähnlicher Einwanderergruppen in den kommenden Jahren. ")
     #st.write("Insgesamt fanden 306 mährische Männer und 268 Frauen am Hutberg eine neue Heimat. Zahlreiche Emigranten waren seit den Tagen der Gegenreformation aus Böhmen ausgewandert, doch ihre Spur ist größtenteils verloren gegangen. Unter dem Schutz eines frommen Standesherrn entstand hier versehentlich eine Emigrantenkolonie. Gott vereinte den Haufen durch eine neue Erweckung zu einer Gemeinde, die sich auf das Wort Gottes gründen und wie Jesus wandeln wollte.")
     #st.write("Eine Abendmahlsfeier in der Berthelsdorfer Kirche am 13. August 1727 markierte das Ende dieser Zeit. Seitdem nannten sie sich eine Brüdergemeine. Ein beliebtes Lied war Herz und Herz, vereint zusammen von Graf Zinzendorf.")
     st.write("USW.")

elif selection == "Karte":
     # die Karte auf der Webseite posten
    with st.container():
    
        st.title("Karte des Gottesackers Hernnhut")

    # Koordinaten für die Anfangsanzeige der Karte (zum Beispiel: Berlin)
        #start_coordinates = (51.019419, 14.748778)

    # Folium-Karte erstellen
       # my_map = folium.Map(location=start_coordinates, zoom_start=19)
        my_map = folium.Map(location=[51.019419, 14.748778], zoom_start=19)


    # Marker zur Karte hinzufügen (zum Beispiel: Brandenburger Tor)
        folium.Marker([51.019330, 14.748093], popup="Hermann Reinhard Schick, 1704-1771").add_to(my_map)


    # Den HTML-Code der Folium-Karte in Streamlit einbetten
    html = my_map._repr_html_()
    st.components.v1.html(html, width=725, height=600, scrolling=True)

    # Karte in Streamlit einbetten
    st_data = st_folium(my_map, width=725)
        
     # Den HTML-Code für die Folium-Karte in Streamlit einbetten
       # st.write(my_map._repr_html_(), unsafe_allow_html=True)
     
elif selection == "Hermann Reinhard Schick":
    st.title("Hermann Reinhard Schick")
    st.write("* 1704 - † 1771")

   




   


