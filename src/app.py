from flask import Flask, jsonify
import logging

app = Flask(__name__)


@app.route("/user/<id>", methods=["GET"])
def index(id):
    try:
        return {"username": "John Doe", "email": "johndoe@email.com", "age": 25}

    except Exception as ex:
        logging.error(
            "An error has occurred while processing the request due to %s" % str(ex)
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
