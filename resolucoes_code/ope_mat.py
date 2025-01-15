# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitar os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolher a operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Realizar a operação
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

# Exibir o resultado
print(f"O resultado da operação é: {resultado}")
