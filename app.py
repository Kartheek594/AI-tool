from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    
    question = data.get("question")
    option = data.get("option")
    
    # Simple logic (replace with your AI logic)
    if "correct" in option.lower():
        return jsonify({"status": "correct"})
    else:
        return jsonify({"status": "wrong"})

if __name__ == "__main__":
    app.run(debug=True)
