def jogar():
    print("**********************************")
    print("Bem vindo ao jogo Mário Versus Corona")
    print("**********************************")

    decisao_casa()
    decisao = int(input())
    if(decisao == 1):
        print("Você está a caminho do trabalho quando seu telefone toca")
        decisao_telefone()

    elif(decisao == 2):
        print ("Você está em casa tomando café quando seu telefone toca")
        decisao_telefone()
    else:
        primeira decisao()

    print("Você vai ajudar a princesa? (1) ou você vai trabalhar? (2)")   
    
    
def estrutura_decisoria(decisao):
    if(decisao == 1):
        return decisão = True
    
    elif(decisao == 2):
        return decisao = False 

def decisao_casa():
    print("Você está na sua casa, você sai de casa direto pro trabalho(1) ou toma café da manhã antes(2)?")
        
def decisao_telefone():
    print("É a princesa Peaches pedindo ajuda, ela precisa que você leve a sei la o que para ela no hospital. ")

def final():
    print("Fim de jogo deseja jogar novamente? Digite 1 para sim ou qualquer outra tecla para fechar o jogo")
    decisao = int(input())
    if(decisao == 1):
        jogar()
    else:
        break