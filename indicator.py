import googlemaps
import json
import gobject
import gtk
import appindicator
import os, sys
from datetime import datetime

arquivo = open('arquivo.txt', 'r')
origin = arquivo.readline()
destination  = arquivo.readline()
# print(origin)
# print(destination)
arquivo.close()

gmaps = googlemaps.Client(key='AIzaSyCENWT_Xz8fFvtPWl1XQ-IbdI1M2KCmD-M')

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.distance_matrix(origin,
                                     destination,
                                     mode="driving",
                                     departure_time=now)

# print(json.dumps(directions_result, indent=2))

# driving_time = directions_result["rows"][0]["elements"][0]["duration"]["value"]
driving_time_text = directions_result["rows"][0]["elements"][0]["duration"]["text"]
# print(driving_time)

class SampleIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator("sample-ind", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("indicator-messages-new")
        self.ind.set_label(str(driving_time_text));

        # Create and populate GTK Menu
        self.menu = gtk.Menu()
        quit_item = gtk.MenuItem("Quit")
        quit_item.connect("activate", self.quit)
        quit_item.show()
        self.menu.append(quit_item)

        self.menu.show()

        self.ind.set_menu(self.menu)

    def quit(self, widget):
        gtk.main_quit()

    def clicked(self, widget):
        print "Item selected"

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    indicator = SampleIndicator()
    main()
