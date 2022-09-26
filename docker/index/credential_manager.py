from flask import Flask, request


app = Flask(__name__)


@app.route("/login.html", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return '<p>Submitted</p>'
    else:
        pass

    return '''
<p>Submitted</p>
'''


if __name__ == "__main__":
    app.run(debug=True)
