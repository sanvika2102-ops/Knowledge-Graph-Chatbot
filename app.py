from flask import Flask, render_template, request, jsonify
from question_processor import answer_question

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()

    if not question:
        return jsonify({"answer": "Please enter a question."}), 400

    result = answer_question(question)
    return jsonify({"answer": result})

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Knowledge Graph chatbot is running."})

if __name__ == "__main__":
    app.run(debug=True)
