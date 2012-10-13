from Tkinter import  *                            # Importación del módulo tkinter
import  ttk                          # Importación de tkk específicamente para el uso de combobox y algunos botones
import  tkMessageBox as box          # Importación del módulo de mensajes de texto
from PIL     import  Image
from pyswip  import  Prolog


pr = Prolog()
pr.consult("Prueba.pl")
nuevasReglas = []


class Archivo:
    
    def __init__(self, texto):
        
        self.direccion = texto
        self.archivo = open(texto, "r+")

        
    def escribir(self, texto):
        
        if(self.archivo.cambio):
            
            self.archivo.open(self.direccion, "w")
            for i in self.datos:
                self.archivo.write(i+"\n")
        else:
            
            self.archivo.open(self.direccion, "a")
            for i in nuevasReglas:
                self.archivo.write(i+"\n")

                
    def leer(self):
        
        self.datos = self.archivo.readlines()
        self.archivo.close()

        
    def cerrar(self):
        
        self.archivo.close()

        
    def cambio(self):
        
        self.cambio = True


ar = Archivo("Prueba.pl")
ar.leer()
        

class VentanaMantenimiento:
    
    def __init__(self, ventana):

        self.varMantenimiento = IntVar()
        
        self.vent = Toplevel(ventana, height = 500, width = 500, bg = "white")
        self.img1 = PhotoImage(file = "ratatouillep.gif")
        self.label_imag1 = Label(self.vent, image = self.img1)
        self.label_imag1.img1 = self.img1
        self.label_imag1.pack(side='top', fill='both', expand='yes')

        self.label_titulo = Label(self.vent, text = "Restaurante Le Poulet", bg = "white", fg = "black", font = ("Helvetica", 15))
        self.label_titulo.place(x = 129, y = 15)

        self.label_mantenimiento = Label(self.vent, text = "Mantenimiento de datos", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.label_mantenimiento.place(x = 134, y = 40)

        self.label_tarea = Label(self.vent, text = "Elija la tarea que desea ejecutar", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.label_tarea.place(x = 190, y = 60)

        self.modo_insertar = Radiobutton(self.vent, text = "Insertar", variable = self.varMantenimiento, value = 1, bg = "white", font = ("Helvetica", 10), command = self.seleccionMantenimiento)
        self.modo_insertar.place(x = 260, y = 100)

        self.modo_borrar = Radiobutton(self.vent, text = "Borrar", variable = self.varMantenimiento, value = 2, bg = "white", font = ("Helvetica", 10), command = self.seleccionMantenimiento)
        self.modo_borrar.place(x = 380, y = 100)

        self.modo_actualizar = Radiobutton(self.vent, text = "Actualizar", variable = self.varMantenimiento, value = 3, bg = "white", font = ("Helvetica", 10), command = self.seleccionMantenimiento)
        self.modo_actualizar.place(x = 490, y = 100)

        self.fram = Frame(self.vent, height = 180, width = 350, bg = "gray")
        self.fram.place(x = 250,y = 140)

        self.label_nombre = Label(self.fram, text = "Nombre de la receta", bg = "gray", fg = "black", font = ("Helvetica", 8))
        self.label_nombre.place(x = 10, y = 10)

        self.entry_nombre = Entry(self.fram, bg = "white", width = 16)
        self.entry_nombre.place(x = 10, y = 30)

        self.label_autor = Label(self.fram, text = "Autor de la receta", bg = "gray", fg = "black", font = ("Helvetica", 8))
        self.label_autor.place(x = 10, y = 65)

        self.entry_autor = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
        self.entry_autor.place(x = 10, y = 85)

        self.label_estilo = Label(self.fram, text = "Estilo de la comida", bg = "gray", fg = "black", font = ("Helvetica", 8))
        self.label_estilo.place(x = 10, y = 120)

        self.entry_estilo = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
        self.entry_estilo.place(x = 10, y = 140)

        self.label_ingredientes = Label(self.fram, text = "Lista de ingredientes", bg = "gray", fg = "black", font = ("Helvetica", 8))
        self.label_ingredientes.place(x = 200, y = 10)

        self.entry_ingredientes = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
        self.entry_ingredientes.place(x = 200, y = 30)

        self.label_pasos = Label(self.fram, text = "Lista de pasos", bg = "gray", fg = "black", font = ("Helvetica", 8))
        self.label_pasos.place(x = 200, y = 65)

        self.entry_pasos = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
        self.entry_pasos.place(x = 200, y = 85)

        self.guardar = Button(self.vent, text = "Guardar", font = ("Helvetica", 10), command = self.ejecutarCambios)
        self.guardar.place(x = 365, y = 330)

        
    def ejecutarCambios(self):
        
        modo = self.varMantenimiento.get()
        
        if(modo==1):
            
            nombre = self.entry_nombre.get()
            autor = self.entry_autor.get()
            estilo = self.entry_estilo.get()
            ingredientes = self.entry_ingredientes.get()
            pasos = self.entry_pasos.get()
            print [nombre, autor, ingredientes, pasos, estilo]
            pr.assertz("receta({},{},{},{},{})".format(nombre, autor, estilo, ingredientes, pasos))
            print list(pr.query("receta({},{},{},{},{})".format(nombre, autor, estilo, ingredientes, pasos)))
            
        elif (modo==2):
            print "Borrar"
            
        elif (modo==3):
            print "Actualzar"
            
        else:
            print "Debe elegir un modo"
        
    
    def seleccionMantenimiento(self):
        
        if (self.varMantenimiento.get() == 2):
            
            self.entry_autor = Entry(self.fram, bg = "white", width = 16, state = DISABLED)
            self.entry_autor.place(x = 10, y = 85)
            self.entry_estilo = Entry(self.fram, bg = "white", width = 16, state = DISABLED)
            self.entry_estilo.place(x = 10, y = 140)
            self.entry_ingredientes = Entry(self.fram, bg = "white", width = 16, state = DISABLED)
            self.entry_ingredientes.place(x = 200, y = 30)
            self.entry_pasos = Entry(self.fram, bg = "white", width = 16, state = DISABLED)
            self.entry_pasos.place(x = 200, y = 85)
            
        else:
            
            self.entry_autor = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
            self.entry_autor.place(x = 10, y = 85)
            self.entry_estilo = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
            self.entry_estilo.place(x = 10, y = 140)
            self.entry_ingredientes = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
            self.entry_ingredientes.place(x = 200, y = 30)
            self.entry_pasos = Entry(self.fram, bg = "white", width = 16, state = NORMAL)
            self.entry_pasos.place(x = 200, y = 85)


class VentanaConsulta:

    def __init__(self, ventana):

        self.consulta = Toplevel(ventana, height = 500, width = 500, bg = "white")
        self.img1 = PhotoImage(file = "rata.gif")
        self.label_imag1 = Label(consulta, image = img1)
        self.label_imag1.img1 = img1
        self.label_imag1.pack(side='top', fill='both', expand='yes')


class VentanaPrincipal:

    def __init__(self):
        
        self.ventana()
        self.menu()
        self.fondo()
        self.labelsBotones()
        self.ventana_principal.mainloop()

    def ventana(self):
        
        self.ventana_principal = Tk() # Creación de la ventana principal
        self.ventana_principal.title("Restaurante Le Poulet") # Nombre de la ventana
        self.ventana_principal.geometry("600x450")

        self.ventana = Frame(self.ventana_principal, height = 1000, width = 1000, bg = "white") # Creación del contenedor de la aplicación
        self.ventana.pack() # Ubicación del frame en la ventana

    def menu(self):
        
        self.Barra = Menu(self.ventana_principal)

        self.Opciones = Menu(self.Barra, tearoff = 0) # Creación de la opción Mantenimiento en la barra de Menú
        self.Opciones.add_separator() # Separador implementado en la barra de menú
        self.Barra.add_cascade(label = "Archivo", menu = self.Opciones) # Implementación de la opción Mantenimiento en la barra

        self.Ayuda = Menu(self.Barra, tearoff = 0)

        self.Ayuda.add_command(label = "Manual de usuario")
        self.Ayuda.add_separator()
        self.Ayuda.add_command(label = "Acerca de...")

        self.Ayuda.add_command(label = "Salir", command = self.ventana_principal.destroy)

        self.Barra.add_cascade(label = "Ayuda", menu = self.Ayuda)
        self.ventana_principal.config(menu = self.Barra)

    def fondo(self):
        
        self.img1 = PhotoImage(file = "Portada.gif")
        self.label_imag1 = Label(self.ventana, image = self.img1)
        self.label_imag1.img1 = self.img1
        self.label_imag1.pack(side='top', fill='both', expand='yes')

        self.tit = Label(self.ventana, text = "¡Bienvenido al Restaurante Le Poulet!", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.tit.place(x = 150, y = 50)

        self.titu = Label(self.ventana, text = "Sírvase elegir el modo de acceso", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.titu.place(x = 160, y = 130)

    def labelsBotones(self):
        
        self.accesar = Button(self.ventana, text = "Ingresar", font = ("Helvetica", 10), command = self.ingresar)
        self.accesar.place(x = 215, y = 300)

        self.titulo = Label(self.ventana, text = "Restaurante Le Poulet", bg = "white", fg = "black", font = ("Helvetica", 20))
        self.titulo.place(x = 129, y = 15)

        self.varModo = IntVar()
        
        self.modo_mantenimiento = Radiobutton(self.ventana, text = "Mantenimiento", variable = self.varModo, value = 1, bg = "white", font = ("Helvetica", 10), command = self.seleccion)
        self.modo_mantenimiento.place(x = 200, y = 180)

        self.modo_consulta = Radiobutton(self.ventana, text = "Consulta", variable = self.varModo, value = 2, bg = "white", font = ("Helvetica", 10), command = self.seleccion)
        self.modo_consulta.place(x = 215, y = 225)


        self.Creditos = Label(self.ventana, text = "Restaurante Le Poulet - 2012", bg = "white", fg = "black", font = ("Helvetica", 9))
        self.Mas_Creditos = Label(self.ventana, text = "Derechos reservados © - Tecnológico de Costa Rica", bg = "white", fg = "black", font = ("Helvetica", 9))
        self.Creditos.place(x = 170, y = 405)
        self.Mas_Creditos.place(x = 90, y = 425)


    def seleccion(self):
        
        return self.varModo.get()


    def ingresar(self):     
        
        if self.seleccion() == 1:

            VentanaMantenimiento(self.ventana_principal)   
            
        elif self.seleccion() == 2:

            VentanaConsulta(self.ventana_principal) 

        else:
            
            box.showerror("Error", "Debe seleccionar un modo de acceso.")

            
VentanaPrincipal()









