import os

usuarios = []

while True:
    print("\n1 - Exibir lista de usuários.")
    print("2 - Cadastrar novo usuário.")
    print("3 - Pesquisar usuário cadastrado.")
    print("4 - Alterar dados do usuário cadastrado.")
    print("5 - Excluir usuário cadastrado.")
    print("6 - Sair do Programa.")

    opcao = input("\nOpção do Usuário: ")

    os.system("cls")

    match opcao:
        case "1":
            if usuarios:
                for i, usuario in (enumerate)(usuarios):
                    print(f"\nÍndice\Número {i}:")
                    for chave, valor in usuario.items():
                        print(f"{chave}: {valor}")
            else:
                print("Nenhum usuário cadastrado.")
                
        case "2":
            try:
                nome = input("Informe o nome completo: ")
                data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
                cpf = input("Informe o CPF (somente números): ")
                profissao = input("Informe a profissão: ")
                email = input("Informe o e-mail: ")
                endereco = input("Informe o endereço: ")
                telefone = input("Informe o telefone: ")

                usuario = {
                    "Nome": nome,
                    "Data de Nascimento": data_nascimento,
                    "CPF": cpf,
                    "Profissão": profissao,
                    "E-mail": email,
                    "Endereço": endereco,
                    "Telefone": telefone
                }
                
                usuarios.append(usuario)
                print("Usuário cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possível cadastrar o usuário: {e}")
                
        case "3":
            nome_procurado = input("Informe o nome completo a pesquisar: ")
            encontrados = [usuario for usuario in usuarios if usuario["Nome"].lower() == nome_procurado.lower()]
            
            if encontrados:
                for usuario in encontrados:
                    for chave, valor in usuario.items():
                        print(f"{chave}: {valor}")
                    print("\n")
            else:
                print(f"Usuário {nome_procurado} não encontrado.")
                
        case "4":
            try:
                indice = int(input("Informe o índice do usuário a alterar: "))
                if 0 <= indice < len(usuarios):
                    usuario = usuarios[indice]
                    print("\nDados atuais do usuário:")
                    for chave, valor in usuario.items():
                        print(f"{chave}: {valor}")

                    usuario["Nome"] = input("Informe o novo nome completo: ")
                    usuario["Data de Nascimento"] = input("Informe a nova data de nascimento (DD/MM/AAAA): ")
                    usuario["CPF"] = input("Informe o novo CPF (somente números): ")
                    usuario["Profissão"] = input("Informe a nova profissão: ")
                    usuario["E-mail"] = input("Informe o novo e-mail: ")
                    usuario["Endereço"] = input("Informe o novo endereço: ")
                    usuario["Telefone"] = input("Informe o novo telefone: ")

                    print("Dados do usuário alterados com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar o usuário: {e}")
                
        case "5":
            try:
                indice = int(input("Informe o índice do usuário a excluir: "))
                if 0 <= indice < len(usuarios):
                    del usuarios[indice]
                    print("Usuário excluído com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível excluir o usuário: {e}")
                
        case "6":
            print("Saindo do programa...")
            break
            
        case _:
            print("Opção inválida, digite uma opção válida.\n")
