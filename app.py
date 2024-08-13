from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    constructeur_a = request.form['constructeurA']
    modele_a = request.form['modeleA']
    constructeur_b = request.form['constructeurB']
    modele_b = request.form['modeleB']
    config_file = request.files['configFile']

    # Placeholder for conversion logic
    # You would write logic to parse and convert the config file based on modele_a and modele_b
    # For now, let's assume the conversion is a simple passthrough
    converted_content = config_file.read()

    output_filename = f"{modele_b}_converted.txt"
    with open(output_filename, 'wb') as f:
        f.write(converted_content)

    return send_file(output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
