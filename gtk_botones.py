# coding: utf-8
from gi.repository import Gtk
import sys, random


class miventana(Gtk.ApplicationWindow):

	def __init__(self, app):
		Gtk.Window.__init__(self, title="Ejemplo con botones", application=app)
		self.set_default_size(450, 350)
		self.set_border_width(10)

		#2.- definir objetos separadores, y las imágenes
		sepHorizontal = []
		imagen = []
		chbtn = [] # checkbuttons
		for i in xrange(0,3):
			sepHorizontal.append(Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL))
			imagen.append(Gtk.Image())
			imagen[i].set_from_file("bombilla_off.png")
			chbtn.append(Gtk.CheckButton())
			chbtn[i].set_label("Botón nº "+str(i+1))
			chbtn[i].set_active(False)
			chbtn[i].connect("toggled", self.si_check, i, imagen)
		rdbtn1 = Gtk.RadioButton(label="Botón nº 1")
		rdbtn1.connect("toggled",self.si_rdcheck, imagen)
		rdbtn1.set_active(False)
		rdbtn2 = Gtk.RadioButton.new_from_widget(rdbtn1)
		rdbtn2.set_label("Botón nº 2")
		rdbtn2.connect("toggled",self.si_rdcheck, imagen)
		rdbtn2.set_active(False)
		rdbtn3 = Gtk.RadioButton.new_with_label_from_widget(rdbtn1, "Botón nº 3")
		rdbtn3.connect("toggled",self.si_rdcheck, imagen)
		rdbtn3.set_active(False)

		# 4.- Un toggle - button para encenderlos a todos
		tglbtn = Gtk.ToggleButton(label="Enciende")
		tglbtn.set_active(False)
		tglbtn.connect("toggled",self.tglconnect, imagen)
		# 5.- Un interruptor, que enciende aleatoriamente una de ellas
		sw = Gtk.Switch()
		sw.connect("notify::active", self.swconnect, imagen)
		# 6.- Y se me olvida..., ¡un botón normal...!
		icono = Gtk.Image() # un objeto imagen nuevo
		icono.set_from_file("bombilla_on.png") # una imagen del almacén
		btn = Gtk.Button()
		btn.set_image(icono)
		# btn.set_label("Todas")
		btn.connect("clicked",self.conectar,imagen)
		# 7.- Link Buttón
		enlace = Gtk.LinkButton(uri="https://es.wikipedia.org/wiki/Digital")
		enlace.set_label("Enlace a una web")
		#1.- definir objeto rejilla
		rejilla = Gtk.Grid()
		rejilla.set_column_spacing(20)
		#3.- definir los grid attach
		for i in xrange(0,3):
			rejilla.attach(imagen[i],i,0,1,1)
		rejilla.attach(sepHorizontal[0],0,1,3,1) # una separación
		for i in xrange(0,3):
			rejilla.attach(chbtn[i],i,2,1,1) # check buttons
		rejilla.attach(sepHorizontal[1],0,3,3,1) # una separación
		rejilla.attach(rdbtn1,0,4,1,1)
		rejilla.attach(rdbtn2,1,4,1,1)
		rejilla.attach(rdbtn3,2,4,1,1)
		rejilla.attach(sepHorizontal[2],0,5,3,1) # una separación
		rejilla.attach(tglbtn,0,6,1,1) # toggle
		rejilla.attach(sw,1,6,1,1) # switch
		rejilla.attach(btn,2,6,1,1) # botón normal
		rejilla.attach(enlace,0,7,3,1) # enlace		
		rejilla.set_column_homogeneous(True) # para centrar los objetos en la columna
		rejilla.set_row_homogeneous(True) # para centrar los objetos en las filas
		self.add(rejilla)

		# =================================================================
		# Funciones de llamada
		# =================================================================
    
	# llamada si activan/desactivan los checkbuttons    
	def si_check(self, button, i, imagen):
	# importante, pasarle la lista imagen...
		if button.get_active():
			print "Encendido", i
			imagen[i].set_from_file("bombilla_on.png")
		else:
			print "Apagado", i
			imagen[i].set_from_file("bombilla_off.png")

	# llamada si activan/desactivan los radiobuttons   
	def si_rdcheck(self, button, imagen):
		if button.get_active(): # la que está activa
			valor = button.get_label()
			k = int(valor[-1])
			self.borrar(imagen) # borra el resto de imágenes
			imagen[k-1].set_from_file("bombilla_on.png")   

	def tglconnect(self, button, imagen):
		if button.get_active():
			button.set_label("Apaga")
			self.todos(imagen)
		else:
			button.set_label("Enciende")
			self.borrar(imagen)
    
	def swconnect(self, button, active, imagen): 
		# switch button pasa ya tres atributos self, button y active
		i = random.randint(0,2)
		# print i, button.get_active()
		self.borrar(imagen)
		if button.get_active():
			imagen[i].set_from_file("bombilla_on.png")

	def conectar(self,button,imagen):
		self.todos(imagen)

	# =================================================================
	# Otras llamadas
	# =================================================================

	def borrar(self, imagen):
		for i in xrange(0,3):
			imagen[i].set_from_file("bombilla_off.png")

	def todos(self, imagen):
		for i in xrange(0,3):
			imagen[i].set_from_file("bombilla_on.png")

# =================================================================
# Mi aplicación
# =================================================================

class miaplicacion(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = miventana(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = miaplicacion()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
