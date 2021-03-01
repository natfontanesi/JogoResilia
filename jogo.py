def jogar():
    print("**********************************")
    print("Bem vindo ao jogo Mário Versus Corona")
    print("**********************************")

    decisao = decisao_casa()
    if(decisao == True):
        decisao_caminho_trabalho()

    elif(decisao == False):
        print ("Você está em casa tomando café quando seu telefone toca")
        decisao_café_da_manhã()
    

    print("Você vai ajudar a princesa? (1) ou você vai trabalhar? (2)")   
    
    
def estrutura_decisoria(decisao):
    if(decisao == 1):
        return decisao = True
    
    elif(decisao == 2):
        return decisao = False 

def decisao_casa():
    print("Você está na sua casa, pensando no que vem por aí no seu dia, com saudades da emoção que tinha de entrar pelos canos e derrotar tartarugas malignas.")
    print("No meio do seu devaneio você percebe que não tomou café da manhã e que precisa sair de casa.")
    decisao=int(input("Você sai de casa imediatamente pro trabalho(1) ou toma café da manhã antes(2): "))
    if(decisao == 1):
        decisao = True
    
    elif(decisao == 2):
        decisao = False
    return decisao
        
def decisao_caminho_trabalho():
    print("Seu telefone toca e você atende. É a princesa Peaches, ela está te chamando para uma aventura como nos velhos tempos. ")
    print("Levar os suprimentos para um hospital próximo que está passando por problemas.")
    print("E aí? Você topa?")
    print("(1) Sim (2) Não")

def final():
    print("Fim de jogo deseja jogar novamente? Digite 1 para sim ou qualquer outra tecla para fechar o jogo")
    decisao = int(input())
    if(decisao == 1):
        jogar()
    else:
        break