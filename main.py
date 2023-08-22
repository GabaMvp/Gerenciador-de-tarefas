class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        nova_tarefa = Tarefa(descricao)
        self.tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    def listar_tarefas(self):
        print("Lista de Tarefas:")
        for indice, tarefa in enumerate(self.tarefas, start=1):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{indice}. {tarefa.descricao} - {status}")

    def concluir_tarefa(self, indice):
        if 1 <= indice <= len(self.tarefas):
            tarefa = self.tarefas[indice - 1]
            tarefa.concluida = True
            print("Tarefa concluída!")

    def remover_tarefa(self, indice):
        if 1 <= indice <= len(self.tarefas):
            tarefa = self.tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa.descricao}' removida!")

def main():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            descricao = input("Digite a descrição da tarefa: ")
            gerenciador.adicionar_tarefa(descricao)
        elif escolha == 2:
            gerenciador.listar_tarefas()
        elif escolha == 3:
            indice = int(input("Digite o índice da tarefa a ser concluída: "))
            gerenciador.concluir_tarefa(indice)
        elif escolha == 4:
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            gerenciador.remover_tarefa(indice)
        elif escolha == 5:
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    
    main()