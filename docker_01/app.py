from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML template using render_template_string
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h2>Enter a number to generate its multiplication table:</h2>
    <form method="post">
        <input type="number" name="number" required>
        <button type="submit">Generate</button>
    </form>
    {% if table %}
        <h3>Table of {{ number }}</h3>
        <ul>
        {% for row in table %}
            <li>{{ row }}</li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    table = None
    number = None
    if request.method == "POST":
        number = int(request.form.get("number"))
        table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
    return render_template_string(html_form, table=table, number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
