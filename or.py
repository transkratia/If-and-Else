# Este programa questiona informações de uma série famosa de RPG.
# Caso o usuário responda com uma das duas melhores temporadas,
# o programa o parabeniza, se não, questiona o seu gosto.

aop = input("Qual é a sua temporada favorita? ")

if aop == "O Segredo Na Floresta" or aop == "O Segredo Na Ilha":
    print("Você tem bom gosto.")
else:
    print("Há temporadas melhores.")
