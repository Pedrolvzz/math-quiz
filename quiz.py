import random 

operadores = ["+", "-", "*", "/"]

print("=== QUIZ DE MATEMÁTICA ===")
print("Você terá 10 questões de matemática para responder.")
print("As operações podem ser: +, -, * e /")
print("Dificuldade: Nível Fácil")
print("Boa Sorte!")

perguntas = 0
acertos = 0

while perguntas < 10:
    print(f"Questão: {perguntas + 1}")
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)
    operador = random.choice(operadores)

    print(f"{numero1} {operador} {numero2} = ?")

    if operador == "+":
        resposta_correta = numero1 + numero2

    elif operador == "-":
        resposta_correta = numero1 - numero2

    elif operador == "*":
        resposta_correta = numero1 * numero2

    elif operador == "/":
        resposta_correta = numero1 / numero2

        if numero1 == 0 or numero2 == 0:
            print("Não é possível dividir por zero, gerando nova questão...")
            continue
            
    resposta_usuario = float(input("Digite sua resposta: "))
    perguntas += 1

    if resposta_usuario == resposta_correta:
        acertos = acertos + 1

print("=== RESULTADO ===")
print(f"Você acertou {acertos} de {perguntas} questões.")

if acertos >= 7:
    print("Parabéns! Você passou no quiz!")

else:
    print("Você não passou no quiz, tente novamente!")



