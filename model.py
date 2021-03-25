
from jogo import estrutura_decisoria
from view import decisao_bowser2_print, decisao_caminho_trabalho_print, decisao_casa_print, decisao_demissao_print, decisao_fake_news_print, decisao_ida_hospital_fome_print, enfrentando_bowser_print


def decisao_casa():
    decisao_casa_print()
    decisao = int(input("--> "))
    decisao = estrutura_decisoria(decisao)
    return decisao

def decisao_caminho_trabalho():
    decisao_caminho_trabalho_print()
    decisao = int(input("--> "))
    decisao = estrutura_decisoria(decisao)
    return decisao

def decisao_ida_hospital_fome():
    decisao_ida_hospital_fome_print()
    decisao = int(input("--> "))
    decisao = estrutura_decisoria(decisao)
    return decisao

def enfrentando_bowser():
    enfrentando_bowser_print()
    decisao = int(input("--> "))
    decisao = estrutura_decisoria(decisao)
    return decisao

def decisao_bowser2(personagem):
    decisao_bowser2_print()
    decisao = int(input("--> "))
    decisao = estrutura_decisoria(decisao)
    return decisao

def decisao_demissao(personagem):
    decisao_demissao_print()
    decisao = int(input("--> "))
    decisao = estrutura_decisoria(decisao)
    return decisao

def decisao_fake_news():
    decisao_fake_news_print()
    decisao = int(input("--> "))
    decisao = estrutura_decisoria(decisao)
    return decisao

def final():
    print("Fim de jogo deseja jogar novamente? Digite 1 para sim ou qualquer outra tecla para fechar o jogo")
    decisao = int(input("--> "))
    if (decisao == 1):
        jogar()