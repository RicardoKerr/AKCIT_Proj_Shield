from flask import Flask, render_template, request

from generator import generate_password

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", password=None, error=None)


@app.post("/generate")
def generate():
    try:
        length = int(request.form.get("length", "12"))
        use_uppercase = request.form.get("uppercase") == "on"
        use_lowercase = request.form.get("lowercase") == "on"
        use_numbers = request.form.get("numbers") == "on"
        use_symbols = request.form.get("symbols") == "on"

        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_symbols=use_symbols,
        )

        return render_template("index.html", password=password, error=None)
    except ValueError as exc:
        return render_template("index.html", password=None, error=str(exc)), 400


if __name__ == "__main__":
    app.run(debug=True)
