## Aula de GitHub

alunos = []
while True:

    nome =  str(input('Digite o seu nome: '))
    alunos.append(nome)
    opcao = ''

    if 'S' != opcao != 'N':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()

    if opcao == 'N':
        break 
for a in alunos        
    print(f'A lista de alunos participantes é : {a}')   
