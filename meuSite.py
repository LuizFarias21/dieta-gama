from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario = nome_usuario)

def perguntar(prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "text" },
    messages=[
         {"role": "system", "content": "Responda sendo irônico"},
         {"role": "user", "content": prompt}
          ]
    )
    return response.choices[0].message.content

@app.route("/chatgpt", methods=['POST', 'GET'])
def chatgpt():
	if request.method == 'POST':
		prompt = request.form['questao']
		resposta = perguntar(prompt)
		return render_template('questao.html', resposta = resposta)
	return render_template('questao.html')

if __name__ == '__main__':
    app.run(debug=True)

print('teste')