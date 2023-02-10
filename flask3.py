from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
<form>
    <label>Primeiro nome:</label>
    <input  type="text"><br><br>
    <label>Segundo  Nome</label>
    <input  type="text" ><br><br>
    <input  type="submit" value="enviar">
</form>"""

app.run()