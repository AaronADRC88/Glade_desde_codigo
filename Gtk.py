from gi.repository import Gtk

class ExemploBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Exemplo de Box")
        self.caixa =Gtk.Box(spacing=6)
        self.caixa.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.caixa)

        self.caixa_inter =Gtk.Box(spacing=6)
        self.caixa.add(self.caixa_inter)

        self.boton1=Gtk.Button(label="Ola")
        self.boton1.connect("clicked",self.on_boton1_clicked)
        self.caixa_inter.pack_end(self.boton1,False,False,3)
        """de esquerda a dereita co pack start
        self.caixa.pack_start(self.boton1,True,True,3)
        """
        self.boton2=Gtk.Button(label="Adeus")
        self.boton2.connect("clicked",self.on_boton2_clicked)
        self.caixa_inter.pack_end(self.boton2,False,False,3)

        self.label=Gtk.Label()
        self.caixa.pack_start(self.label,False,False,3)

    def on_boton1_clicked(self,control):
        print("lolololololololololololololo")
        self.label.set_text("ola")
    def on_boton2_clicked(self,widget):
        print("ratatatatataratatatata")
        self.label.set_text("adeus")

fiestra=ExemploBox()
fiestra.connect("delete-event",Gtk.main_quit)
fiestra.set_position(Gtk.WindowPosition.CENTER)
fiestra.set_default_size(100,200)
fiestra.set_resizable(False)
fiestra.show_all()

Gtk.main()