import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto Semestral - Estructuras Discretas")
ventana.geometry("700x900")

# Crear un marco para la presentación
frame_presentacion = tk.Frame(ventana, pady=20)
frame_presentacion.pack() 

# Crear las etiquetas con la información
titulo = tk.Label(frame_presentacion, text="Universidad Tecnológica de Panamá", font=("Arial", 16, "bold"))
facultad = tk.Label(frame_presentacion, text="Facultad de Ingeniería de Sistemas Computacionales", font=("Arial", 12, "bold"))
materia = tk.Label(frame_presentacion, text="Estructuras Discretas para la Computación\n", font=("Arial", 12, "bold"))
semestral = tk.Label(frame_presentacion, text="Semestral No.1\n", font=("Arial", 12, "bold"))
tema = tk.Label(frame_presentacion, text="Tema:", font=("Arial", 12, "bold"))
tema_texto = tk.Label(frame_presentacion, text="Conceptos de la teoría de conjuntos", font=("Arial", 12))
facilitador_titulo = tk.Label(frame_presentacion, text="\nFacilitador:", font=("Arial", 12, "bold"))
integrantes_titulo = tk.Label(frame_presentacion, text="\nIntegrantes:", font=("Arial", 12, "bold"))
grupo = tk.Label(frame_presentacion, text="Grupo: 1IL123\n", font=("Arial", 12, "bold"))
semestre = tk.Label(frame_presentacion, text="Semestre: 1", font=("Arial", 12, "bold"))



# NOMBRES
facilitador_nombre = tk.Label(frame_presentacion, text="Ing. Samuel Jiménez")
integrante1 = tk.Label(frame_presentacion, text="De Los Santos, David 8-974-141")
integrante2 = tk.Label(frame_presentacion, text="Borge, Sara 8-1025-1487")
integrante3 = tk.Label(frame_presentacion, text="Alveo, Rogelio 8-1024-1320")
integrante4 = tk.Label(frame_presentacion, text="Diego, Sanjur 8-1024-2362\n")


# Empaquetar las etiquetas para que aparezcan en el marco
titulo.pack()
facultad.pack()
materia.pack()
semestral.pack()
tema.pack()
tema_texto.pack()
facilitador_titulo.pack()
facilitador_nombre.pack()
integrantes_titulo.pack()
integrante1.pack()
integrante2.pack()
integrante3.pack()
integrante4.pack()
grupo.pack()
semestre.pack()
###################
#FINAL PRESENTACIÓN
###################
from tkinter import messagebox
import itertools
# marco para la entrada de datos
frame_entrada = tk.Frame(ventana, pady=10)
frame_entrada.pack()

label_A = tk.Label(frame_entrada, text="Conjunto A (máx 5 elementos, separados por coma):")
label_A.pack()
entry_A = tk.Entry(frame_entrada, width=50)
entry_A.pack()

label_B = tk.Label(frame_entrada, text="\nConjunto B (máx 5 elementos, separados por coma):")
label_B.pack()
entry_B = tk.Entry(frame_entrada, width=50)
entry_B.pack()

# RESULTADOS 
frame_resultados = tk.Frame(ventana, pady=10)
frame_resultados.pack()

label_producto_titulo = tk.Label(frame_resultados, text="Resultado del Producto Cartesiano (A x B):", font=("Arial", 12, "bold"))
label_producto_titulo.pack()

# Etiqueta donde se mostrará el resultado
label_producto_resultado = tk.Label(frame_resultados, text="", font=("Courier", 10), wraplength=550, justify="left")
label_producto_resultado.pack()

# FUNCIÓN PARA EL BOTÓN 
def procesar_conjuntos():
    texto_A = entry_A.get()
    texto_B = entry_B.get()
    
    if not texto_A or not texto_B:
        messagebox.showerror("Error", "Ambos conjuntos deben tener valores.")
        return

    conjunto_A = [elemento.strip() for elemento in texto_A.split(',') if elemento.strip()]
    conjunto_B = [elemento.strip() for elemento in texto_B.split(',') if elemento.strip()]

    if len(conjunto_A) > 5 or len(conjunto_B) > 5:
        messagebox.showwarning("Error de validación", "Cada conjunto debe tener un máximo de 5 elementos.")
        return

    # Calcular el producto cartesiano
    producto_cartesiano = list(itertools.product(conjunto_A, conjunto_B))
    
    # Formatear el resultado para mostrarlo
    resultado_texto = "A x B = {" + ", ".join(map(str, producto_cartesiano)) + "}"

    # Actualizar la etiqueta de resultado en la GUI
    label_producto_resultado.config(text=resultado_texto)

# Botón para procesar los conjuntos
boton_procesar = tk.Button(frame_entrada, text="1. Calcular Producto Cartesiano", command=procesar_conjuntos, pady=5, font=("Arial", 10, "bold"))
boton_procesar.pack(pady=20)


ventana.mainloop()