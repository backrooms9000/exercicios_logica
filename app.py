import subprocess
import random

#numero = random.randint(1, 1000)

#baco de dados
database = {
    "1": { "name": "Rex", "phone": "(21)3456789", "}`,
    "120": { "name": "maria simpa", "contact": "(21)9876203" },
def cls():
    subprocess.run("cls", shell=True)

def new_contact():
    cls()
    print("[ AGENDA FURRECA - NOVO CONTATO ]")

    print("\nDiguite os dados do contato\n")

    name + input(" ")

    #...

def list_contacts():
    cls()
    print("[ AGENDA FURRECA - LISTAR CONTATOS ]")

    #...

def edit_contact():
    cls()
    print("[ AGENDA FURRECA - EDITAR CONTATO ]")

    #...

def delete_contact():
    cls()
    print("[ AGENDA FURRECA - APAGAR CONTATO ]")

    #...

  # programa principal
  def main(erro = str()):
    #main loop
    while true:
    cls()
    print("[ AGENDA FURRECA - MENU PRINCIPAL ]")
    print(erro)
    erro = str()
    print('''
Opcoes:

1-novo contato
2-listar contatos
3-Editar contato
4- Apagar contato
0-Sir do programa
    ''')

        opcao = imput("Escolha uma opcao: ")

        match opcao:
        case 1:
           new_contact()
        case 2:
           list_contacts()
        case 3:
           edit_contact()
        case 0:
            cls()
            print("\Acabou!")
            exist()
        case_:
            erro = "digite uma opcao valida!"
            main(erro)

# "Roda" o programa
main()