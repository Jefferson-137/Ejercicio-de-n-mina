from flask import Flask, jsonify, request
from pyswip import Prolog

app = Flask(__name__)
prolog = Prolog()

# Cargar la base de conocimiento Prolog
prolog.consult("nomina.pl")

@app.route("/empleados", methods=["GET"])
def listar_empleados():
    """
    Listar todos los empleados con sus horas trabajadas.
    """
    empleados = list(prolog.query("empleado(Nombre, Horas)"))
    return jsonify(empleados)

@app.route("/salario/<string:nombre>", methods=["GET"])
def calcular_salario(nombre):
    """
    Calcular el salario de un empleado dado su nombre.
    """
    try:
        resultado = list(prolog.query(f"salario({nombre}, Salario)"))
        if resultado:
            return jsonify({"nombre": nombre, "salario": resultado[0]["Salario"]})
        else:
            return jsonify({"error": "Empleado no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/empleado", methods=["POST"])
def agregar_empleado():
    """
    Agregar un nuevo empleado con sus horas trabajadas.
    """
    data = request.json
    try:
        nombre = data["nombre"]
        horas = data["horas"]
        prolog.assertz(f"empleado({nombre}, {horas})")
        return jsonify({"message": "Empleado agregado exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
