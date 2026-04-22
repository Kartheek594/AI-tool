from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS
CORS(app)

app = Flask(__name__)

client = OpenAI(api_key="YOUR_API_KEY")  # 🔑 put your key here

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    question = data["question"]
    option = data["option"]

    prompt = f"""
    Question: {question}
    Option: {option}
    Is this option correct? Answer only YES or NO.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    if "YES" in answer.upper():
        return jsonify({"status": "correct"})
    else:
        return jsonify({"status": "wrong"})

if __name__ == "__main__":
    app.run(debug=True)
