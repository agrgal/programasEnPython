from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Grid Example", application=app)
        
        tope = 10
		
        # muchas etiquetas
        labels=[]
        for i in xrange(0,tope):
			for j in xrange(0,tope):
				labels.append(Gtk.Label(label="Etiqueta "+str(i)+":"+str(j)))


        # a grid
        grid = Gtk.Grid()

        # some space between the columns of the grid
        grid.set_column_spacing(5)

        # 
        for i in xrange(0,tope):
			for j in xrange(0,tope):
				grid.attach(labels[i+j*10],i,j,1,1)
        

        # add the grid to the window
        self.add(grid)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
