def jogar():
    print("**********************************")
    print("Bem vindo ao jogo Mário Versus Corona")
    print("**********************************")
    

    personagem = int(input("Com quem você deseja jogar?\n1-Mário 2- Luigi 3- Daisy:"))
    while(personagem != 1 and personagem != 2 and personagem != 3):
        int(input("Com quem você deseja jogar?\n1-Mário 2- Luigi 3- Daisy"))
    
    if(personagem == 1 ):
        personagem = "Mario"
    elif (personagem == 2):
        personagem= "Luigi"
    elif(personagem == 3):
        personagem= "Daisy"
    
    

    decisao = decisao_casa()
    if(decisao == True):#decisao_casa
        fome= True #aqui faz diferença nao ter tomado café da manhã
        decisao = decisao_caminho_trabalho

    elif(decisao == False):#decisao_casa
        fome = False #aqui faz diferença nao ter tomado café da manhã
        decisao=decisao_caminho_trabalho()
    

    if(decisao == True and fome == True):#decisao_caminho_trabalho
        decisao = decisao_ida_hospital_fome()

    elif(decisao == False):#decisao_caminho_trabalho
        decisao = decisao_ida_trabalho()
    
    elif(decisao == True and fome == False):#decisao_caminho_trabalho
        decisao = enfrentando_bowser()


    if(decisao == False and fome== True):#decisao_ida_hospital_fome
        decisao= morrer_de_fome
        final()
        
    elif(decisao == True):
        decisao = enfrentando_bowser()

    elif(decisao == False and fome == False):
        decisao = enfrentando_bowser()


    if(decisao == True):#enfrentando_bowser
        coragem = True
        decisao = decisao_bowser2(personagem)

    elif(decisao == False):#enfrentando_bowser
        coragem = False
        decisao = decisao_coragem()
        final()

    if(decisao == True):#decisão_bowser2
        decisao = decisao_conversa()
        final()

    elif(decisao == False):#decisao_bowser2
        decisao = decisao_demissao(personagem)

    if(decisao == True):#decisao_demissao
        decisao = decisao_laranja()
        final()

    elif(decisao == False):#decisao_demissao
        decisao = decisao_fake_news(personagem)
    
    if(decisao == True):#decisao_fake
        decisao = decisao_policia()
        final()

    elif(decisao == False):#decisao_fake
        decisao = decisao_ciencia(personagem)
        final()
    
    
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

def decisao_ida_hospital_fome():
    print("Você está com a princesa Peaches no hospital e precisa buscar oxigênio e resíradores do outro lado da cidade.")
    print("Você chama o Yoshi para carregar as coisas com você")
    print("Você ta com fome da uma parada para comer (1) Não para, está com pressa (2)")
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
    print("Você enfrenta ele(1) ou vai embora(2)?")
    decisao=int(input())
    decisao=estrutura_decisoria(decisao)
    return decisao

def morrer_de_fome():
    print("Enquanto você e Yoshi descarregam os suprimentos, você tem um mal súbito devido a falta de comida.")
    print("Oh não! Você está sendo levado ao hospital")
    print("Você está internado, você perdeu!")
    final()

def decisao_bowser2(personagem):
    print("Voce não deveria estar em outro lugar? O que está fazendo aqui? - Pergunta Bowservisivelmente bravo")
    print("Eu vim ajudar no combate contra a covid, o senhor entende ne?")
    print("Eu não peguei essa gripezinha, isso é tudo alarde da imprensa!- Responde ele")
    print("E agora {}, você continua a discussão (1) ou simplesmente pede demissão(2)".format(personagem))

def decisao_coragem():
    print("Você se deixou levar pelo medo e agora os suprimentos não serão entregues a tempo")
    print("Você perdeu!")

def decisao_conversa():
    print("Você se deixou levar pela discussão e agora os suprimentos não serão entregues a tempo")
    print("Você perdeu!")

def decisao_demissao(personagem):
    print("Você muito corajosamente pediu demissão e agora é um homem livre, porém não pensou que seria tão fácil assim não é?")
    print("Bowser ainda está inconformado e está tentando atrapalhar a entrega de suprimentos, segundo ele é tudo golpe da mídia")
    print("O capitão Cloroquina chega para ajudar Bowser e agora, {}, o que vc vai fazer?".format(personagem))
    print("Seguir seu caminho até o hospital deixando varias laranjas pelo caminho (1) Jogar uma bomba de Fake News no Capitão (02)")

def decisao_laranja():
    print("Muito bem! Bowser pe alérgico a laranjas, você conseguiu despistá-lo.")
    print("Parabéns! Você ajudou Peaches e muitas pessoas que precisavam de suprimentos no hospital")

def decisao_fake_news():
    print("As fake news não surtiram o efeito desejado, agora você está no meio de uma manifestação apoiando Bowser")
    print("Mas há uma maneira de escapar, você chama a policia para te ajudar (1) ou você espanta os manifestantes com um artigo cientifico(2)")

def decisao_policia():
    print("Você perdeu")

def decisao_ciencia():
    print("Você ganhou!")

def final():
    print("Fim de jogo deseja jogar novamente? Digite 1 para sim ou qualquer outra tecla para fechar o jogo")
    decisao = int(input())
    if(decisao == 1):
        jogar()


if(__name__ == "__main__"):
    jogar()