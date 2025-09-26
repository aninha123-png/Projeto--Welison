# Importa o módulo json para leitura de arquivos no formato JSON
import json

# Define a classe Filme, responsável por carregar e exibir informações de filmes
class Filme:
    # Nome do arquivo onde os dados dos filmes estão salvos
    __arquivo = "filmes.json"

    # Método de classe que carrega todos os filmes do arquivo JSON
    @classmethod
    def carregar_filmes(cls):
        # Abre o arquivo 'filmes.json' no modo leitura com codificação UTF-8
        with open(cls.__arquivo, "r", encoding="utf-8") as f:
            return json.load(f)  # Converte o conteúdo JSON para uma lista de dicionários e retorna

    # Método de classe que busca um filme pelo título informado pelo usuário
    @classmethod
    def exibir_filme(cls):
        # Solicita ao usuário o título do filme
        titulo_input = input("Digite o título do filme: ").strip().lower()

        # Carrega a lista de filmes do arquivo
        filmes = cls.carregar_filmes()

        # Percorre todos os filmes carregados
        for filme in filmes:
            # Compara o título do filme (ignorando espaços e maiúsculas/minúsculas)
            if filme["titulo"].strip().lower() == titulo_input:
                # Exibe os detalhes do filme encontrado
                print("\n🎬 Filme encontrado:")
                print(f"Título: {filme['titulo']}")
                print(f"Gênero: {filme['genero']}")
                print(f"Ano: {filme['ano']}")
                # Mostra o link de streaming se existir, senão exibe "Indisponível"
                print(f"Link de streaming: {filme.get('link_streaming', 'Indisponível')}")
                # Mostra a descrição se existir, senão exibe "Sem descrição"
                print(f"Descrição: {filme.get('descricao', 'Sem descrição')}")
                return filme["titulo"]  # Retorna apenas o título do filme (usado para adicionar ao histórico)

        # Se nenhum filme for encontrado com o título informado
        print("Filme não encontrado.")
        return None  # Indica que nenhum filme foi retornado
