# -*- coding: utf-8 -*-
from gi.repository import Gtk
import sys

"""
#Poner una etiqueta como clase
class  mietiqueta(Gtk.Label):
	
	def __init__(self):
		Gtk.Label.__init__(self)
		self.set_text("¡Hola, soy una etiqueta con clase")"""

# Una ApplicationWindow GTK
class miventana(Gtk.ApplicationWindow):
    # Constructor de ApplicationWindow

    def __init__(self,app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        # también puede venir aquí win.show_all()
        self.set_default_size(100,100)
        
        # Quitar este ejemplo si se quiere 
        # comprobar como se hace con una clase
        # =======================
        # Otra etiqueta sin clase
        # =======================
        label2 = Gtk.Label()
        label2 = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)
        self.add(label2)
        # =======================

class miaplicacion(Gtk.Application):
    
    # Constructor de Gtk.Application
    def __init__(self):
        Gtk.Application.__init__(self)

    # al activarse la aplicación, crea un objeto miventana.
    # Paso la aplicación "self" como argumento.
    def do_activate(self):
        win = miventana(self)
        # añade la imagen
        """ win.add(mietiqueta()) """
        # Muestra la ventana
        win.show_all()

    # hacer un startup
    def do_startup(self):
        Gtk.Application.do_startup(self)

# al igual que antes se crea y se ejecuta la aplicación
app = miaplicacion()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
