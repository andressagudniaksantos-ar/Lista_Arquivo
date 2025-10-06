 4) Abre o arquivo no modo "w" para comecar uma lista nova
with open ("tarefas.txt ", "w") as arquivo_tarefas :
    print ("Por favor, digite 3 tarefas a serem feitas:")
    for i in range(3) :
      tarefa = input(f"Tarefa {i + 1}: ")
      arquivo_tarefas.write(tarefa + "\n")

print ("\ nLista de tarefas foi salva em ’tarefas .txt ’!")






5)print ("--- Minha Lista de Tarefas ---")
  try:
      with open ("tarefas.txt ", "r") as arquivo_tarefas :
          numero_tarefa = 1
          for tarefa in arquivo_tarefas:
              # O f- string ajuda a formatar a saida
              print (f"{ numero_tarefa }. {tarefa.strip ()}")
              numero_tarefa += 1 # O mesmo que numero_tarefa =
    numero_tarefa + 1
except FileNotFoundError :
    print("Arquivo ’tarefas.txt ’ nao encontrado . Rode o exercicio 4
primeiro .")
