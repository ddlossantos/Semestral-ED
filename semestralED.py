import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Proyecto Semestral - Estructuras Discretas")
ventana.geometry("600x500") # Ancho x Alto en píxeles

# Crear un marco (frame) para la presentación
frame_presentacion = tk.Frame(ventana, pady=20) # pady añade un espacio vertical
frame_presentacion.pack() # Coloca el marco en la ventana

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



# --- LOS NOMBRES ---
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

ventana.mainloop()