# Entrenador Digital Voley

# **Documentación del Proyecto: Entrenador Digital de Voleibol**

## **1. Introducción**

El *Entrenador Digital de Voleibol* es una aplicación diseñada para ayudar a los jugadores de voleibol a mejorar su desempeño, ajustándose a su nivel, posición y objetivos. Este sistema combina una interfaz intuitiva con un backend funcional para recoger datos del usuario y proporcionar retroalimentación personalizada.

Este documento explica la estructura, implementación y funcionamiento del proyecto hasta la fecha.

---

## **2. Estructura del Proyecto**

El proyecto se organiza en dos componentes principales:

1. **Backend**: Implementado en Python con Flask.
2. **Frontend**: Una interfaz web interactiva creada con HTML5, CSS3 y Bootstrap.



### **Componentes Clave**

- **`app.py`**: Archivo que contiene toda la lógica de la aplicación. Define las rutas, maneja solicitudes y renderiza las plantillas HTML.
- **`templates/formulario.html`**: Archivo HTML que presenta el formulario al usuario, diseñado con Bootstrap y estilos personalizados.

---

## **3. app.py**

El archivo `app.py` es el núcleo de la aplicación, escrito en Python utilizando Flask, un framework minimalista para aplicaciones web.

### **Código**

```python
from flask import Flask, render_template, request

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta principal para mostrar el formulario
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Recibir datos del formulario
        nivel = request.form.get("nivel")
        posicion = request.form.get("posicion")
        objetivo = request.form.get("objetivo")
        tiempo = request.form.get("tiempo")

        # Mostrar los datos recibidos en consola (debugging)
        print(f"Nivel: {nivel}, Posición: {posicion}, Objetivo: {objetivo}, Tiempo: {tiempo}")
        return "Formulario enviado exitosamente. (Implementar lógica aquí)"

    # Renderizar el formulario HTML
    return render_template('formulario.html')

# Ejecutar la aplicación en modo desarrollo
if __name__ == "__main__":
    app.run(debug=True)
