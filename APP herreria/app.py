from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Productos
products = [
    {"id": 1, "objeto": "Casco de Hierro", "Valor": 500},
    {"id": 2, "objeto": "Armadura de malla", "Valor": 1200},
    {"id": 3, "objeto": "Guantes de Acero", "Valor": 300},
    {"id": 4, "objeto": "Espada Larga", "Valor": 800},
    {"id": 5, "objeto": "Escudo", "Valor": 700},
    {"id": 6, "objeto": "Hacha Grande", "Valor": 1200}
]

# Inventario
art = []

#Productos
@app.route("/products", methods=["GET"])
def get_products():
    """
    Obtener productos
    ---
    responses:
      200:
        description: Lista de productos disponibles
    """
    return jsonify(products)

# Ver inventario
@app.route("/art", methods=["GET"])
def get_art():
    """
    Obtener inventario
    ---
    responses:
      200:
        description: Lista de objetos en inventario
    """
    return jsonify(art)

# Agregar
@app.route("/art", methods=["POST"])
def add_to_art():
    """
    Agregar objeto al inventario
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            id:
              type: integer
    responses:
      200:
        description: Objeto agregado
      404:
        description: Producto no encontrado
    """
    data = request.json
    product_id = data.get("id")

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404

    art.append(product)

    return jsonify({
        "message": "Objeto agregado ",
        "art": art
    })

# Eliminar uno
@app.route("/art/<int:product_id>", methods=["DELETE"])
def remove_from_art(product_id):
    """
    Eliminar objeto del inventario
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Objeto eliminado
    """
    global art
    art = [p for p in art if p["id"] != product_id]

    return jsonify({
        "message": "Objeto removido",
        "art": art
    })

# Vaciar inventario
@app.route("/art", methods=["DELETE"])
def clear_art():
    """
    Vaciar inventario completo
    ---
    responses:
      200:
        description: Inventario vacio
    """
    global art
    art = []
    return jsonify({"message": "Inventario vacio"})

#Total
@app.route("/art/total", methods=["GET"])
def get_total():
    """
    Calcular total del inventario
    ---
    responses:
      200:
        description: Total calculado
    """
    total = sum(p["Valor"] for p in art)

    return jsonify({"total": total})


if __name__ == "__main__":
    app.run(debug=True)