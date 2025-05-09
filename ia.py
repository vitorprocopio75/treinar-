# perguntar 
def boas_vindas():
    nome = input("Olá! Qual é o seu nome? ")
    print(f"Seja bem-vindo(a), {nome}!")

    resposta = input("Você gostaria de uma indicação de livro para mudar de vida? (sim/não) ").strip().lower()

    if resposta == "sim":
        print("\nAqui estão  algumas indicações de livros que podem mudar sua vida:\n")
        livros = [
            "1 – Trabalhe 4 Horas por Semana, Tim Ferriss.",
            "2 – Na Natureza Selvagem, Jon Krakauer.",
            "3 – Como Fazer Amigos e Influenciar Pessoas, Dale Carnegie.",
            "4 – O Poder do Hábito, Charles Duhigg.",
            "5 – Roube como um Artista: 10 Dicas sobre Criatividade, Austin Kleon.",
            "6 – Como Encontrar o Trabalho da Sua Vida, Roman Krznaric."
        ]
        for livro in livros:
            print(livro)
    else:
        print(f"\nMuito obrigado pela atenção, {nome}!")

# Executar o programa
boas_vindas()