from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        df = pd.read_csv(file)
        # Perform data analysis here
        summary = df.describe().to_html()
        return render_template('result.html', summary=summary)
    return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(debug=True)
