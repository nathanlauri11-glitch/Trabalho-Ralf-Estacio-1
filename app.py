# Lista global para simular o banco de dados na memoria
lista_alunos = []


def cadastrar():
    print("\n--- CADASTRO DE ALUNO ---")
    nome = input("Digite o nome do aluno: ")
    disciplina = input("Digite a disciplina: ")
    nota_str = input("Digite a nota: ")

    if not nome or not disciplina or not nota_str:
        print("Erro: Todos os campos sao obrigatorios!")
        return

    try:
        nota = float(nota_str)
        aluno = {"nome": nome, "disciplina": disciplina, "nota": nota}
        lista_alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
    except ValueError:
        print("Erro: A nota precisa ser um numero valido (Ex: 7.5).")


def listar():
    print("\n--- LISTA DE ALUNOS REGISTRADOS ---")
    if len(lista_alunos) == 0:
        print("Nenhum aluno cadastrado ate o momento.")
        return

    for i, aluno in enumerate(lista_alunos, start=1):
        print(
            f"ID: {i} | Nome: {aluno['nome']} | Disciplina: {aluno['disciplina']} | Nota: {aluno['nota']}"
        )


# --- MENU PRINCIPAL DO PROGRAMA ---
while True:
    print("\n=========================")
    print("      SISTEMA DE NOTAS   ")
    print("=========================")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saindo do programa... Ate logo!")
        break
    else:
        print("Opcao invalida! Tente novamente.")
