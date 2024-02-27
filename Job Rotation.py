"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

fibonacci = [0, 1]  
while fibonacci[-1] < numero:  
    fibonacci.append(fibonacci[-1] + fibonacci[-2])  

if numero in fibonacci:
    print(fibonacci)
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(fibonacci)
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, 
na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal."""

faturamento = [[
	{"dia": 1,"valor": 22174.1664},
	{"dia": 2,"valor": 24537.6698},
	{"dia": 3,"valor": 26139.6134},
	{"dia": 4,"valor": 0.0},
	{"dia": 5,"valor": 0.0},
	{"dia": 6,"valor": 26742.6612},
	{"dia": 7,"valor": 0.0},
	{"dia": 8,"valor": 42889.2258},
	{"dia": 9,"valor": 46251.174},
	{"dia": 10,"valor": 11191.4722},
	{"dia": 11,"valor": 0.0},
	{"dia": 12,"valor": 0.0},
	{"dia": 13,"valor": 3847.4823},
	{"dia": 14,"valor": 373.7838},
	{"dia": 15,"valor": 2659.7563},
	{"dia": 16,"valor": 48924.2448},
	{"dia": 17,"valor": 18419.2614},
	{"dia": 18,"valor": 0.0},
	{"dia": 19,"valor": 0.0},
	{"dia": 20,"valor": 35240.1826},
	{"dia": 21,"valor": 43829.1667},
	{"dia": 22,"valor": 18235.6852},
	{"dia": 23,"valor": 4355.0662},
	{"dia": 24,"valor": 13327.1025},
	{"dia": 25,"valor": 0.0},
	{"dia": 26,"valor": 0.0},
	{"dia": 27,"valor": 25681.8318},
	{"dia": 28,"valor": 1718.1221},
	{"dia": 29,"valor": 13220.495},
	{"dia": 30,"valor": 8414.61}
]]


valores_faturamento = [dia["valor"] for dia in faturamento[0]]


valores_faturamento_com_faturamento = [valor for valor in valores_faturamento if valor != 0]


menor_valor = min(valores_faturamento_com_faturamento)
maior_valor = max(valores_faturamento_com_faturamento)


media_mensal = sum(valores_faturamento_com_faturamento) / len(valores_faturamento_com_faturamento)


dias_acima_da_media = sum(1 for valor in valores_faturamento_com_faturamento if valor > media_mensal)


print(f"Média mensal: R$ {media_mensal:5.2f}")
print(f"Menor valor de faturamento: R$ {menor_valor:5.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:5.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
que cada estado teve dentro do valor total mensal da distribuidora."""

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento.values())


percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento.items()}

print(f"Total mensal: R$ {total_mensal:5.2f}")
print("Percentual de representação de cada estado no valor total mensal:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

nome = "Elisangela"
nome_invertido = ''.join([nome[i] for i in range(len(nome) - 1, -1, -1)])
print(nome_invertido)