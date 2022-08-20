# Nesse programa de if dentro de if, o usuário irá responder a várias
# perguntas para efetuar o login num dispositivo.

login = input("Deseja efetuar login? (S/N) ")

if login == "S":
    user = input("Qual é o usuário? ")
    if user == "angelofthenight":
        password = input("Qual é a senha? ")
        if password == "cris":
            print("Acesso concedido.")
