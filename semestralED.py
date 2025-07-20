import tkinter as tk
from tkinter import messagebox
import itertools
import re

# --- Variables globales para compartir datos entre funciones ---
conjunto_A_global = []
conjunto_B_global = []
producto_cartesiano_global = []
# (Puedes añadir más variables globales aquí para R y S si las necesitas después)

# --- FUNCIONES DE LA APLICACIÓN ---

def procesar_conjuntos():
    """Lee los conjuntos, calcula el producto cartesiano y lo muestra"""
    global conjunto_A_global, conjunto_B_global, producto_cartesiano_global

    texto_A = entry_A.get()
    texto_B = entry_B.get()
    
    if not texto_A or not texto_B:
        messagebox.showerror("Error", "Ambos conjuntos deben tener valores")
        return

    conjunto_A_global = [elemento.strip() for elemento in texto_A.split(',') if elemento.strip()]
    conjunto_B_global = [elemento.strip() for elemento in texto_B.split(',') if elemento.strip()]

    if len(conjunto_A_global) > 5 or len(conjunto_B_global) > 5:
        messagebox.showwarning("Error de validación", "Cada conjunto debe tener un máximo de 5 elementos")
        return

    producto_cartesiano_global = list(itertools.product(conjunto_A_global, conjunto_B_global))
    resultado_texto = "A x B = {" + ", ".join(map(str, producto_cartesiano_global)) + "}"
    label_producto_resultado.config(text=resultado_texto)
    
    for widget in frame_relaciones.winfo_children():
        widget.config(state='normal')

def generar_matrices():
    """Lee las relaciones R y S y muestra sus matrices booleanas"""
    if not producto_cartesiano_global:
        messagebox.showerror("Error", "Primero debes calcular el producto cartesiano.")
        return

    # Procesamiento y validación de R y S
    texto_R = entry_R.get()
    try:
        pares_R_str = re.findall(r'\((.*?)\)', texto_R)
        relacion_R = [tuple(par.split(',')) for par in pares_R_str]
        relacion_R = [(a.strip(), b.strip()) for a, b in relacion_R]
    except:
        messagebox.showerror("Error de formato", "El formato para R es incorrecto. Usa (a,b), (c,d), ...")
        return

    texto_S = entry_S.get()
    try:
        pares_S_str = re.findall(r'\((.*?)\)', texto_S)
        relacion_S = [tuple(par.split(',')) for par in pares_S_str]
        relacion_S = [(a.strip(), b.strip()) for a, b in relacion_S]
    except:
        messagebox.showerror("Error de formato", "El formato para S es incorrecto. Usa (a,b), (c,d), ...")
        return

    if len(relacion_R) > 8 or len(relacion_S) > 8:
        messagebox.showwarning("Error de validación", "Cada relación puede tener un máximo de 8 pares")
        return
    
    producto_str = [tuple(map(str, t)) for t in producto_cartesiano_global]
    for par in relacion_R + relacion_S:
        if par not in producto_str:
            messagebox.showerror("Error de validación", f"El par {par} no pertenece al producto cartesiano A x B")
            return

    matriz_R_texto = crear_texto_matriz(relacion_R, "R", conjunto_A_global, conjunto_B_global)
    matriz_S_texto = crear_texto_matriz(relacion_S, "S", conjunto_A_global, conjunto_B_global)
    
    label_matriz_R.config(text=matriz_R_texto)
    label_matriz_S.config(text=matriz_S_texto)

def crear_texto_matriz(relacion, nombre, c_a, c_b):
    texto_matriz = f"Matriz Booleana de {nombre}:\n\n"
    texto_matriz += f"{nombre:^2}|" + "".join([f"{elem:^5}" for elem in c_b]) + "\n"
    texto_matriz += "-" * (len(texto_matriz) + 20) + "\n"

    for a in c_a:
        fila = f"{a:^2}|"
        for b in c_b:
            if (str(a), str(b)) in [(str(x), str(y)) for x, y in relacion]:
                fila += f"{'1':^5}"
            else:
                fila += f"{'0':^5}"
        texto_matriz += fila + "\n"
    return texto_matriz

# --- INTERFAZ GRÁFICA ---
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto Semestral - Estructuras Discretas")
ventana.geometry("500x600") 

# --- CONFIGURACIÓN DEL SCROLLBAR ---
# Crear un Canvas principal y una Scrollbar
main_canvas = tk.Canvas(ventana)
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=main_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar el Canvas para que funcione con la Scrollbar
main_canvas.configure(yscrollcommand=scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

scrollable_frame = tk.Frame(main_canvas)

# Añadir el scrollable_frame al Canvas
main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

frame_presentacion = tk.Frame(scrollable_frame, pady=20)
frame_presentacion.pack(pady=10, padx=10) 

# Crear las etiquetas con la información 
titulo = tk.Label(frame_presentacion, text="Universidad Tecnológica de Panamá", font=("Arial", 16, "bold"), justify="center")
facultad = tk.Label(frame_presentacion, text="Facultad de Ingeniería de Sistemas Computacionales", font=("Arial", 12, "bold"), justify="center")
materia = tk.Label(frame_presentacion, text="Estructuras Discretas para la Computación\n", font=("Arial", 12, "bold"), justify="center")
semestral = tk.Label(frame_presentacion, text="Semestral No.1\n", font=("Arial", 12, "bold"), justify="center")
tema = tk.Label(frame_presentacion, text="Tema:", font=("Arial", 12, "bold"), justify="center")
tema_texto = tk.Label(frame_presentacion, text="Conceptos de la teoría de conjuntos", font=("Arial", 12), justify="center")
facilitador_titulo = tk.Label(frame_presentacion, text="\nFacilitador:", font=("Arial", 12, "bold"), justify="center")
integrantes_titulo = tk.Label(frame_presentacion, text="\nIntegrantes:", font=("Arial", 12, "bold"), justify="center")
grupo = tk.Label(frame_presentacion, text="Grupo: 1IL123\n", font=("Arial", 12, "bold"), justify="center")
semestre = tk.Label(frame_presentacion, text="Semestre: 1", font=("Arial", 12, "bold"), justify="center")

# NOMBRES 
facilitador_nombre = tk.Label(frame_presentacion, text="Ing. Samuel Jiménez", justify="center")
integrante1 = tk.Label(frame_presentacion, text="De Los Santos, David 8-974-141", justify="center")
integrante2 = tk.Label(frame_presentacion, text="Borge, Sara 8-1025-1487", justify="center")
integrante3 = tk.Label(frame_presentacion, text="Alveo, Rogelio 8-1024-1320", justify="center")
integrante4 = tk.Label(frame_presentacion, text="Diego, Sanjur 8-1024-2362\n", justify="center")

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

# --- SECCIÓN DE ENTRADA DE CONJUNTOS ---
frame_entrada = tk.Frame(scrollable_frame, pady=10)
frame_entrada.pack(pady=10, padx=10)
# Crear etiquetas y campos de entrada para los conjuntos A y B
label_A = tk.Label(frame_entrada, text="Conjunto A (máx 5 elementos, separados por coma):")
label_A.pack()
entry_A = tk.Entry(frame_entrada, width=50)
entry_A.pack()
label_B = tk.Label(frame_entrada, text="Conjunto A (máx 5 elementos, separados por coma):")
label_B.pack()
entry_B = tk.Entry(frame_entrada, width=50)
entry_B.pack()
boton_procesar = tk.Button(frame_entrada, text="1. Calcular Producto Cartesiano", command=procesar_conjuntos, pady=5, font=("Arial", 10, "bold"))
boton_procesar.pack(pady=20)


# --- SECCIÓN DE RESULTADO DEL PRODUCTO CARTESIANO ---
frame_resultados = tk.Frame(scrollable_frame, pady=10)
frame_resultados.pack(pady=10, padx=10)
# Crear etiquetas para mostrar el resultado del producto cartesiano
label_producto_titulo = tk.Label(frame_resultados, text="Resultado del Producto Cartesiano (A x B):", font=("Arial", 12, "bold"))
label_producto_titulo.pack()
label_producto_resultado = tk.Label(frame_resultados, text="", font=("Courier", 10), wraplength=650, justify="center")
label_producto_resultado.pack()


# --- SECCIÓN DE ENTRADA DE RELACIONES ---
frame_relaciones = tk.Frame(scrollable_frame, pady=10)
frame_relaciones.pack(pady=10, padx=10)
# Crear etiquetas y campos de entrada para las relaciones R y S
label_R = tk.Label(frame_relaciones, text="\nRelación R (máx 8 pares, formato: (a,b), (c,d)):", state='disabled')
label_R.pack()
entry_R = tk.Entry(frame_relaciones, width=70, state='disabled')
entry_R.pack()
label_matriz_S = tk.Label(frame_relaciones, text="\nRelación R (máx 8 pares, formato: (a,b), (c,d)):", state='disabled')
label_matriz_S.pack()
entry_S = tk.Entry(frame_relaciones, width=70, state='disabled')
entry_S.pack()
boton_matrices = tk.Button(frame_relaciones, text="2. Generar Matrices de Relación", command=generar_matrices, state='disabled', pady=5, font=("Arial", 10, "bold"))
boton_matrices.pack(pady=20)


# --- SECCIÓN DE VISUALIZACIÓN DE MATRICES ---
frame_matrices = tk.Frame(scrollable_frame, pady=10)
frame_matrices.pack(pady=10, padx=10)
# Crear etiquetas para mostrar las matrices booleanas de R y S
frame_matriz_display = tk.Frame(frame_matrices)
frame_matriz_display.pack()
label_matriz_R = tk.Label(frame_matriz_display, text="", font=("Courier", 12), justify="center")
label_matriz_R.pack(side="left", padx=20)
label_matriz_S = tk.Label(frame_matriz_display, text="", font=("Courier", 12), justify="center")
label_matriz_S.pack(side="left", padx=20)



ventana.mainloop()