from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_dollar', methods=['POST'])
def calcular_dollar():
    real = float(request.form['real'])
    dollar = real / 5.68
    return render_template('index.html', dollar=dollar)

if __name__ == '__main__':
    app.run(debug=True)