# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sys

class miaplicacion(Gtk.Application):

    def do_activate(self):
        # create a Gtk Window belonging to the application itself
        # Creae una ventana GTK que pertenece a la misma aplicación
        ventana = Gtk.Window(application=self)
        # Pongo un título
        ventana.set_title("¡Bienvenidos a GNOME!")
        ventana.set_default_size(600,600)
        ventana.set_position(Gtk.WindowPosition.MOUSE)
        # activo o muestro la ventana
        ventana.show_all()

# crea una instancia de la clase miaplicacion
app = miaplicacion()
# ejecuto la misma pasando los argumentos sys.argv
exit_status = app.run(sys.argv)
# Sale de la aplicación leyendo el status de la misma.
sys.exit(exit_status)
