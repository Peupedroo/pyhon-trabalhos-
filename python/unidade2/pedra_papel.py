import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    
    # Solicitar a escolha do usuário
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    
    if escolha_usuario not in opcoes:
        print("Escolha inválida. Tente novamente.")
        return
    
    # Escolha aleatória do computador
    escolha_computador = random.choice(opcoes)
    print(f"Computador escolheu: {escolha_computador}")
    
    # Determinar o vencedor
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

# Executar o jogo
pedra_papel_tesoura()