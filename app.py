from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

users_data = [
    {
        "id": 1,
        "name": "Paulo"
    },
    {
        "id": 2,
        "name": "Vitor"
    },
]


def response_users():
    return {"users": users_data}


@app.route('/')
def root():
    return "<h1>Api com Flask</h1>"


@app.route("/users")
def list_users():
    return response_users()


app.run(debug=True)
