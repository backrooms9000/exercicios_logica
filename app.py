#Importar "subprocess" e "os" que permitem execultar comandos
import subprocess
import random

#numero = random.randint(1, 1000)

#baco de dados
database = {}
{
    "1": {"name": "Rex", "phone": "(21)3456789"},
    "120": { "name": "maria simpa", "phone": "marian@sirilampo" }
}
def cls():
    subprocess.run("cls", shell=True)

def new_contact():
    # cadastra novo contato
    # Limpa  a tela
    cls()
    print("[ AGENDA FURRECA - NOVO CONTATO ]")
    print("\nDiguite os dados do contato\n")

    # Recebe os dados do usuario

    #Recebe e valida o "name"
    while True:
        name = input("Nome: ")
        if name.strip():
            break
        print("-----", "Nome invalido! Digite novamente." " ,"-----")
        
        #Gera o ID aleatorio e nao repetido
    contact_id = str(random.randint(100, 1000))
    while contact_id in database:
        contact_id = str(random.randint(100, 1000))

    # recebe e valida o "phone"
    while True:
        phone = input("Telefone: ")
        if phone.strip():
            break
            print("-----", "telefone invalido! digite novamente>")
    contact = input(" Contato: ")

def list_contacts():
    # Limpa a tela
    cls()
    print("[ AGENDA FURRECA - LISTAR CONTATOS ]")
    print()
    print(len(database), "usuarios encontrados!")
    print()

    #loop para itear sobre os registros usando o metodo `dick.items()`
    for key, value in database.items():
        # Formata a saida
        print("ID:",key)
        print("\t.nome:", value['phone'])
        print("\t.contato:"), value["name"]
        print()

    input("tecle [Enter] para continuar")
    main()

    #...

def edit_contact():
    cls()
    print("[ AGENDA FURRECA - EDITAR CONTATO ]")

    print()
    key = input("Digite o ID do usuari0: ")

    print()
    print("ID:", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['phone'])
    print()

    input("tecle [Enter] para continuar")
    main()

def delete_contact():
    cls()
    print("[ AGENDA FURRECA - APAGAR CONTATO ]")

    import subprocess
    main()

  # programa principal
  def main(erro = str()):
    #main loop
    while true:
    cls()
    print("[ AGENDA FURRECA - MENU PRINCIPAL ]")
    print(erro)
    erro = str()
    # Debug
    print("\n", database)
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
            exit()
        case_:
            erro = "digite uma opcao valida!"
            main(erro)

# "Roda" o programa
main()