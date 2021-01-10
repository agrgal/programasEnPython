# -*- coding: utf-8 -*-
from gi.repository import Gtk
from gi.repository import GdkPixbuf
import sys

class miventana(Gtk.ApplicationWindow):
	# create a window
	def __init__(self, app):
		Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
		self.set_default_size(300, 300)

		# create a pixbuf from file filename="gnome-image.png", with width=32
		# and height=64 amd boolean preserve_aspect_ratio=False.
		pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("coche.png", 200, 128, True)

		# create an image
		image = Gtk.Image()
		# set the content of the image as the pixbuf
		image.set_from_pixbuf(pixbuf)
		# add the image to the window
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
