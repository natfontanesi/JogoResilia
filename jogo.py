def jogar():
    def primeira_decisao():
        print("Você está na sua casa, você sai de casa direto pro trabalho(1) ou toma café da manhã antes(2)?")
        
    def segunda_decisao():
        print("")

    def final():
        print("Fim de jogo deseja jogar novamente? Digite 1 para sim ou qualquer outra tecla para fechar o jogo")
        decisao = int(input())
        if(decisao == 1):
            jogar()
        else:
            break



    print("**********************************")
    print("Bem vindo ao jogo Mário Versus Corona")
    print("**********************************")

    primeira_decisao()
    decisao = int(input())
    if(decisao == 1):
        
    elif(decisao == 2):

    else:
        primeira decisao()
        


