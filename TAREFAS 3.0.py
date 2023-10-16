# Importações
import csv  # Importação para trabalhar com aquivos CSV.
import datetime # Importação para trabalhar com data e horas.
import os # Importação que interage com o sistema operacional.


# Executa o limpeza da tela.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Classes:
class Tarefa:
    # Faz a montagem da tarefa.
    def __init__(self, titulo, descricao, data_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.concluida = False
        
    # Marca como concluida.
    def marcar_como_concluida(self):
        self.concluida = True
        
    # Marca como pendente.
    def marcar_como_pendente(self):
        self.concluida = False
        
    # Integra os novos dados substituindo os antigos.
    def atualizar(self, novo_titulo, nova_descricao, nova_data_vencimento):
        self.titulo = novo_titulo
        self.descricao = nova_descricao
        self.data_vencimento = nova_data_vencimento

class GerenciadorTarefas:
    # Constrói as bases de dados e listas.
    def __init__(self):
        self.tarefas_gerais = []
        self.nome_arquivo = 'base.csv'
        self.carregar_tarefas()
        
    # Faz a adição da tarefa nova à sua lista correspondente.
    def adicionar_tarefa(self, titulo, descricao, data_vencimento, status):
        tarefa = Tarefa(titulo, descricao, data_vencimento)
        if status == 'concluida':
            tarefa.marcar_como_concluida()
        self.tarefas_gerais.append(tarefa)
    
    # imprime na tela todas as tarefas gravadas em memória.     
    def listar_tarefas(self, concluidas=False):
        tarefas_filtradas = [tarefa for tarefa in self.tarefas_gerais if tarefa.concluida == concluidas]

        if not tarefas_filtradas:
            print("\nLista de tarefas concluídas está vazia.\n" if concluidas else "\nLista de tarefas pendentes está vazia.\n")
        else:
            for idx, tarefa in enumerate(tarefas_filtradas, start=1):  # Imprime informações sobre cada tarefa
                print(f"Tarefa {idx}:\n")
                print(f"Titulo: {tarefa.titulo}")
                print(f"Descrição: {tarefa.descricao}")
                print(f"Data de vencimento: {tarefa.data_vencimento} ")
                print(f"Concluída: {'sim' if tarefa.concluida else 'não'}")
                print("-" * 20)

    # imprime na tela as tarefas pendentes gravadas em memória e se solicitado, inicia o processo de mudança de status.
    def listar_tarefas_pendentes(self):
        limpar_tela()
        while True:
            print("\nTarefas Pendentes:\n")
            tarefas_pendentes = [i for i, tarefa in enumerate(self.tarefas_gerais) if not tarefa.concluida]

            if not tarefas_pendentes:
                print("Não há tarefas pendentes.\n")
                break

            for idx, tarefa_idx in enumerate(tarefas_pendentes, start=1):
                tarefa = self.tarefas_gerais[tarefa_idx]
                print(f"{idx} - {tarefa.titulo}")
                print(f"Descrição: {tarefa.descricao}")
                print(f"Data de vencimento: {tarefa.data_vencimento} ")
                print("-" * 20)

            print("\nDigite o número da tarefa que deseja marcar como concluída ou 0 para voltar ao menu principal.")

            N_tarefa_escolhida = -1
            N_tarefa = input("\nDigite o número da tarefa: ")

            if N_tarefa.isdigit():
                N_tarefa_escolhida = int(N_tarefa)
                if N_tarefa_escolhida == 0:
                    limpar_tela()
                    break
                elif 1 <= N_tarefa_escolhida <= len(tarefas_pendentes):
                    limpar_tela()
                    tarefa_idx = tarefas_pendentes[N_tarefa_escolhida - 1]
                    self.marcar_como_concluida(tarefa_idx)
                    break
                else:
                    limpar_tela()
                    print(f"Tarefa {N_tarefa} não encontrada. Verifique o número da tarefa.\n")
            else:
                limpar_tela()
                print("\nDigite somente números e apenas um número!\n")

    # imprime na tela as tarefas concluídas gravadas em memória e se for solicitada inicia o processo de mudança de status. 
    def listar_tarefas_concluidas(self):
        limpar_tela()
        while True:
            print("\nTarefas Concluídas:\n")
            tarefas_concluidas = [i for i, tarefa in enumerate(self.tarefas_gerais) if tarefa.concluida]

            if not tarefas_concluidas:
                print("Não há tarefas concluídas.\n")
                break

            for idx, tarefa_idx in enumerate(tarefas_concluidas, start=1):
                tarefa = self.tarefas_gerais[tarefa_idx]
                print(f"{idx} - {tarefa.titulo}")
                print(f"Descrição: {tarefa.descricao}")
                print(f"Data de vencimento: {tarefa.data_vencimento} ")
                print("-" * 20)

            print("\nDigite o número da tarefa que deseja marcar como pendente ou 0 para voltar ao menu principal.")

            N_tarefa_escolhida = -1
            N_tarefa = input("\nDigite o número da tarefa: ")

            if N_tarefa.isdigit():
                N_tarefa_escolhida = int(N_tarefa)
                if N_tarefa_escolhida == 0:
                    limpar_tela()
                    break
                elif 1 <= N_tarefa_escolhida <= len(tarefas_concluidas):
                    limpar_tela()
                    tarefa_idx = tarefas_concluidas[N_tarefa_escolhida - 1]
                    self.marcar_como_pendente(tarefa_idx)
                    break
                else:
                    limpar_tela()
                    print(f"Tarefa {N_tarefa} não encontrada. Verifique o número da tarefa.\n")
            else:
                limpar_tela()
                print("\nDigite somente números e apenas um número!\n")
    
    # Determina qual tarefa sera substituída por uma nova.
    def atualizar_tarefa(self, N_tarefa, novo_titulo, nova_descricao, nova_data_vencimento):
        if 0 <= N_tarefa < len(self.tarefas_gerais):
            tarefa = self.tarefas_gerais[N_tarefa]
            tarefa.atualizar(novo_titulo, nova_descricao, nova_data_vencimento)

    # Finaliza o processo de atualização de status pra concluída.
    def marcar_como_concluida(self, N_tarefa):
        if 0 <= N_tarefa < len(self.tarefas_gerais):
            tarefa = self.tarefas_gerais[N_tarefa]
            if not tarefa.concluida:
                tarefa.marcar_como_concluida()
                print(f"Tarefa marcada como concluída.\n")
            else:
                print(f"Tarefa {N_tarefa + 1} não encontrada. Verifique o número da tarefa.\n")

    # Finaliza o processo de atualização de status pra concluída.
    def marcar_como_pendente(self,N_tarefa):
        if 0 <= N_tarefa < len(self.tarefas_gerais):
            tarefa = self.tarefas_gerais[N_tarefa]
            if tarefa.concluida:
                tarefa.marcar_como_pendente()
                print(f"Tarefa marcada como pendente.\n")
            else:
                print(f"Tarefa {N_tarefa + 1 } não encontrada. Verifique o número da tarefa.\n")

    # Exclui a tarefa desejada.
    def excluir_tarefa(self, N_tarefa):
        if 0 <= N_tarefa < len(self.tarefas_gerais):
            del self.tarefas_gerais[N_tarefa]

    # Faz a conferencia da data pra ver se não é algo fora dos paramentros do calendário.
    def conferir_data(self, data_vencimento):
        formato_data = "%d/%m/%Y"
        try:
            datetime.datetime.strptime(data_vencimento, formato_data)
            return True
        except ValueError:
            return False
    # Faz a leitura o arquivo que seria nosso banco de dados.
    def carregar_tarefas(self):
        try:
            with open(self.nome_arquivo, 'r', newline='') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)
                for linha in leitor_csv:
                    titulo, descricao, data_vencimento, concluida = linha
                    tarefa = Tarefa(titulo, descricao, data_vencimento)
                    if concluida == 'True':
                        tarefa.marcar_como_concluida()
                    self.tarefas_gerais.append(tarefa)
        except FileNotFoundError:
            pass
    # Faz o salvamento das alterções de todas as tarefas no banco de dados após o encerrmento do programa.
    def salvar_tarefas(self):
        with open(self.nome_arquivo, 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for tarefa in self.tarefas_gerais:
                escritor_csv.writerow([
                    tarefa.titulo,
                    tarefa.descricao,
                    tarefa.data_vencimento,
                    tarefa.concluida
                ])
                    
# Definição principal que inicia o programa inteiro.
def main():
    inicializador = GerenciadorTarefas()

    while True:
        # O que sera impresso na tela.
        print("\n======= Bem-vindo ao Tarefas! ========\n")
        print("1 - Adicionar Tarefa ")
        print("2 - Listar Tarefas Pendentes e alterar status ")
        print("3 - Listar Tarefas Concluídas e alterar status ")
        print("4 - Atualizar Tarefas")
        print("5 - Excluir Tarefas ")
        print("6 - Sair")
        
        # A escolha do usuário e logo a baixo os devidos tratamentos de possíveis burlas e bugs e execuções de cada função!
        escolha = input("\nO que deseja fazer? Insira o número da função desejada: ")
        
        if escolha.isdigit():
            numero_escolhido = int(escolha)
            if 0 < numero_escolhido < 7:
                if numero_escolhido == 1:  # Adição de uma nova tarefa;
                    limpar_tela()
                    titulo = input("\nDigite o titulo da tarefa: ")
                    descricao = input("\nDigite a descrição da tarefa: ")
                    
                    # Conferencia da data.
                    while True:
                        data_vencimento = input("\nDigite a data de vencimento da tarefa (dd/mm/yyyy): ")
                        if inicializador.conferir_data(data_vencimento):
                            break
                        else:
                            print(f"\nData {data_vencimento} inválida. Insira uma data válida no formato dd/mm/yyyy.\n")
                            continue
                    
                    limpar_tela()        
                    print("\nTarefa adicionada com sucesso!\nPara salvar, não esqueça de encerrar o programa na opção 6!\n")
                    inicializador.adicionar_tarefa(titulo, descricao, data_vencimento, status='pendente')

                elif numero_escolhido == 2:  # Imprime a lista de tarefas na tela pendentes e troca de status se solicitado;
                    inicializador.listar_tarefas_pendentes()

                elif numero_escolhido == 3:  # Imprime a lista de tarefas na tela concluídas e troca de status se solicitado;
                    inicializador.listar_tarefas_concluidas()

                elif numero_escolhido == 4:  # Imprime todas as tarefas na tela e atualiza a tarefa escolhida pelo usuário;
                    limpar_tela()
                    print("\nLista de Tarefas:\n")
                    for idx, tarefa in enumerate(inicializador.tarefas_gerais, start=1): # Imprime informações sobre cada tarefa.
                        print(f"{idx} - {tarefa.titulo}")
                        print(f"Titulo: {tarefa.titulo}")
                        print(f"Descrição: {tarefa.descricao}")
                        print(f"Data de vencimento: {tarefa.data_vencimento} ")
                        print(f"Concluída: {'sim' if tarefa.concluida else 'não'}")
                        print("-" * 20)

                    print("\nPara voltar ao menu inicial, digite 0!\n")
                    N_tarefa_escolhida = -1
                    while True:
                        # Escolher a tarefa a se atualizar,com tratamentos para supostas burlas e bugs!
                        N_tarefa = input("\nDigite o número da tarefa que deseja atualizar: ")
                        if N_tarefa.isdigit():
                            N_tarefa_escolhida = int(N_tarefa)
                            if N_tarefa_escolhida == 0:
                                limpar_tela()
                                break
                            elif 1 <= N_tarefa_escolhida <= len(inicializador.tarefas_gerais):
                                limpar_tela()
                                tarefa = inicializador.tarefas_gerais[N_tarefa_escolhida - 1]
                                print(f"\nTarefa escolhida: {tarefa.titulo}")
                                novo_titulo = input("\nDigite o novo título da tarefa: ")
                                print(f"\nDescrição esolhida: {tarefa.descricao}")
                                nova_descricao = input("\nDigite a nova descrição da tarefa: ")
                                while True:
                                    print(f"\nData de vencimento escolhida: {tarefa.data_vencimento} ")
                                    nova_data_vencimento = input("\nDigite a nova data de vencimento da tarefa (dd/mm/yyyy): ")
                                    if inicializador.conferir_data(nova_data_vencimento):
                                        break
                                    else:
                                        print(f"\nData {nova_data_vencimento} inválida. Insira uma data válida no formato dd/mm/yyyy.\n")

                                tarefa.atualizar(novo_titulo, nova_descricao, nova_data_vencimento)
                                print("\nTarefa atualizada com sucesso!\n")
                                break
                            else:
                                print(f"\nTarefa {N_tarefa_escolhida} não encontrada.\n")
                        else:
                            print("\nDigite somente números e apenas um número!\n")

                elif numero_escolhido == 5: # Imprime todas as tarefas na tela e elimina a se solicitado;
                    limpar_tela()
                    print("\nLista de Tarefas:\n")
                    for idx, tarefa in enumerate(inicializador.tarefas_gerais, start=1):  # Informações sobre cada tarefa.
                        print(f"{idx} - {tarefa.titulo}")
                        print(f"Titulo: {tarefa.titulo}")
                        print(f"Descrição: {tarefa.descricao}")
                        print(f"Data de vencimento: {tarefa.data_vencimento} ")
                        print(f"Concluída: {'sim' if tarefa.concluida else 'não'}")
                        print("-" * 20)
                        
                    print("\nCaso queira voltar ao menu inicial, digite 0!\n")
                    N_tarefa_escolhida = -1
                    while True:
                        N_tarefa = input("\nDigite o número da tarefa que deseja excluir: ")

                        if N_tarefa.isdigit():
                            N_tarefa_escolhida = int(N_tarefa)
                            if N_tarefa_escolhida == 0:
                                limpar_tela()
                                break
                            elif 1 <= N_tarefa_escolhida <= len(inicializador.tarefas_gerais):
                                limpar_tela()
                                print(f"\nTarefa {N_tarefa_escolhida} excluída com sucesso!\n")
                                inicializador.excluir_tarefa(N_tarefa_escolhida - 1)
                                break
                            else:
                                print(f"\nTarefa {N_tarefa_escolhida} não encontrada. Verifique o número da tarefa.\n")
                        else:
                            print("\nDigite somente números e apenas um número!\n")
                            
                elif numero_escolhido == 6:   # Encerra o programa.
                    limpar_tela()
                    print("\nEncerrando o programa!\n")
                    break
            else:
                print("\nDigite somente números correspondentes às opções destacadas no quadro de funções!\n")
        else:
            print("\nDigite somente números e apenas um número!\n")
            
    # Efetua o salvamento das alterações após digitar o opção 6 e segue para o encerramento do programa.
    inicializador.salvar_tarefas()
    
# Chama a inicialização do programa o coração de tudo!
if __name__ == "__main__":
    main()

print("\nPrograma encerrado, dados salvos!\n")