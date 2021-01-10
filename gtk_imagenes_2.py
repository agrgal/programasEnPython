# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sys

# Una ApplicationWindow GTK

class miventana(Gtk.ApplicationWindow):
    # Constructor de ApplicationWindow

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        # también puede venir aquí win.show_all()
        self.set_default_size(800,800)
		
		# Crear una imagen
        image = Gtk.Image()
        # Obtenerla desde un fichero
        image.set_from_file("coche.png")
        # añadirla a la ventana.
        self.add(image)

class miaplicacion(Gtk.Application):
    
    # Constructor de Gtk.Application
    def __init__(self):
        Gtk.Application.__init__(self)

    # al activarse la aplicación, crea un objeto miventana.
    # Paso la aplicación "self" como argumento.
    def do_activate(self):
        win = miventana(self)
        # Muestra la ventana
        win.show_all()

    # hacer un startup
    def do_startup(self):
        Gtk.Application.do_startup(self)

# al igual que antes se crea y se ejecuta la aplicación
app = miaplicacion()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
