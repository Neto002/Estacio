#Ler 2 numeros e dizer qual é maior

#Python
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if (n1 > n2):
    print(f'O maior número entre eles é: {n1}')
elif (n1 < n2):
    print(f'O maior número entre eles é: {n2}')
else:
    print('Os números são iguais')

#C

'''
#include <stdio.h>

int main()
{
    int n1, n2 = 0;
    
    printf("Digite o primeiro número: ");
    scanf("%d", &n1);
    
    printf("Digite o segundo número: ");
    scanf("%d", &n2);
    
    if (n1 > n2) {
        printf("O maior número entre eles é %d", n1);
    } else if (n1 < n2) {
        printf("O maior número entre eles é %d", n2);
    } else {
        printf("Os números são iguais.")
    }

    return 0;
}
'''

#C++

'''
#include <iostream>
using namespace std;

int main()
{
    int n1, n2 = 0;
    
    cout << "Digite o primeiro número: ";
    cin >> n1;
    
    cout << "Digite o segundo número: ";
    cin >> n2;
    
    if (n1 > n2) {
        cout << "O maior número entre eles é " << n1;
    } else if (n1 < n2) {
        cout << "O maior número entre eles é " << n2;
    } else {
        cout << "Os números são iguais.";
    }

    return 0;
}
'''