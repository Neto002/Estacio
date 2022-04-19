import os

# Tendo um arquivo de texto .txt, faça um script em Python que leia uma palavra e que verifique se esta palavra está no arquivo e quantas ocorrências dela tem no arquivo. Lembrando que a busca da palavra tem  de  ser  exata,  exemplo: se  a  busca  forpela  palavra “amor” e seu textotiver  a  palavra “amora”,  o programa irá contar, logo, isso deve ser evitado. (0,2pontos)

busca_palavra = input('Digite a palavra a ser buscada: ')

try:
    with open(os.path.join(os.getcwd(), 'Desenvolvimento Rápido Python', 'aula08', 'exercicio.txt'), 'r+') as arquivo:
        texto_arquivo = arquivo.read().split()

    qtd_busca = texto_arquivo.count(busca_palavra)

    print(f'A palavra amor apareceu {qtd_busca} vezes no arquivo.' if qtd_busca > 1 else f'A palavra amor apareceu {qtd_busca} vez no arquivo.' if qtd_busca == 1 else 'A palavra amor não apareceu no arquivo.')
    
except FileNotFoundError:
    print('O arquivo não foi encontrado.')
except Exception as erro:
    print(f'Ocorreu um erro: {erro}')


# Faça um script que leia um email e verifique as seguintes condições: todas os caracteres em minúsculo e sem pontuações, somente letras e números antes do @. Emitir uma mensagem se é email válido. (0,2 pontos)

try:
    email = input('Digite seu email: ').strip()
    if email == '':
        raise ValueError('E-mail inválido!')
    if '@' not in email:
        raise ValueError('Por favor, insira o @ no seu e-mail.')
    elif email != email.lower():
        raise ValueError('Por favor, insira seu e-mail em minúsculo.')
    elif not email[:email.index('@')].isalnum():
        raise ValueError('Por favor, insira apenas letras e números antes do @.')
    else:
        print('E-mail válido!')
except ValueError as erro:
    print(f'Erro: {erro}')

# Dado uma data informada separada como entrada (dia, mês e ano) e um horário informado separado (hora, minutos e segundos), imprima a data no formato “dia/mês/ano” e o horário no formato “hora:minutos:segundos” usando o método join. (0,2 pontos)

try:

    dados = {'dia': input('Digite o dia (dd): '), 'mes': input('Digite o mês (mm): '), 'ano': input('Digite o ano (aaaa): '), 'hora': input('Digite a hora (hh): '), 'minutos': input('Digite os minutos (mm): '), 'segundos': input('Digite os segundos (ss): ')}

    if not dados['dia'].isnumeric() or not dados['mes'].isnumeric() or not dados['ano'].isnumeric() or not dados['hora'].isnumeric() or not dados['minutos'].isnumeric() or not dados['segundos'].isnumeric():
        raise ValueError('Por favor, insira apenas números.')

    for chave in dados.keys():
        if len(dados[chave]) < 2:
            dados[chave] = f'0{dados[chave]}'

    data = str.join('/', [dados['dia'], dados['mes'], dados['ano']])
    horario = str.join(':', [dados['hora'], dados['minutos'], dados['segundos']])

    print(f'Data: {data}')
    print(f'Horário: {horario}')

except ValueError as erro:
    print(erro)

# Uma string é utilizada para representar uma das fitas de uma cadeia de DNA. Para tanto, as bases Adenina, Guanina, Citosina, Timina e Uracila são representadas pelas letras A, G, C, T e U, respectivamente. Deseja-se construir um programa em Python que dada uma sequência de DNA é fornecida a sequência de RNA-m equivalente de acordo com a transformação indicada na Tabela abaixo. (0,2 pontos)

try:
    dna = input('Digite a sequência de DNA: ').upper()
    if dna not in 'AGCT':
        raise ValueError('Por favor, insira apenas A, G, C, T ou U.')
    rna = dna.replace('A', 'U').replace('G', 'C').replace('C', 'G').replace('T', 'A')
    print(f'A sequência de RNA-m é: {rna}')
except ValueError as erro:
    print(erro)

# Uma biblioteca distribui um cartão magnético para que os alunos possam frequentá-la. A senha inicial, enviada  por  email,  é  gerada  automaticamente  a partir  da  data  de  nascimento  do  aluno ('dd/mm/aaaa') do  seguinte  modo: mm'$'dd(invertido)  +  '#'  +  dd'!'mm(invertido)  +  '\'+aaaa. Exemplo: Data  de nascimento:  25/10/1995. Resultado: 25$01#10!52\1995. Escreva  um  programa em  Python que  leia  o dia, mês e ano de nascimento de um aluno e retorne sua senha de acordo com as regras acima. (0,2 pontos)

try:
    dados = {'dia': input('Digite o dia (dd): '), 'mes': input('Digite o mês (mm): '), 'ano': input('Digite o ano (aaaa): ')}

    for chave in dados.keys():
        if len(dados[chave]) < 2:
            dados[chave] = f'0{dados[chave]}'

    data = str.join('/', [dados['dia'], dados['mes'], dados['ano']])

    print("A senha é: {}".format(dados['dia'] + "$" + dados['mes'][::-1] + "#" + dados['dia'] + "!" + dados['mes'][::-1] + "\\" + dados['ano']))

except ValueError as e:
    print(e)