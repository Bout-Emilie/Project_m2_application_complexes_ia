from flask import * 

app = Flask(__name__)

@app.route("/health", methods=['POST'])

def notes_list():
    value = request.form['value']
    print(request.url)
    print('value = ' + value)
    return value

if __name__ == "__main__":
    app.run(debug=True)