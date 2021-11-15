numero = str(input('Digite um número: ')).strip()

print(f'O número {numero} tem {len(numero)}', 'dígitos.' if len(numero) > 1 else 'dígito.')