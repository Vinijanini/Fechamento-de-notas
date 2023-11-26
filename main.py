alu = 0
sm = 0
def lin():
    print("-=" * 16)
def lista():
    lin()
    print("Aprovados")
    print(listaaprov)
    lin()
    print("reprovados")
    print(listareprov)
    lin()

listareprov = []
listaaprov = []
qntnotas = int(input('Quantas notas a serem consideredas:'))
lin()
med = int(input('A média para aprovação é:'))
lin()
while True:
    alu += 1
    al = str(input(f'{alu}ºAluno(a) - nome:'))
    lin()
    for nota in range(1, qntnotas+1):            ##insire as notas do aluno
        nt = float(input(f'{nota}º nota:'))
        sm += nt
        media = sm/qntnotas           #calcula média
    lin()
    print(f'{al} média: {media:.2f}')
    lin()
    soma = f"{al} - {media:.2f}"
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
lista()
with open('Média_dos_alunos.txt', "w") as arq: #cria o arquivo de texto com as informações
    arq.write("APROVADOS:")
    arq.write(f"{listaaprov}\n\n")
    arq.write("REPROVADOS:")
    arq.write(f"{listareprov}")
with open('Notas_dos_alunos', 'w') as arq2:
    arq2.write(f'')
input('Foi criado um arquivo txt para salvar as informações')
