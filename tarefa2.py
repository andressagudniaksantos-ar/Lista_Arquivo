     Abre o arquivo no modo "r" ( read/leitura )
   with open("meu_diario .txt", "r") as diario:
    conteudo = diario.read()
    print("--- Conteudo do Diario ---")
    print(conteudo)
except FileNotFoundError:
   print("O arquivo "meu_diario .txt ainda nao existe . Rode o
exercicio 1 primeiro.")