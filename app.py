from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
	return { "status": "ok", "message": "Server is running" }, 200


if __name__ == "__main__":
	app.run()
