from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200


# ---------- ADD ----------
@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    return jsonify({
        "operation": "addition",
        "a": a,
        "b": b,
        "result": a + b
    }), 200


# ---------- SUBTRACT ----------
@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    return jsonify({
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": a - b
    }), 200


# ---------- MULTIPLY ----------
@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    return jsonify({
        "operation": "multiplication",
        "a": a,
        "b": b,
        "result": a * b
    }), 200


# ---------- DIVIDE ----------
@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400

    return jsonify({
        "operation": "division",
        "a": a,
        "b": b,
        "result": a / b
    }), 200


if __name__ == "__main__":
    app.run(debug=True)