# Importa as classes necessárias
from usuario import Usuario
from filme import Filme
from conta import Conta

# Função principal que exibe o menu e controla o fluxo do programa
def menu():
    usuario = None  # Armazena o usuário logado (inicialmente nenhum)
    conta = None    # Armazena a conta associada ao usuário (histórico)

    # Loop infinito até o usuário escolher sair
    while True:
        # Exibe o menu estilizado
        print("""
──────────────────────────🏁MENU🏁──────────────────────────""")
        print("# 1 - Entrar🚪")
        print("# 2 - Cadastrar📋")
        print("# 3 - Buscar Filme🔎")
        print("# 4 - Ver Histórico📜")
        print("# 5 - Sair🔚")
        print("────────────────────────────────────────────────")

        opcao = input("Escolha uma opção: ")

        # Opção 1: Login
        if opcao == "1":
            usuario = Usuario.entrar_usuario()  # Tenta fazer login
            if usuario:
                conta = Conta(usuario)  # Cria conta (carrega histórico)

        # Opção 2: Cadastro
        elif opcao == "2":
            Usuario.cadastrar_usuario()  # Chama o método de cadastro

        # Opção 3: Buscar filme
        elif opcao == "3":
            if not usuario:
                print("Você precisa estar logado.")
            else:
                titulo = Filme.exibir_filme()  # Busca e exibe filme
                if titulo:
                    # Adiciona ao histórico (só se confirmar que assistiu)
                    conta.adicionar_ao_historico(titulo)

        # Opção 4: Ver histórico
        elif opcao == "4":
            if not usuario:
                print("Você precisa estar logado.")
            else:
                conta.exibir_historico()  # Mostra o histórico

        # Opção 5: Sair
        elif opcao == "5":
            print("Saindo...")
            break  # Encerra o loop

        # Opção inválida
        else:
            print("Opção inválida. Tente novamente.")

# Garante que o menu só seja executado se este arquivo for o principal
if __name__ == "__main__":
    menu()