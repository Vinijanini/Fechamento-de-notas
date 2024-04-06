alu, sm = 0, 0
listareprov, listaaprov = [], []
def lin():
    print("-=" * 16)

while True:
    try:
        qntnotas = int(input('Quantas notas a serem consideredas:'))
        break
    except ValueError:
        print('Digite um número!')
lin()
while True:
    try:
        med = int(input('A média para aprovação é:'))
        break
    except ValueError:
        print('Digite um número!')
lin()
while True:
    alu += 1
    al = str(input(f'{alu}ºAluno(a) - nome:')).title()
    lin()
    for nota in range(1, qntnotas+1):            ##insire as notas do aluno
        while True:
            try:
                nt = float(input(f'{nota}º nota:'))
                break
            except ValueError:
                print('Digite uma nota válida!')
        sm += nt
        media = sm/qntnotas           #calcula média
    lin()
    print(f'Aluno: {al} - média: {media:.2f}')
    lin()
    soma = f"{al} - Média: {media:.2f}"
    if media < med:
        listareprov.append(soma) #se a média for abaixo, adicione o aluno na lista de reprovados
    else:
        listaaprov.append(soma) #caso contrário, coloque nos aprovados
    sm = 0
    media = 0
    cont = str(input('Continuar?[s/n]:')).lower()     ##pergunta se deseja avaliar mais um aluno
    lin()
    while cont not in "sn":
        print('Opção inválida')
        cont = str(input('Continuar?[s/n]:')).lower()  ##possivel erro do clinte
        lin()
    if cont == "n":
        break
print('Aprovados')
for al in listaaprov:
    print(al)
lin()
print('Reprovados')
for al in listareprov:
    print(al)
lin()
with open('Média_dos_alunos.txt', "w") as arq: #cria o arquivo de texto com as informações
    arq.write("APROVADOS:\n")
    for al in listaaprov:
        arq.write(f"{al}\n")
    arq.write('-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
    arq.write("REPROVADOS:\n")
    for al in listareprov:
        arq.write(f"{al}\n")
input('Arquivo "Média_dos_alunos.txt" foi criado para salvar os resultados')