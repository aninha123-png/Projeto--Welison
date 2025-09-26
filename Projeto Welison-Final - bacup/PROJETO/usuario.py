# Importa o módulo json para manipular dados em arquivos JSON
import json

# Classe Usuario: responsável por gerenciar cadastro, login e persistência dos dados de usuários
class Usuario:
    # Nome do arquivo onde os dados dos usuários serão armazenados
    _arquivo = "usuario.json"

    # Construtor da classe: recebe nome e email e armazena como atributos privados
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    # Método para acessar o nome do usuário
    def nome(self):
        return self.__nome

    # Método para acessar o email do usuário
    def email(self):
        return self.__email

    # Método que define como o objeto será exibido ao ser convertido em string
    def __str__(self):
        return f"{self.__nome} ({self.__email})"

    # Salva a lista de usuários no arquivo JSON
    @classmethod
    def salvar_usuario(cls, usuarios):
        with open(cls._arquivo, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)  # Salva com indentação e acentos corretos

    # Carrega os usuários do arquivo JSON
    @classmethod
    def carregar_usuarios(cls):
        #Abre em modo "a" (append) para garantir que o arquivo exista
        open(cls._arquivo, "a", encoding="utf-8").close()

        # Abre em modo leitura para carregar os dados
        with open(cls._arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()  # Remove espaços e quebras de linha
            if conteudo == "":           # Se estiver vazio, retorna lista vazia
                return []
            return json.loads(conteudo)  # Converte o JSON para uma lista de dicionários

    # Método para cadastrar um novo usuário
    @classmethod
    def cadastrar_usuario(cls):
        print("Cadastro de novo usuário:\n")

        # Solicita nome e valida se não está vazio
        nome = input("Nome: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio.")
            return

        # Solicita email e converte para minúsculas
        email = input("Email: ").strip().lower()

        # Validação de email sem usar endswith (verifica se termina com '@gmail.com')
        if len(email) <= 10 or email[-10:] != "@gmail.com":
            print("❌ Erro: O e-mail deve ser do Gmail (@gmail.com) e conter um nome antes do @.")
            return

        # Carrega os usuários existentes
        usuarios = cls.carregar_usuarios()

        # Verifica se o e-mail já está cadastrado
        for u in usuarios:
            if u["Email"].lower() == email:
                print("❌ Erro: Já existe um usuário com esse e-mail.")
                return

        # Cria novo usuário e adiciona à lista
        novo_usuario = {"Nome": nome, "Email": email}
        usuarios.append(novo_usuario)

        # Salva a lista atualizada
        cls.salvar_usuario(usuarios)
        print("✅ Usuário cadastrado com sucesso!")

    # Método para login (entrada do usuário)
    @classmethod
    def entrar_usuario(cls):
        # Solicita o e-mail do usuário
        email = input("Digite seu email: ").strip().lower()

        # Validação de domínio do e-mail
        if len(email) <= 10 or email[-10:] != "@gmail.com":
            print("❌ Erro: O e-mail deve ser do Gmail (@gmail.com).")
            return None

        # Carrega a lista de usuários
        usuarios = cls.carregar_usuarios()

        # Procura o e-mail na lista
        for usuario in usuarios:
            if usuario["Email"].lower() == email:
                print(f"Bem-vindo, {usuario['Nome']}!")
                # Retorna um objeto da classe Usuario
                return Usuario(usuario["Nome"], usuario["Email"])

        # Caso o e-mail não seja encontrado
        print("Usuário não encontrado.")
        return None
