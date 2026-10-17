from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form.get("amount")
    category = request.form.get("category")
    description = request.form.get("description")

    return f"Received: ₹{amount} | {category} | {description}"


if __name__ == "__main__":
    app.run(debug=True)
    