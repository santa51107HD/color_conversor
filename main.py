import tkinter as tk
#RGB a HSV
def rgb_hsv(r,g,b):
    rp=r/255
    gp=g/255
    bp=b/255
    cmax=max(rp,gp,bp)
    cmin=min(rp,gp,bp)
    delta=cmax-cmin
    h=0
    if delta==0:
        h=0
    elif cmax==rp:
        h=60*(((gp-bp)/delta)%6)
    elif cmax==gp:
        h=60*(((bp-rp)/delta)+2)
    elif cmax==bp:
        h=60*(((rp-gp)/delta)+4)
    s=0
    if cmax==0:
        s=0
    elif cmax!=0:
        s=delta/cmax
    v=cmax
    resultado = "HSV:("+ " " + str(h) + " , " + str(s) + " , " + str(v) + " )"
    return resultado

#HSV a RGB
def hsv_rgb(h,s,v):
    c=v*s
    x=c*(1-abs(((h/60)%2)-1))
    m=v-c
    rp=0
    gp=0
    bp=0
    if 0<=h<60:
        rp=c
        gp=x
        bp=0
    elif 60<=h<120:
        rp=x
        gp=c
        bp=0
    elif 120<=h<180:
        rp=0
        gp=c
        bp=x
    elif 180<=h<240:
        rp=0
        gp=x
        bp=c
    elif 240<=h<300:
        rp=x
        gp=0
        bp=c
    elif 300<=h<360:
        rp=c
        gp=0
        bp=x
    r=(rp+m)*255
    g=(gp+m)*255
    b=(bp+m)*255
    resultado = "RGB:("+ " " + str(r) + " , " + str(g) + " , " + str(b) + " )"
    return resultado

#RGB a HSL
def rgb_hsl(r,g,b):
    rp=r/255
    gp=g/255
    bp=b/255
    cmax=max(rp,gp,bp)
    cmin=min(rp,gp,bp)
    delta=cmax-cmin
    h=0
    if delta==0:
        h=0
    elif cmax==rp:
        h=60*(((gp-bp)/delta)%6)
    elif cmax==gp:
        h=60*(((bp-rp)/delta)+2)
    elif cmax==bp:
        h=60*(((rp-gp)/delta)+4)
    l=(cmax+cmin)/2
    s=0
    if delta==0:
        s=0
    elif delta<0 or delta>0:
        s=delta/(1-abs(2*l-1))
    resultado = "HSL:("+ " " + str(h) + " , " + str(s) + " , " + str(l) + " )"
    return resultado

#HSL a RGB
def hsl_rgb(h,s,l):
    c=(1-abs(2*l-1))*s
    x=c*(1-abs(((h/60)%2)-1))
    m=l-(c/2)
    rp=0
    gp=0
    bp=0
    if 0<=h<60:
        rp=c
        gp=x
        bp=0
    elif 60<=h<120:
        rp=x
        gp=c
        bp=0
    elif 120<=h<180:
        rp=0
        gp=c
        bp=x
    elif 180<=h<240:
        rp=0
        gp=x
        bp=c
    elif 240<=h<300:
        rp=x
        gp=0
        bp=c
    elif 300<=h<360:
        rp=c
        gp=0
        bp=x
    r=(rp+m)*255
    g=(gp+m)*255
    b=(bp+m)*255
    resultado = "RGB:("+ " " + str(r) + " , " + str(g) + " , " + str(b) + " )"
    return resultado

#RGB a CMY
def rgb_cmy(r,g,b):
    rp=r/255
    gp=g/255
    bp=b/255
    c=1-rp
    m=1-gp
    y=1-bp
    resultado = "CMY:("+ " " + str(c) + " , " + str(m) + " , " + str(y) + " )"
    return resultado

#CMY a RGB
def cmy_rgb(c,m,y):
    r=(1-c)*255
    g=(1-m)*255
    b=(1-y)*255
    resultado = "RGB:("+ " " + str(r) + " , " + str(g) + " , " + str(b) + " )"
    return resultado

def valores():
    ventana.destroy() 
    respuesta = var.get()
    resultado = None
    # Crea la ventana principal
    ventana2 = tk.Tk()
    ventana2.eval('tk::PlaceWindow . center')
    ventana2.title("Convertidor de espacio de color")

    # Crear una etiqueta con el texto"
    etiqueta = tk.Label(ventana2, text="Llene los campos con los valores correspondientes:")
    etiqueta.grid(row=0, columnspan=2, padx=10, pady=10)

    # Centrar los widgets en la ventana
    ventana2.columnconfigure(0, weight=1)
    ventana2.columnconfigure(1, weight=1)
    ventana2.rowconfigure(0, weight=1)

    #Funcion que ejecuta los algoritmos de conversion
    def algoritmo():
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        valor3 = float(entrada3.get())
        if respuesta  == "rgb_hsv":
            resultado =rgb_hsv(valor1,valor2,valor3)
        elif respuesta  == "hsv_rgb":
            resultado =hsv_rgb(valor1,valor2,valor3)
        elif respuesta  == "rgb_hsl":
            resultado =rgb_hsl(valor1,valor2,valor3)
        elif respuesta  == "hsl_rgb":
            resultado =hsl_rgb(valor1,valor2,valor3)
        elif respuesta  == "rgb_cmy":
            resultado =rgb_cmy(valor1,valor2,valor3)
        elif respuesta  == "cmy_rgb":
            resultado =cmy_rgb(valor1,valor2,valor3)
        etiqueta_resultado.config(text="Resultado: " + str(resultado))

    boton2 = tk.Button(ventana2, text="Convertir", command=algoritmo)
    boton2.grid(row=4, columnspan=2, padx=10, pady=10)

    # Crear un widget de etiqueta para mostrar el resultado
    etiqueta_resultado = tk.Label(ventana2, text="Resultado: ")
    etiqueta_resultado.grid(row=5, columnspan=3, padx=10, pady=10)

    if respuesta == "rgb_hsv" or respuesta =="rgb_hsl" or respuesta =="rgb_cmy":

        etiqueta1 = tk.Label(ventana2, text="R:")
        etiqueta1.grid(row=1, column=0, padx=10, pady=10)

        entrada1 = tk.Entry(ventana2)
        entrada1.grid(row=1, column=1, padx=10, pady=10)

        etiqueta2 = tk.Label(ventana2, text="G:")
        etiqueta2.grid(row=2, column=0, padx=10, pady=10)

        entrada2 = tk.Entry(ventana2)
        entrada2.grid(row=2, column=1, padx=10, pady=10)

        etiqueta3 = tk.Label(ventana2, text="B:")
        etiqueta3.grid(row=3, column=0, padx=10, pady=10)

        entrada3 = tk.Entry(ventana2)
        entrada3.grid(row=3, column=1, padx=10, pady=10)

    elif respuesta == "hsv_rgb":

        etiqueta1 = tk.Label(ventana2, text="H:")
        etiqueta1.grid(row=1, column=0, padx=10, pady=10)

        entrada1 = tk.Entry(ventana2)
        entrada1.grid(row=1, column=1, padx=10, pady=10)

        etiqueta2 = tk.Label(ventana2, text="S:")
        etiqueta2.grid(row=2, column=0, padx=10, pady=10)

        entrada2 = tk.Entry(ventana2)
        entrada2.grid(row=2, column=1, padx=10, pady=10)

        etiqueta3 = tk.Label(ventana2, text="V:")
        etiqueta3.grid(row=3, column=0, padx=10, pady=10)

        entrada3 = tk.Entry(ventana2)
        entrada3.grid(row=3, column=1, padx=10, pady=10)

    elif respuesta == "hsl_rgb":

        etiqueta1 = tk.Label(ventana2, text="H:")
        etiqueta1.grid(row=1, column=0, padx=10, pady=10)

        entrada1 = tk.Entry(ventana2)
        entrada1.grid(row=1, column=1, padx=10, pady=10)

        etiqueta2 = tk.Label(ventana2, text="S:")
        etiqueta2.grid(row=2, column=0, padx=10, pady=10)

        entrada2 = tk.Entry(ventana2)
        entrada2.grid(row=2, column=1, padx=10, pady=10)

        etiqueta3 = tk.Label(ventana2, text="L:")
        etiqueta3.grid(row=3, column=0, padx=10, pady=10)

        entrada3 = tk.Entry(ventana2)
        entrada3.grid(row=3, column=1, padx=10, pady=10)

    elif respuesta == "cmy_rgb":

        etiqueta1 = tk.Label(ventana2, text="C:")
        etiqueta1.grid(row=1, column=0, padx=10, pady=10)

        entrada1 = tk.Entry(ventana2)
        entrada1.grid(row=1, column=1, padx=10, pady=10)

        etiqueta2 = tk.Label(ventana2, text="M:")
        etiqueta2.grid(row=2, column=0, padx=10, pady=10)

        entrada2 = tk.Entry(ventana2)
        entrada2.grid(row=2, column=1, padx=10, pady=10)

        etiqueta3 = tk.Label(ventana2, text="Y:")
        etiqueta3.grid(row=3, column=0, padx=10, pady=10)

        entrada3 = tk.Entry(ventana2)
        entrada3.grid(row=3, column=1, padx=10, pady=10)


# Crea la ventana principal
ventana = tk.Tk()
ventana.eval('tk::PlaceWindow . center')
ventana.title("Convertidor de espacio de color")

# Crear una etiqueta con el texto"
etiqueta = tk.Label(ventana, text="Marque el tipo de conversion que desea realizar:")
etiqueta.pack()

# Crear una variable para almacenar la respuesta del usuario
var = tk.StringVar()
var.set(0)

# Crear los botones de radio con las opciones de conversion
radio1 = tk.Radiobutton(ventana, text="RGB a HSV", variable=var, value="rgb_hsv")
radio2 = tk.Radiobutton(ventana, text="HSV a RGB", variable=var, value="hsv_rgb")
radio3 = tk.Radiobutton(ventana, text="RGB a HSL", variable=var, value="rgb_hsl")
radio4 = tk.Radiobutton(ventana, text="HSL a RGB", variable=var, value="hsl_rgb")
radio5 = tk.Radiobutton(ventana, text="RGB a CMY", variable=var, value="rgb_cmy")
radio6 = tk.Radiobutton(ventana, text="CMY a RGB", variable=var, value="cmy_rgb")
radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()
radio5.pack()
radio6.pack()

# Crear un boton que llame a la funcion valores
boton = tk.Button(ventana, text="Continuar", command=valores)
boton.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()