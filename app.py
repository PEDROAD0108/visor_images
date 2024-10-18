import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Crear la ventana principal
root = tk.Tk()
root.title("Visor de Imágenes")
root.geometry("800x600")
root.config(bg="#2c3e50")  # Cambiar el color de fondo

# Variables para manejar la lista de imágenes y el índice actual
imagenes = []
indice_actual = 0
carpeta_anterior = ""  # Variable para almacenar la carpeta anterior

# Label para mostrar el mensaje de bienvenida
welcome_label = tk.Label(root, text="Welcome to my Visor Images", bg="#2c3e50", fg="white", font=("Arial", 24))
welcome_label.pack(pady=20)

# Label para mostrar la imagen
image_label = tk.Label(root, bg="#34495e")
image_label.pack(expand=True, padx=10, pady=10)

def mostrar_imagen():
    """Mostrar la imagen actual en el Label."""
    if imagenes:
        img = Image.open(imagenes[indice_actual])
        img.thumbnail((800, 600))  # Redimensionar la imagen manteniendo la relación de aspecto
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Referencia para evitar que se recoja

def cargar_imagenes():
    """Cargar imágenes desde un directorio."""
    global imagenes, indice_actual, carpeta_anterior
    directorio = filedialog.askdirectory()
    if directorio:
        carpeta_anterior = directorio  # Guardar la carpeta actual como anterior
        imagenes = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if not imagenes:
            messagebox.showwarning("Advertencia", "No se encontraron imágenes en el directorio seleccionado.")
        else:
            indice_actual = 0  # Reiniciar el índice
            welcome_label.pack_forget()  # Ocultar el mensaje de bienvenida al cargar imágenes
            mostrar_imagen()  # Mostrar la primera imagen

def cargar_imagenes_ruta_predeterminada():
    """Cargar imágenes desde una carpeta predeterminada."""
    global imagenes, indice_actual, carpeta_anterior
    ruta_predeterminada = "/path/to/your/images"  # Cambia esto por la ruta que desees
    if os.path.exists(ruta_predeterminada):
        carpeta_anterior = ruta_predeterminada  # Guardar la carpeta actual como anterior
        imagenes = [os.path.join(ruta_predeterminada, f) for f in os.listdir(ruta_predeterminada) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if not imagenes:
            messagebox.showwarning("Advertencia", "No se encontraron imágenes en la ruta predeterminada.")
        else:
            indice_actual = 0  # Reiniciar el índice
            welcome_label.pack_forget()  # Ocultar el mensaje de bienvenida al cargar imágenes
            mostrar_imagen()  # Mostrar la primera imagen
    else:
        messagebox.showerror("Error", "La ruta predeterminada no existe.")

def retroceder_carpeta():
    """Retroceder a la carpeta anterior."""
    global imagenes, indice_actual
    if carpeta_anterior:
        # Permitir al usuario seleccionar un nuevo directorio
        directorio = filedialog.askdirectory(initialdir=carpeta_anterior)
        if directorio:
            cargar_imagenes()

def anterior_imagen():
    """Mostrar la imagen anterior."""
    global indice_actual
    if imagenes:
        indice_actual = (indice_actual - 1) % len(imagenes)  # Volver al último si estamos en el primero
        mostrar_imagen()

def siguiente_imagen():
    """Mostrar la imagen siguiente."""
    global indice_actual
    if imagenes:
        indice_actual = (indice_actual + 1) % len(imagenes)  # Volver al primero si estamos en el último
        mostrar_imagen()

def tecla_navegacion(event):
    """Navegar usando teclas de flecha."""
    if event.keysym == 'Left':
        anterior_imagen()
    elif event.keysym == 'Right':
        siguiente_imagen()

# Conectar la función de navegación con el teclado
root.bind("<Key>", tecla_navegacion)

# Crear un marco para los botones
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

# Botones
btn_cargar = tk.Button(button_frame, text="Cargar imágenes", command=cargar_imagenes, bg="#3498db", fg="white", font=("Arial", 12))
btn_cargar.pack(side="left", padx=5)

btn_ruta_predeterminada = tk.Button(button_frame, text="Cargar desde ruta predeterminada", command=cargar_imagenes_ruta_predeterminada, bg="#3498db", fg="white", font=("Arial", 12))
btn_ruta_predeterminada.pack(side="left", padx=5)

btn_retroceder = tk.Button(button_frame, text="Retroceder", command=retroceder_carpeta, bg="#3498db", fg="white", font=("Arial", 12))
btn_retroceder.pack(side="left", padx=5)

btn_prev = tk.Button(button_frame, text="Anterior", command=anterior_imagen, bg="#3498db", fg="white", font=("Arial", 12))
btn_prev.pack(side="left", padx=5)

btn_next = tk.Button(button_frame, text="Siguiente", command=siguiente_imagen, bg="#3498db", fg="white", font=("Arial", 12))
btn_next.pack(side="left", padx=5)

root.mainloop()
