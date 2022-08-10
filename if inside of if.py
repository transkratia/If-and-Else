# Nesse programa de if dentro de if, o usuário irá responder a várias
# perguntas para efetuar o login num dispositivo.

login = ("Deseja efetuar login? (S/N)")
if login == "S":
    user = input("Qual é o usuário? ")
    if user == "Transkratia":
        password = input("Qual é a senha? ")
        if password == "hello world":
            print("Acesso concedido.")
