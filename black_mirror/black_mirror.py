respostas = {
    "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?": "Joan Bright",
    "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?": "Leonardo",
    "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?": "Smithereen",
    "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?": "Por meio de sua ex-namorada",
    "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?": "Fica chocada e confusa, depois decide confrontar o criador da série",
    "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?": "Privacidade, vigilância, exploração da mídia",
    "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.": "Não, o episódio termina de forma mais otimista do que é comum em Black Mirror, com Joan conseguindo algum controle sobre sua própria narrativa."
}

while True:
    pergunta = input("Por favor, insira sua pergunta ou digite 'sair' para encerrar: ").strip().upper()
    if pergunta == "SAIR":
        print('Encerrando o programa...')
        break
    else:
        if pergunta in respostas:
            print(respostas[pergunta])
        else:
            print("Desculpe, não encontrei uma resposta para essa pergunta.")
