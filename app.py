from flask import Flask, render_template, request, send_file
import os
from config_parser import convert_config

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

    # Lire le contenu du fichier de configuration
    config_data = config_file.read().decode('utf-8')

    # Convertir le fichier de configuration
    converted_content = convert_config(constructeur_a, modele_a, constructeur_b, modele_b, config_data)

    output_filename = f"{modele_b}_converted.txt"
    with open(output_filename, 'w') as f:
        f.write(converted_content)

    return send_file(output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
