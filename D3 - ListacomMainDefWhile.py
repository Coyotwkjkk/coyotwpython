agenda = []

def add_peoples(lista):
    name = input("Digite o nome: ")
    data = input("Digite a data: ")
    lista.append((name, data))
    print(f"Nome: {name} / Data: {data}.")
    print("Usuario adcionado com sucesso!")

def remove_people(identify):
    leitura = len(agenda)

    if leitura == 0:
        print("A lista está vázia.")

    elif leitura >= 1:

        for position, (name, data) in enumerate(agenda, start= 1):
            print(f"{position} - Name: {name} / Data: {data}")

        remove_this = int(input("\nQuem você deseja remover? \nDigite o número: "))
        
        agenda.pop((remove_this - 1))

    else: 
        print("Opção invalida!")

def listar_pessoas():
    contagem = len(agenda)

    if contagem == 1:
        print(f"Temos exatamente {contagem} pessoa na lista!")
    
    elif contagem >= 2:
        print(f"Temos exatamente {contagem} pessoas na lista!")

    else:
        print("Não temos ninguem na lista.")

    for name, data in agenda:
        print(f"Nome: {name} / Data: {data}.")
    
def main():

    while True:

        print("1 - Adcionar pessoas")
        print("2 - Remover pessoas")
        print("3 - Listar pessoas")
        print("4 - Sair")

        op = input("Escolha um numero: ")

        if op == "1":
            add_peoples(agenda)

        elif op == "2":
            remove_people(agenda)

        elif op == "3":
            listar_pessoas()

        elif op == "4":
            print("Saindo...")
            break

        else:
            print("Opção invalida!")
main()