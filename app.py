# Importación de librerías necesarias
from flask import Flask, render_template, request
import os
import cv2
import mediapipe as mp

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Crear carpeta 'uploads' para guardar videos si no existe
if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Ruta principal de la aplicación.
    Métodos admitidos:
    - GET: Renderiza el formulario HTML para la entrada de datos del usuario.
    - POST: Procesa los datos enviados por el formulario.
    """
    if request.method == "POST":
        # Capturar datos del formulario
        nivel = request.form.get("nivel")  # Nivel del jugador: principiante, intermedio o avanzado.
        posicion = request.form.get("posicion")  # Posición en la cancha (ej. armador).
        objetivo = request.form.get("objetivo")  # Meta personal ingresada por el usuario.
        tiempo = request.form.get("tiempo")  # Tiempo estimado para alcanzar el objetivo.

        # Guardar el video enviado en la carpeta 'uploads'
        video = request.files.get("video")
        video_path = os.path.join("uploads", video.filename)
        video.save(video_path)

        # Procesar el video para análisis
        process_video(video_path)

        # Respuesta para el usuario después de enviar el formulario
        return f"""
            ¡Gracias por enviar tu información! 
            Nivel: {nivel}, Posición: {posicion}, Objetivo: {objetivo}, Tiempo: {tiempo} semanas.
        """

    return render_template("formulario.html")  # Renderiza el formulario al acceder.

def process_video(video_path):
    """
    Procesa el video subido utilizando MediaPipe Pose para detectar puntos de referencia en el cuerpo.
    - Analiza frame por frame para extraer datos clave.
    - Muestra el video procesado con las detecciones en tiempo real.
    """
    # Inicialización de MediaPipe Pose
    mp_pose = mp.solutions.pose  # Solución para la detección de poses.
    pose = mp_pose.Pose()  # Configuración por defecto de MediaPipe Pose.
    cap = cv2.VideoCapture(video_path)  # Cargar el video para análisis.

    while cap.isOpened():
        ret, frame = cap.read()  # Leer cada frame del video.
        if not ret:  # Salir del bucle si el video termina.
            break

        # Convertir el frame a RGB (MediaPipe requiere imágenes en formato RGB).
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)  # Procesar el frame para obtener puntos de referencia.

        # Dibujar puntos de referencia si se detectan
        if results.pose_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Mostrar el video con anotaciones
        cv2.imshow("Video Procesado", frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Liberar el video capturado.
    cv2.destroyAllWindows()  # Cerrar todas las ventanas de OpenCV.

# Ejecutar la aplicación en modo debug
if __name__ == "__main__":
    app.run(debug=True)
