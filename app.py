from flask import Flask

app = Flask(__name__)

@app.get("/health")
def health():
    return "Ok"

@app.get("/")
def home():
    return "Hello Word!" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
