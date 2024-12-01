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

```

### Descripción Funcional 

#### 1: Importacion de Modulos

```python
from flask import Flask, render_template, request
```
- **Flask**: Framework que proporciona herramientas para crear aplicaciones web.
- **render_template**: Renderiza archivos HTML desde la carpeta ```templates```.
- **request**: Captura datos enviados mediante formularios.


#### 2: Inicialización

```python
app = Flask(__name__)
```
- Crea una instancia de Flask. Este es el punto de partida de cualquier aplicación Flask.


#### 3: Definición de la ruta principal

```python
@app.route("/", methods=["GET", "POST"])

```
- Define que la ruta ```/ ```(URL raíz) se puede acceder tanto con ```GET``` como con ```POST```.
  - **GET**: Muestra el formulario al usuario.
  - **POST**: Procesa los datos enviados por el formulario.



#### 4: Manejo de solicitudes

```python
if request.method == "POST":
    nivel = request.form.get("nivel")
    posicion = request.form.get("posicion")
    objetivo = request.form.get("objetivo")
    tiempo = request.form.get("tiempo")

```
- Extrae los valores ingresados por el usuario utilizando ```request.form.get()```. Estos valores corresponden a los nombres de los campos en el formulario HTML.



#### 5: Depuración

```python
print(f"Nivel: {nivel}, Posición: {posicion}, Objetivo: {objetivo}, Tiempo: {tiempo}")
```
- Muestra los datos capturados en la consola para verificar que la aplicación funciona correctamente.


  
#### 6: Renderización del formulario

```python
return render_template('formulario.html')
```
- Muestra el archivo ```formulario.html``` cuando se accede a la aplicación por primera vez (método ```GET```).



#### 7: Ejecución del servidor

```python
if __name__ == "__main__":
    app.run(debug=True)
 
```
- Inicia el servidor Flask en modo desarrollo.
- ```debug=True``` permite detectar errores y recargar automáticamente la aplicación al hacer cambios en el código.



### 4 Formulario.html

El archivo ```formulario.html``` es la interfaz gráfica que interactúa con el usuario.

Codigo: 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entrenador de Voleibol</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .form-container {
            background: white;
            color: black;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        .btn {
            background: #ff6f61;
            border: none;
        }
        .btn:hover {
            background: #e65b50;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2 class="text-center">Entrenador Digital</h2>
        <form method="POST">
            <div class="form-group mb-3">
                <label for="nivel">Selecciona tu nivel:</label>
                <select class="form-select" name="nivel" id="nivel" required>
                    <option value="" disabled selected>Elige una opción</option>
                    <option value="Principiante">Principiante</option>
                    <option value="Intermedio">Intermedio</option>
                    <option value="Avanzado">Avanzado</option>
                </select>
            </div>
            <div class="form-group mb-3">
                <label for="posicion">Tu posición en el equipo:</label>
                <input type="text" class="form-control" id="posicion" name="posicion" placeholder="Ejemplo: Líbero" required>
            </div>
            <div class="form-group mb-3">
                <label for="objetivo">¿Cuál es tu objetivo principal?</label>
                <textarea class="form-control" id="objetivo" name="objetivo" rows="3" placeholder="Escribe tus metas..." required></textarea>
            </div>
            <div class="form-group mb-3">
                <label for="tiempo">¿Cuánto tiempo puedes entrenar por semana? (horas)</label>
                <input type="number" class="form-control" id="tiempo" name="tiempo" min="1" max="40" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Enviar</button>
        </form>
    </div>
</body>
</html>

```

#### **Características del Diseño**

- Estilo Moderno
  - Fuente ```Poppins``` de Google Fonts
  - Gradiente de fondo.
  - Diseño centrado y responsivo.

- Formulario Interactivo
  - Campos requeridos (```required```) para validación básica.
  - Uso de Bootstrap para estilos predefinidos.

- Accesibilidad
  - Etiquetas ```<label>``` asociadas a campos específicos para facilitar la navegación.
 




# **Evaluación de Jugadores de Voleibol**

## Descripción
Este proyecto es una aplicación web construida con **Flask**, diseñada para evaluar y analizar las habilidades de jugadores de voleibol. Los usuarios pueden:
- Ingresar información básica sobre su nivel, posición y metas.
- Subir un video de su desempeño en la cancha.
- Recibir retroalimentación inicial basada en su entrada.

## Funcionalidades
1. **Interfaz Dinámica**:
   - Basada en Bootstrap para un diseño moderno y responsivo.
   - Opciones intuitivas para seleccionar nivel, posición y metas.
2. **Análisis de Video**:
   - Uso de MediaPipe Pose para detectar movimientos y posturas.
   - Visualización del video con puntos de referencia dibujados.
3. **Fácil Configuración**:
   - Requiere dependencias básicas instaladas con `pip`.

## Requisitos
- **Python**: 3.8 o superior
- **Bibliotecas**: 
  - Flask
  - OpenCV
  - MediaPipe

Instalación:
```bash
pip install flask opencv-python mediapipe





