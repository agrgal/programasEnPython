# coding: utf-8
from gi.repository import Gtk
import sys


class miventana(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Ejemplo de scroll", application=app)
        self.set_default_size(5, 5)

        # La ventana con scroll
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)
        #política de scroll: que siempre aparezca
        scrolled_window.set_policy(
            Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)

        # una imagen más grande que la ventana
        image = Gtk.Image()
        image.set_from_file("coche.png")

        # la añade a la ventana con scroll
        scrolled_window.add_with_viewport(image)

        # y la ventana con scroll a la ventana en sí
        self.add(scrolled_window)


class miaplicacion(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = miventana(self)
        win.show_all()

app = miaplicacion()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
