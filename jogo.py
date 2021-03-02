def jogar():
    print("**********************************")
    print("Bem vindo ao jogo Mário Versus Corona")
    print("**********************************")
    #fatores de vitória ou derrota
    #cansaço
    #fome
    #coragem
    #contagio

    decisao = decisao_casa()
    if(decisao == True):
        fome= True#aqui faz diferença nao ter tomado café da manhã
  
        decisao=decisao_caminho_trabalho()

    elif(decisao == False):
        fome = False#aqui faz diferença nao ter tomado café da manhã
        descisao=decisao_caminho_trabalho()
    
    if(decisao == True):
        decisao = decisao_ida_hospital()

    elif(decisao == False):
        decisao = decisao_ida_trabalho()
        
    if(decisao == True):
        decisao = enfrentando_bowser()

    elif(decisao == False):
        decisao = morrer_de_fome()  
    
    
def estrutura_decisoria(decisao):
    if(decisao == 1):
        decisao = True
    
    elif(decisao == 2):
        decisao = False
    return decisao

def decisao_casa():
    print("Você está na sua casa, pensando no que vem por aí no seu dia, com saudades da emoção que tinha de entrar pelos canos e derrotar tartarugas malignas.")
    print("No meio do seu devaneio você percebe que não tomou café da manhã e que precisa sair de casa.")
    decisao=int(input("Você sai de casa imediatamente pro trabalho(1) ou toma café da manhã antes(2): "))
    decisao=estrutura_decisoria(decisao)
    return decisao
        
def decisao_caminho_trabalho():
    print("Seu telefone toca e você atende. É a princesa Peaches, ela está te chamando para uma aventura como nos velhos tempos. ")
    print("Levar os suprimentos para um hospital próximo que está passando por problemas.")
    print("E aí? Você topa?")
    print("(1) Sim (2) Não")
    decisao=int(input())
    decisao=estrutura_decisoria(decisao)
    return decisao

def decisao_ida_hospital():
    print("Você está com a princesa Peaches, precisa buscar oxigênio e resíradores do outro lado da cidade.")
    print("Você chama o Yoshi para carregar as coisas com você")
    print("Você ta com fome da uma parada para comer (1) Não para,está com pressa (2)")
    decisao=int(input())
    decisao=estrutura_decisoria(decisao)
    return decisao

def decisao_ida_trabalho():
    print("Você chega ao trabalho e vem noticia de Lockdown na cidade, os hospitais estão cheios")
    print("Oh não! Temos suspeita de covid no trabalho e vc teve contato com koopa tropa doente")
    print("Você está em quarentena, você perdeu!")
    final()

def enfrentando_bowser():
    print("Enquanto você e Yoshi descarregam os suprimentos, Bowser aparece muito bravo.")
    print("Você está fazendo o que aqui? - Ele pergunta - Já não falei que é só uma gripezinha?")
    print("Você enfrenta ele(1) ou vai embora(2)")
    decisao=int(input())
    decisao=estrutura_decisoria(decisao)
    return decisao


def morrer_de_fome():
    print("Enquanto você e Yoshi descarregam os suprimentos, você tem um mal súbito devido a falta de comida.")
    print("Oh não! Você está sendo levado ao hospital")
    print("Você está internado, você perdeu!")
    final()


def final():
    print("Fim de jogo deseja jogar novamente? Digite 1 para sim ou qualquer outra tecla para fechar o jogo")
    decisao = int(input())
    if(decisao == 1):
        jogar()
    