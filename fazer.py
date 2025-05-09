# perguntar, qual o nome da pessoa, e perguntar se ela quer dicas de livros sobre persuasão 
#.strip().lower() pra que serve esses codigos 
#como usar o def 
#como usar o == e os comandos strip e lower 
#aprimorar esse codigo
#como usar \n
nome = input("Qual é o seu nome ?")
print(f"Olá,{nome}")        
resposta = input(f"{nome}, Você gostaria de uma indicação de livro para persuasão ? (sim ou não)").strip().lower()

if resposta == "sim":
    print("\nAqui tem alguma indicação de livro de persuasão:\n")
    Livro =[
    
        'Poder e manipulação: A Versão moderna de O Príncipe de Maquiavel'
        

        ]
for livro in Livro:
    print(Livro)
print(f"\nEsse livro foi considerado o melhor livro sobre persuasão, muito obrigado pela atenção {nome}:")
