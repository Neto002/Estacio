S = [2*x for x in range(101) if x%2==0]
A = [x**2+x+1 for x in range(100) if x%2==0]
print(S)
print(A)

#Transformar as listas na sintaxe Haskell abaixo em list comprehension em python:
# a) [x | x <- [1..10]] -> numeros de 1 a 100
# b) [x | x <- [1,22,43..200]] -> numeros de 1 a 200, passo 21
# c) [x^2 | x<-[10..20], odd x] -> quadrado dos impares de 10 a 20

