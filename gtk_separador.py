# coding: utf-8
from gi.repository import Gtk
import sys


class miventana(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Ejemplo de separador", application=app)

        # Las etiquetas
        label1 = Gtk.Label()
        label1.set_text("Abajo, un separador horizontal.")

        label2 = Gtk.Label()
        label2.set_text("A la derecha, un separador vertical.")

        label3 = Gtk.Label()
        label3.set_text("A la izquierda, un separador vertical")

        # separador horizontal		
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        # separador vertical
        vseparator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)

        # una rejilla donde incrustar los separadores
        grid = Gtk.Grid()
        grid.attach(label1, 0, 0, 3, 1)
        grid.attach(hseparator, 0, 1, 3, 1)
        grid.attach(label2, 0, 2, 1, 1)
        grid.attach(vseparator, 1, 2, 1, 1)
        grid.attach(label3, 2, 2, 1, 1)
        grid.set_column_homogeneous(True)
        # añado a la ventana la rejilla.
        self.add(grid)


class miaplicacion(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = miventana(self)
        win.show_all()

app = miaplicacion()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
