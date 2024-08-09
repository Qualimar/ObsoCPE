from flask import Flask, request, render_template, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Fonction fictive pour simuler la conversion de configuration
def convert_config(config_text, brand, model):
    # Logique simplifiée de conversion
    return f"Configuration convertie pour {brand} {model}.\nConfig originale:\n{config_text}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'config_file' not in request.files:
        return 'Pas de fichier sélectionné', 400

    file = request.files['config_file']
    if file.filename == '':
        return 'Fichier non sélectionné', 400

    if file:
        config_text = file.read().decode('utf-8')
        brand = request.form['brand']
        model = request.form['model']

        converted_config = convert_config(config_text, brand, model)

        output_filename = os.path.join(UPLOAD_FOLDER, 'converted_config.txt')
        with open(output_filename, 'w') as f:
            f.write(converted_config)

        return send_file(output_filename, as_attachment=True, download_name='converted_config.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
