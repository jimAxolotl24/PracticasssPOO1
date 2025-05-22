from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Hola mundo :3 😈"

if __name__ == "__main__":
    app.run(debug=True)

# * se vuelve chango * 
# me vuelvo chango