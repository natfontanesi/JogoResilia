import view
import model


def jogar():
    view.jogar_print()

    personagem = int(input("--> "))
    while personagem != 1 and personagem != 2 and personagem != 3:
        print("Com quem você deseja jogar?")
        personagem = int(input("Mário(1) -- Luigi(2) -- Daisy(3)"))
        
    if personagem == 1:
        personagem = "Mario"
    elif personagem == 2:
        personagem = "Luigi"
    elif personagem == 3:
        personagem = "Daisy"

    decisao = model.decisao_caminho_trabalho()
    if (decisao == True):  # decisao_casa
        fome = True  # aqui faz diferença nao ter tomado café da manhã
        decisao = model.decisao_caminho_trabalho()

    elif (decisao == False):  # decisao_casa
        fome = False  # aqui faz diferença nao ter tomado café da manhã
        decisao = model.decisao_caminho_trabalho()

    if (decisao == True and fome == True):  # decisao_caminho_trabalho
        decisao = model.decisao_ida_hospital_fome()

    elif (decisao == False):  # decisao_caminho_trabalho
        decisao = model.decisao_ida_trabalho()

    elif (decisao == True and fome == False):  # decisao_caminho_trabalho
        decisao = model.enfrentando_bowser()

    if (decisao == False and fome == True):  # decisao_ida_hospital_fome
        decisao = model.morrer_de_fome
        model.final()

    elif (decisao == True):
        decisao = model.enfrentando_bowser()

    elif (decisao == False and fome == False):
        decisao = model.enfrentando_bowser()

    if (decisao == True):  # enfrentando_bowser
        coragem = True
        decisao = model.decisao_bowser2(personagem)

    elif (decisao == False):  # enfrentando_bowser
        coragem = False
        decisao = model.decisao_coragem()
        model.final()

    if (decisao == True):  # decisão_bowser2
        decisao = model.decisao_conversa()
        model.final()

    elif (decisao == False):  # decisao_bowser2
        decisao = model.decisao_demissao(personagem)

    if (decisao == True):  # decisao_demissao
        decisao = model.decisao_laranja()
        model.final()

    elif (decisao == False):  # decisao_demissao
        decisao = model.decisao_fake_news(personagem)

    if (decisao == True):  # decisao_fake
        decisao = model.decisao_policia()
        model.final()

    elif (decisao == False):  # decisao_fake
        decisao = model.decisao_ciencia(personagem)
        model.final()

def estrutura_decisoria(decisao):
    if (decisao == 1):
        decisao = True

    elif (decisao == 2):
        decisao = False
        return decisao