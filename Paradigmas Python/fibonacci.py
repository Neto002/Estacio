n = int(input("Quantos números da série deseja mostrar? "))
termo_1 = 0
termo_2 = 1

print(termo_1)
print(termo_2)

for i in range(3,n+1):
    termo_atual = termo_1 + termo_2
    print(termo_atual)
    termo_1 = termo_2
    termo_2 = termo_atual