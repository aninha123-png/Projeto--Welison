# Importa json para manipular o arquivo de histórico dos filmes
import json
# Importa os para verificar se o arquivo existe no sistema
import os

# Importa a classe Usuario, que será associada a cada conta
from usuario import Usuario

# Define a classe Conta, responsável por gerenciar o histórico de filmes do usuário
class Conta:
    # Define o nome do arquivo onde o histórico será salvo
    _arquivo = "conta.json"

    # Construtor da classe: inicializa com um usuário e carrega o histórico
    def __init__(self, usuario: Usuario):
        self.__usuario = usuario                          # Armazena o objeto Usuario
        self.__email = usuario.email()                    # Usa o e-mail como identificador único
        self.__historico = self.carregar_historico_usuario()  # Carrega o histórico do usuário (ou lista vazia)

    # Adiciona um filme ao histórico, após confirmar se o usuário já assistiu
    def adicionar_ao_historico(self, titulo_filme):
        # Pergunta se o usuário já assistiu o filme
        assistiu = input("Já assistiu esse filme? [s/n] ").strip().lower()

        # Verifica se a resposta foi 's' ou 'sim'
        if assistiu == 's' or assistiu == 'sim':
            print("Filme assistido com sucesso!")
            print(f"Filme '{titulo_filme}' adicionado ao histórico.")
            self.__historico.append(titulo_filme)      # Adiciona à lista de histórico do usuário
            self.salvar_historico_usuario()            # Salva no arquivo JSON
        else:
            print("Esperamos que goste quando assistir!")

    # Exibe o histórico de filmes assistidos do usuário
    def exibir_historico(self):
        if not self.__historico:                       # Verifica se o histórico está vazio
            print("Seu histórico está vazio.")
        else:
            print("\n📜 Histórico de filmes assistidos:")
            for titulo in self.__historico:            # Exibe cada título no histórico
                print(f" - {titulo}")

    # Salva o histórico do usuário atual no arquivo JSON
    def salvar_historico_usuario(self):
        historico_geral = self.carregar_todos_historicos()  # Carrega todos os históricos existentes

        # Procura se o usuário já existe no arquivo
        for conta in historico_geral:
            if conta["Email"] == self.__email:
                conta["Historico"] = self.__historico   # Atualiza o histórico do usuário
                break
        else:
            # Se o usuário ainda não estiver registrado, adiciona novo
            historico_geral.append({
                "Email": self.__email,
                "Historico": self.__historico
            })

        # Salva todos os dados de volta no arquivo
        with open(self._arquivo, "w", encoding="utf-8") as f:
            json.dump(historico_geral, f, indent=4, ensure_ascii=False)

    # Carrega o histórico de filmes apenas do usuário atual
    def carregar_historico_usuario(self):
        historico_geral = self.carregar_todos_historicos()  # Carrega todos os históricos

        # Procura o histórico do usuário atual
        for conta in historico_geral:
            if conta["Email"] == self.__email:
                return conta.get("Historico", [])       # Retorna o histórico, ou uma lista vazia
        return []  # Se o usuário não existir no arquivo, retorna lista vazia

    # Método de classe que carrega todos os históricos salvos no arquivo JSON
    @classmethod
    def carregar_todos_historicos(cls):
        # Verifica se o arquivo existe. Se não, cria um novo com lista vazia
        if not os.path.exists(cls._arquivo):
            with open(cls._arquivo, "w", encoding="utf-8") as f:
                json.dump([], f)  # Cria um arquivo JSON com lista vazia como conteúdo inicial

        # Abre e carrega o conteúdo do arquivo
        with open(cls._arquivo, "r", encoding="utf-8") as f:
            return json.load(f)  # Retorna os dados carregados do arquivo
