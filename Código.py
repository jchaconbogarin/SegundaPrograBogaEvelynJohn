# -*- coding: utf-8 -*-
from Tkinter import * # Importación del módulo tkinter
import ttk # Importación de tkk específicamente para el uso de combobox y algunos botones
import tkMessageBox as box # Importación del módulo de mensajes de texto
from PIL import Image
from pyswip import Prolog

##Definición de la clase ManejoProlog.
##Se encarga de manejar el código de Prolog y de actualizar la base de conocimientos cada vez que hay algún cambio.

class ManejoProlog:
    

    #Definición de la función constructora.
    #E: dirección del código de prolog.
    #S: ninguna
    #R: ninguna
    def __init__(self, texto):

        try:                                                            #Validación de que archivo exista.
            
            archivo = open(texto, "r")
            archivo.close
            self.direccion = texto                                      #Se define el atributo con la dirección del código de prolog.
            self.cargarConocimientos()                                  #Se cargan los conocimientos del código.
            self.error = False

            
        except:
            
            archivo = open("Recetas.pl", "w")                           #Creación de uno nuevo.
            archivo.close()
            self.direccion = "Recetas.pl"                               #Se define el atributo con la dirección del código de prolog.
            self.cargarConocimientos()                                  #Se cargan los conocimientos del código.
            self.error = True

    
    #Definición de la función que crea una nueva regla.
    #E: texto con el código de prolog.
    #S: ninguna
    #R: ninguna(método llamado internamente)
    def nuevaRegla(self, texto):

        archivo = open(self.direccion, "a")
        archivo.write('\n' + texto + '.')
        archivo.close()
        self.cargarConocimientos()
        

    #Definición de la función que lee el código de prolog y carga cada línea en una lista
    #E: ninguna.
    #S: lista con cada línea del código fuente de prolog.
    #R: ninguna.
    def leer(self):

        archivo = open(self.direccion, "r")
        lineas = archivo.readlines()
        archivo.close()
        return lineas


    #Función que borra una receta.
    #E: nombre de la receta por borrar.
    #S: ninguna.
    #R: ninguna.
    def borrarReceta(self, receta):

        lineas = self.leer()
        contador = 0
        
        for i in lineas:                                                #Se recorre el código de prolog en busca de la receta.
            
            if (i.startswith("receta("+receta+",")):                    #Se verifica que la receta sea igual a la ingresada.
                
                lineas.pop(contador)                                    #Se elimina de la lista
                contador += 1
                
            else:
                
                contador += 1
                
        archivo = open(self.direccion, "w")                             #Se reescribe el archivo con la receta eliminada.
        
        for i in lineas:
            
            archivo.write(i)
            
        archivo.close()
        self.cargarConocimientos()
        box.showinfo("Éxito", "La receta se ha borrado con éxito.")


    #Función que actualiza alguna receta.
    #E: lista con las posiciones a modificar y todos los datos de la receta (dato vacío si no se va a modificar y nombre de la receta siempre estará).
        #Ejemplo:
        #         Se tiene una receta(pizza, giovanni, italiana, queso, calentar)
        #         Se desea cambiar solamente el dato de 'giovanni'(autor) y 'queso'(ingredientes) por 'giussepe' y 'jamón'.
        #         Los datos de entrada serían: posiciones = [1,3], datos = ['pizza', 'giussepe', '', 'jamon', '']
    #S: ninguna.
    #R: ninguna.
    def actualizarReceta(self, posiciones, datos):

        lineas = self.leer()
        contador = 0
        
        for i in lineas:                                                #Se recorre el código de prolog en busca de la receta a actualizar
            
            if (i.startswith("receta("+datos[0]+",")):                  #Se verifica que la receta sea igual a la que se desee cambiar
                
                lineas[contador] = self.actualizarReceta_aux(posiciones, datos, i[7:])  #Se sustituye la línea con el resultado de la función auxiliar.
                contador += 1
                
            else:
                
                contador += 1
                
        archivo = open(self.direccion, "w")                             #Se reescribe el archivo con los nuevos datos.
        
        for i in lineas:
            
            archivo.write(i)
            
        archivo.close()
        self.cargarConocimientos()
        box.showinfo("Éxito", "La receta se ha borrado con éxito.")


    #Función auxiliar que se encarga de actualizar los datos.
    #E: lista de las posiciones por modificar, datos por cambiar, datos originales.
        #Continuando el ejemplo:
                #datos = ['pizza', 'giussepe', '', 'jamon', '']
                #posiciones = [1,3]
                #original = 'pizza, giovanni, italiana, queso, calentar'
    #S: línea de código prolog con los nuevos valores.
    #R: ninguna.
    def actualizarReceta_aux(self, posiciones, datos, original):

        separacion = original.split(",")                                #Se hace una lista con los datos viejos. Continuando el ejemplo anterior:
                                                                                #Se obtiene separacion =  ['pizza', 'giovanni', 'italiana', 'queso', 'calentar']  (DATOS ORIGINALES)                                      
        for i in posiciones:                                            #Se recorre la lista con las posiciones de la lista separacion por cambiar.
            separacion[i] = datos[i]                                    #Se cambia la posición obtenida en la lista posiciones, con la misma posición de la lista datos.
                                                                                #Se cambiaría la posición separacion[1] = datos[1] ('giussepe') y luego separacion[3] = datos[3] ('jamon')
        return "receta({},{},{},{},{}).\n".format(separacion[0], separacion[1], separacion[2], separacion[3], separacion[4])
                                                                        #Se retorna la nueva línea de código prolog.

    #Función que se encarga de cargar los conocimientos.
    #E: ninguna.
    #S: código prolog cargado.
    #R: ninguna.
    def cargarConocimientos(self):
        
        self.prolog = None                                              #Se elimina la base de conocimientos anterior
        self.prolog = Prolog()                                          #Se abre nuevamente prolog
        self.prolog.consult(self.direccion)                             #Se carga el código con la dirección obtenida anteriormente
    


#Definición de la clase VentanaMantenimiento.
#Ventana en la que se tienen todas las opciones de mantenimiento.

class VentanaMantenimiento:

    #Se define el método constructor.
    #E: root original
    #S: interfaz del método mantenimiento.
    #R: niguna
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

    
    #Función que se encarga de ejecutar los cambios
    #E: ninguna
    #S: ninguna
    #R: ninguna
    def ejecutarCambios(self):
        
        modo = self.varMantenimiento.get()                                          #Se obtiene la variable que indica la acción de método deseada.

        #Se obtienen los datos de los entrys (.get())
        #Se hacen todos los caracteres minúsculas(.lower() -Prolog interpreta mayúsculas como variables-)
        #Se le quitan los espacios al inicio y al final (.strip() -Prolog presenta error al involucrarlos-)
        #Se le reemplazan los espacios por "_" (.replace() -Prolog rechaza los espacios-)
        
        nombre = self.entry_nombre.get().lower().strip().replace(" ", "_")
        autor = self.entry_autor.get().lower().strip().replace(" ", "_")
        estilo = self.entry_estilo.get().lower().strip().replace(" ", "_")
        ingredientes = self.entry_ingredientes.get().lower().strip().replace(" ", "_")
        pasos = self.entry_pasos.get().lower().strip().replace(" ", "_")

        #Modo 1 => Inserción de nueva receta.
        if(modo==1):
            
            validacion = self.validaciones(nombre, autor, estilo, ingredientes, pasos)  #Se validan los datos. Función explicada abajo.

            if (validacion[0]):                                                         #Se obtiene el valor de retorno de validacion
                
                box.showerror("Error de datos", validacion[1])                          #Muestra el error con su mensaje.
                
            else:
                
                pr.nuevaRegla(validacion[1])                                            #Se agrega la receta.
                box.showinfo("Informacion", "La receta se ha creado con exito")         #Muestra mensaje de éxito.


        #Modo 2 => Borrado de receta
        elif (modo==2):
            
            if (nombre == ""):                                                          #Validación de que el usuario ingresó datos correctamente.

                box.showerror("Error", "Debe ingresar un nombre.")
            
            elif (list(pr.prolog.query("receta("+nombre+",W,X,Y,Z)")) == []):           #Validación de que la receta exista en la base de conocimientos.
                
                box.showerror("Error", "La receta que está intentando borrar no existe.")
                
            else:
                pr.borrarReceta(nombre)                                                 #Borrado de la receta.


        #Modo 3 => Actualización de receta
        elif (modo==3):

            datosActualizar = []                                                        #Se hace una lista con las posiciones a actualizar.
            
            if(nombre == ""):                                                           #Se valida que el usuario digitó el nombre de una receta.

                box.showerror("Error", "El nombre de la receta es necesario para poder actualizar")

            elif (list(pr.prolog.query("receta("+nombre+",W,X,Y,Z)")) == []):           #Validación de que la receta exista en la base de conocimientos.
                
                box.showerror("Error", "La receta que está intentando borrar no existe.")

            else:

                if(autor != ""):
                    datosActualizar.append(1)                                           #Se insertan las posiciones a actualizar.

                if(estilo != ""):

                    datosActualizar.append(2)

                if(ingredientes != ""):

                    datosActualizar.append(3)

                if(pasos != ""):

                    datosActualizar.append(4)

                pr.actualizarReceta(datosActualizar, [nombre, autor, estilo, ingredientes, pasos])
            
        else:
            
            box.showerror("Validaciones", "Debe elegir un modo para ejecutar una tarea.")
            

    #Función que valida los datos ingresados.
    #E: Datos ingresados
    #S: Lista con dos elementos. El primero corresponde a booleano indicando si los datos son válidos(False) o si son inválidos(True).
    #   El segundo elemento corresponde al mensaje de error específico o el código de prolog formado.
    #R: Datos no pueden iniciar con número ni con "_" ni estar vacíos.
    def validaciones(self, nombre, autor, estilo, ingredientes, pasos):

        receta = "receta({},{},{},{},{})".format(nombre, autor, estilo, ingredientes, pasos)
        
        if(nombre == "" or autor == "" or estilo == "" or ingredientes == "" or pasos == ""):

            return [True, "Todos los campos son requeridos."]

        elif(nombre[0].isdigit() or autor[0].isdigit() or estilo[0].isdigit() or ingredientes[0].isdigit() or pasos[0].isdigit()
            or nombre[0] == "_" or autor[0] == "_" or estilo[0] == "_" or ingredientes[0] == "_" or pasos[0] == "_"):

            return [True, "Los datos no pueden iniciar con números ni el caracter \"_\"."]

        elif (list(pr.prolog.query(receta)) != []):

            return [True, "La receta ya existe."]

        else:

            return [False, receta]

        
    #Función que cambia los entrys dependiendo del modo.
    #E: ninguna
    #S: ninguna
    #R: ninguna
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


#Clase que define el método de consulta.
#Se encarga de manejar todas las consultas.
class VentanaConsulta:

    def __init__(self, ventana):

        self.consulta = Toplevel(ventana, height = 500, width = 500, bg = "white")
        self.img1 = PhotoImage(file = "rata.gif")
        self.label_imag1 = Label(self.consulta, image = self.img1)
        self.label_imag1.img1 = self.img1
        self.label_imag1.pack(side='top', fill='both', expand='yes')

        self.label_consulta = Label(self.consulta, text = "Restaurante Le Poulet", bg = "white", fg = "black", font = ("Helvetica", 15))
        self.label_consulta.place(x = 70, y = 15)

        self.label_query = Label(self.consulta, text = "Consulta de datos", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.label_query.place(x = 75, y = 40)

        self.label_ingrediente = Label(self.consulta, text = "Ingrediente", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.label_ingrediente.place(x = 30, y = 90)

        ingredientes=['Aguacate', 'Culantro', 'Arroz', 'Espinaca']                 
        sv = StringVar()
        self.ingrediente = ttk.Combobox(self.consulta, width = 15, height = 6,textvariable = sv)
        self.ingrediente.place(x = 30, y = 115, height=20, width=115)
        self.ingrediente['values']=(ingredientes) 

        self.receta = Label(self.consulta, text = "Nombre de la receta", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.receta.place(x = 30, y = 155)

        recetas=['Sopa Azteca', 'Arroz blanco', 'Sopa de mariscos', 'Lasagna']                 
        sv = StringVar()
        self.receta = ttk.Combobox(self.consulta, width = 15, height = 6,textvariable = sv)
        self.receta.place(x = 30, y = 180, height=20, width=115)
        self.receta['values']=(recetas) 

        self.cocinero = Label(self.consulta, text = "Autor de la receta", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.cocinero.place(x = 200, y = 155)
        
        cocineros=['Chef Geovanny', 'Chef Luisa', 'Chef Alexander', 'Tia Florita']                 
        sv = StringVar()
        self.cocinero = ttk.Combobox(self.consulta, width = 15, height = 6,textvariable = sv)
        self.cocinero.place(x = 200, y = 180, height=20, width=115)
        self.cocinero['values']=(cocineros) 
        
        self.estilo = Label(self.consulta, text = "Estilo de la comida", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.estilo.place(x = 200, y = 90)

        estilos=['Mexicana', 'Francesa', 'Americana', 'Light']                 
        sv = StringVar()
        self.estilo = ttk.Combobox(self.consulta, width = 15, height = 6,textvariable = sv)
        self.estilo.place(x = 200, y = 115, height=20, width=115)
        self.estilo['values']=(estilos) 

        self.consultar = Button(self.consulta, bg = "gray", fg = "black", text = "Consultar", height = 1, width = 10, relief = RAISED)
        self.consultar.place(x = 120, y = 240)

        self.indicacion = Label(self.consulta, text = "*Sirvase ingresar los datos que requiera para la consulta", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.indicacion.place(x = 30, y = 310)


#Clase de interfaz.
#Se encarga de manejar toda la intefaz.
class VentanaPrincipal:

    #Constructor. No recibe parámetros.
    def __init__(self, errorInicio):
        
        self.ventana()
        self.menu()
        self.fondo()
        self.labelsBotones()
        if(errorInicio):
            box.showinfo("Error","El código de prolog que se intentó abrir no existe.\n Se creó uno bajo el nombre de Recetas.pl")
        self.ventana_principal.mainloop()


    #Función que crea la ventana principal.
    def ventana(self):
        
        self.ventana_principal = Tk() # Creación de la ventana principal
        self.ventana_principal.title("Restaurante Le Poulet") # Nombre de la ventana
        self.ventana_principal.geometry("600x450")

        self.ventana = Frame(self.ventana_principal, height = 1000, width = 1000, bg = "white") # Creación del contenedor de la aplicación
        self.ventana.pack() # Ubicación del frame en la ventana

    #Función que crea el menú.
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

    #Función que crea el fondo de la ventana.
    def fondo(self):
        
        self.img1 = PhotoImage(file = "Portada.gif")
        self.label_imag1 = Label(self.ventana, image = self.img1)
        self.label_imag1.img1 = self.img1
        self.label_imag1.pack(side='top', fill='both', expand='yes')

        self.tit = Label(self.ventana, text = "¡Bienvenido al Restaurante Le Poulet!", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.tit.place(x = 150, y = 50)

        self.titu = Label(self.ventana, text = "Sírvase elegir el modo de acceso", bg = "white", fg = "black", font = ("Helvetica", 10))
        self.titu.place(x = 160, y = 130)

    #Función que crea los labels y botones.
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

    #Función que obtiene el valor del modo a entrar (Mantenimiento o consulta.)
    def seleccion(self):
        
        return self.varModo.get()

    #Función que se encarga de crear las otras ventanas de la interfaz.
    def ingresar(self):

        if self.seleccion() == 1:                                           #1 para mantenimiento

            VentanaMantenimiento(self.ventana_principal)
            
        elif self.seleccion() == 2:                                         #2 para consulta

            VentanaConsulta(self.ventana_principal)

        else:
            
            box.showerror("Error", "Debe seleccionar un modo de acceso.")   #Mensaje de error si no escogió ningún modo.


pr = ManejoProlog("Prasdaueba.pl")   #Se crea la instancia del manejo de prolog con la dirección del archivo.
VentanaPrincipal(pr.error)               #Se crea la instancia de la interfaz.













