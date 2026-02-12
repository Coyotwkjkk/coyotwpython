agenda = []

def adcionar_pessoas():
    pessoa = {}

    nome = input("Adcionar nome de usuario: ")
    data = input("Adcionar data do usuario: ")

    pessoa["Nome"] = nome
    pessoa["Data"] = data

    agenda.append(pessoa)

    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")

def remover_pessoas():
    leitura = len(agenda)

    if leitura == 0:
        print("A lista está vazia.")
    else:
        

        for position, pessoa in enumerate(agenda, start=1):
            nome = pessoa["Nome"]
            data = pessoa["Data"]
            print(f"{position} - Nome: {nome} // Data: {data}")
            print()
        try:
            escolher_remover = int(input("Quem deseja remover? Digite a posição: "))

            if escolher_remover < 1 or escolher_remover > leitura:
                print("Posição inexsitente, tente novamente.")

            else:

                agenda.pop((escolher_remover - 1))
                print("Usuario removido com sucesso.")


        except:
            print("Opção inválida, tente novamente.") 


def listar_pessoas():
    leitura = len(agenda)
    
    if leitura == 0:
        print("A lista está vazia.")

    else:    
        for position, pessoa in enumerate(agenda, start=1):
            nome = pessoa["Nome"]
            data = pessoa["Data"]
            print(f"{position} - Nome: {nome} // Data: {data}")
            print()
def main():

    while True: 
        print("Menu Iniciar: ")
        print("1 - Adicionar usuario na lista")
        print("2 - Listar usuarios na lista")
        print("3 - Remover usuario da lista")
        print("4 - Sair")

        try:

            op = int(input("Escolha uma opção: 1/2/3 ou 4: "))

            
            if op == 1:
                adcionar_pessoas()
                
            elif op == 2:
                listar_pessoas()

            elif op == 3:
                remover_pessoas()

            elif op == 4:
                print("Saindo...")
                break

        except:
                print("Escolha invalida, tente novamente.")

if __name__ == "__main__" :
    main()