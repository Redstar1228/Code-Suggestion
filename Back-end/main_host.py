from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

suggestions = {
    "for i in range": "    print(i)",
    "for item in": "    print(item)",
    "while True:": "    break",

    "if x > 0:": "    print('Positive')",
    "if x < 0:": "    print('Negative')",
    "if": "    pass",
    "else:": "    pass",
    "elif": "    pass",

    "def": "    pass",
    "def __init__": "        pass",
    "return": "    return None",

    "try:": "    except Exception as e:\n        print(e)",
    "print(": "    # prints the output",
    "input(": "    # gets user input",

    "class ": "    def __init__(self):\n        pass",

    "my_list = [": "    for item in my_list:\n        print(item)",
    "my_dict = {": "    for key, value in my_dict.items():\n        print(key, value)",
    "my_set = {": "    for val in my_set:\n        print(val)",

    "import os": "    print(os.getcwd())",
    "import math": "    print(math.pi)",

    "[x for x in": "    # list comprehension",
    "{x: x**2 for x in": "    # dict comprehension"
}

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.get_json()
    code = data.get("code", "").strip()

    response = ""
    for pattern, suggestion in suggestions.items():
        if code.startswith(pattern):
            response = suggestion
            break

    return jsonify({"suggestion": response or "# No suggestion found"})

if __name__ == "__main__":
    app.run(debug=True)
