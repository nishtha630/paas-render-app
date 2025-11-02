from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello from Cloud Platform as a Service (PaaS) - Render 🚀</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
