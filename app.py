from flask import Flask, render_template
import json
import os
app = Flask(__name__)

@app.route('/')
def home():
    json_url = os.path.join(app.static_folder, 'data/data.json')
    with open(json_url) as f:
        data = json.load(f)
    return render_template('interface.html',
        product=data)

if __name__ == '__main__':
    app.run(debug=True)
