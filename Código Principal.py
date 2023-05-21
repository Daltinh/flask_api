from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para receber o webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Verifica o status do pagamento
    status = data.get('status')

    if status == 'approved':
        # Ação: Liberar acesso ao curso
        email = data.get('email')
        print(f"Liberar acesso do e-mail: {email}")

        # Ação: Enviar mensagem de boas-vindas
        send_welcome_message(email)

    elif status == 'rejected':
        # Ação: Enviar mensagem de pagamento recusado
        email = data.get('email')
        print(f"Enviar mensagem de pagamento recusado para o e-mail: {email}")

    elif status == 'refunded':
        # Ação: Remover acesso ao curso
        email = data.get('email')
        print(f"Remover acesso do e-mail: {email}")

    # Registra o webhook recebido
    register_webhook(data)

    return jsonify({'message': 'Webhook received'}), 200

# Função para enviar mensagem de boas-vindas
def send_welcome_message(email):
    print(f"Enviar mensagem de boas-vindas para o e-mail: {email}")

# Função para registrar o webhook 
def register_webhook(data):
    print("Registro do webhook:")
    print(data)
   

# Rota para autenticação de login
@app.route('/login', methods=['POST'])
def login():
    token = request.form.get('token')

    if token == 'uhdfaAADF123':
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401

# Rota para exibir as tratativas do sistema para cada usuário
@app.route('/tratativas', methods=['GET'])
def tratativas():
    user = request.args.get('user')
    tratativas = get_tratativas(user)
    return jsonify(tratativas), 200

# Função para obter as tratativas do banco de dados
def get_tratativas(user):
    tratativas = [
        {'user': 'fulano@email.com', 'tratativa': 'Liberar acesso'},
        {'user': 'fulano@email.com', 'tratativa': 'Enviar mensagem'},
        {'user': 'fulano@email.com', 'tratativa': 'Remover acesso'}
    ]

    if user:
        tratativas = [t for t in tratativas if t['user'] == user]

    return tratativas

if __name__ == '__main__':
    app.run(debug=True)

