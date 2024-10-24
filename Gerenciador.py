def adiconar_tarefas(tarefas):
    repetir = 1
    while repetir == 1:
        tarefa_a_adicionar = input ("Digite a tarefa que deseja adicionar: """)
        tarefas.append(tarefa_a_adicionar)
        print("Tarefa adicionada com sucesso !")
        repetir = int(input("Deseja adicionar mais tarefas(Digite o numero indicado) ? \n 1. Sim \n 2. Nao \n "))
    return
def visualizar_tarefas(tarefas):
    for indice in range(0, len(tarefas)):
        print(indice +1, ":", tarefas[indice])
    return
def att_tarefas(tarefas):
    visualizar_tarefas(tarefas)
    atualizacao = 1
    while atualizacao == 1:
        codigo_tarefa_alteração = int(input("Digite o numero da tarefa que voce deseja alterar: " ""))
        indice_tarefa_ajustado = codigo_tarefa_alteração - 1
        nova_tarefa = input("Descreva a nova tarefa que você deseja: " "")
        if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
            tarefas[indice_tarefa_ajustado] = nova_tarefa
            print(f"Tarefa {codigo_tarefa_alteração} atualizada para {nova_tarefa}")
            atualizacao = int(input("Voce deseja alterar mais tarefas ? 1. sim 2.nao \n Indique o numero da opcao desejada: " ""))
        else:
            condicao = input("numero de tarefa incorreto, voce deseja continuar alterando as tarefas ? " "")
            if condicao == "Sim":
                att_tarefas(tarefas)
            break
    return

def completar_tarefas(tarefas, tarefas_completadas):
    visualizar_tarefas(tarefas)
    completar = 1
    while completar == 1:
        codigo_tarefa_completo = int(input("Digite o numero da tarefa que voce deseja completar: " ""))
        indice_tarefa_ajustado = codigo_tarefa_completo - 1
        if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
            manejamento_tarefa = tarefas[indice_tarefa_ajustado]
            tarefas_completadas.append(manejamento_tarefa)
            print("Tarefa atualizada para completa")
            tarefas.pop(indice_tarefa_ajustado)
            completar = int(input("Voce deseja completar mais tarefas ? 1. sim 2.nao \n Indique o numero da opcao desejada: " ""))
        else:
            condicao = input("numero de tarefa incorreto, voce deseja continuar completar alguma tarefa ? " "")
            if condicao == "Sim":
                completar_tarefas(tarefas, tarefas_completadas)
            break
    return
def limpar_tarefas(tarefas_completadas):
    tarefas_completadas.clear()

tarefas = []
tarefas_completadas = []
while True:
    print("\n Menu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefas")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
 
    escolha = int(input("indique o numeros da acao desejada: "))

    if escolha == 1:
        adiconar_tarefas(tarefas)
        print("Suas tarefas foram adicionadas com sucesso")
    elif escolha == 2:
        print("Tarefas nao completadas")
        visualizar_tarefas(tarefas)
        print("Tarefas completadas")
        visualizar_tarefas(tarefas_completadas)
    elif escolha == 3:
        att_tarefas(tarefas)
    elif escolha == 4:
        completar_tarefas(tarefas, tarefas_completadas)
    elif escolha == 5:
        limpar_tarefas(tarefas_completadas)
    elif escolha == 6:
        print("Programa finalizado")
        break
    else:
        break