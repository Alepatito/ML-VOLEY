# Formulario HTML para ingresar la información del usuario 
from flask import Flask, request, render_template

# Inicializar Flask app
app = Flask(__name__)

# Ruta principal que muestra el formulario y procesa la información del usuario
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nivel = request.form.get('nivel')
        posicion = request.form.get('posicion')
        objetivo = request.form.get('objetivo')
        tiempo = request.form.get('tiempo')
        # Procesar la información del usuario
        return f"Nivel: {nivel}, Posición: {posicion}, Objetivo: {objetivo}, Tiempo: {tiempo}"
    return render_template('formulario.html')

# Página de inicio con el mensaje de bienvenida

if __name__ == '__main__':
    app.run(debug=True)
