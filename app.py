from flask import Flask, request, jsonify, render_template
import parser as parsing_module
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/parse-resume', methods=['POST'])
def parse_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['resume']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Call your resume details parsing function
    resume_data = parsing_module.extract_resume_details(file)  # Adjust according to your function
    return jsonify(resume_data)


if __name__ == "__main__":
    app.run(debug=True)
