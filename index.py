import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'traceroute'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('sample_icon.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    indicator.set_title('traceroute')
    gtk.main()

def traceroute(source):

    win = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
    win.set_border_width(12)
    win.set_resizable(False)

    # win.connect("delete-event", Gtk.main_quit)
    # button = Gtk.Button(label="Click Here")
    # button.connect("clicked", self.on_button_clicked)
    # win.add(button)
    # win.show_all()


def build_menu(self):
    menu = gtk.Menu()
    #traceroute
    item_traceroute = gtk.MenuItem('Trace route')
    item_traceroute.connect("activate", traceroute, None)
    menu.append(item_traceroute)

    #separator
    item_separator = gtk.SeparatorMenuItem()
    menu.append(item_separator)

    #Quit
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
