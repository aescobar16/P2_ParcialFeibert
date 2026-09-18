from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Banco de preguntas sobre Stack y Arquitectura de Software
QUESTIONS = [
    {
        "id": 1,
        "pregunta": "¿Cuál es la característica principal de la Arquitectura Hexagonal (Puertos y Adaptadores)?",
        "opciones": {
            "A": "Depende directamente de la base de datos y la interfaz de usuario en el núcleo.",
            "B": "Aísla la lógica de dominio central de los detalles externos mediante puertos (interfaces) y adaptadores.",
            "C": "Obliga a que todo el código se implemente en un único script monohilo.",
            "D": "Elimina por completo la necesidad de protocolos de comunicación e inversión de dependencias."
        },
        "correcta": "B",
        "explicacion": "¡Excelente! La Arquitectura Hexagonal desacopla el núcleo de la aplicación (dominio/negocio) del exterior (bases de datos, frameworks, UI), facilitando pruebas y reemplazos sin tocar las reglas de negocio."
    },
    {
        "id": 2,
        "pregunta": "¿En el stack tecnológico Python/Flask + Gunicorn, qué rol cumple Gunicorn?",
        "opciones": {
            "A": "Actúa como servidor WSGI de producción que gestiona múltiples procesos/workers para atender peticiones.",
            "B": "Es una base de datos relacional orientada a grafos.",
            "C": "Es un motor de plantillas HTML idéntico a Jinja2.",
            "D": "Se encarga del diseño visual y estilización CSS del frontend."
        },
        "correcta": "A",
        "explicacion": "¡Correcto! Gunicorn (Green Unicorn) es un servidor WSGI HTTP compatible con UNIX que permite manejar múltiples peticiones concurrentes en producción, a diferencia del servidor de desarrollo de Flask."
    },
    {
        "id": 3,
        "pregunta": "¿Cuál es la principal ventaja de una Arquitectura de Microservicios frente a una Monolítica?",
        "opciones": {
            "A": "Menor complejidad en el despliegue y cero necesidad de monitoreo distribuido.",
            "B": "Despliegue independiente, escalabilidad modular y tolerancia a fallos por componentes.",
            "C": "Permite usar una sola tabla en SQLite para todo el sistema sin APIs.",
            "D": "Garantiza que la red interna nunca falle ni tenga latencia."
        },
        "correcta": "B",
        "explicacion": "¡Muy bien! Los microservicios permiten que cada servicio sea desplegado, escalado y mantenido independientemente, adaptando la tecnología a la necesidad de cada dominio."
    }
]

@app.route('/')
def home():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/api/quiz/validate', methods=['POST'])
def validate_answer():
    data = request.get_json() or {}
    question_id = data.get('question_id')
    selected_option = data.get('selected_option')

    # Buscar la pregunta
    question = next((q for q in QUESTIONS if q['id'] == question_id), None)
    if not question:
        return jsonify({"success": False, "message": "Pregunta no encontrada"}), 404

    is_correct = (selected_option == question['correcta'])
    
    return jsonify({
        "success": True,
        "is_correct": is_correct,
        "correct_option": question['correcta'],
        "selected_option": selected_option,
        "explicacion": question['explicacion'] if is_correct else f"Incorrecto. La respuesta correcta era la opción {question['correcta']}: {question['opciones'][question['correcta']]}. ¡Sigue repasando los principios arquitectónicos!"
    })

if __name__ == '__main__':
    app.run(debug=True)