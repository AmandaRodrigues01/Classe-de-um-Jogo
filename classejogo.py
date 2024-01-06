class jogo():
    def __init__(self,nome,idade,tipo=False,atacar=True):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.atacar = atacar
#         tipo=['guerreiro'],['Mago'],['Monge']
     
        while True:
      
           if tipo is True:
            print('-'*20)
            print('escolha uma das opções a seguir:')
            print('\n 1:guerreiro,\n 2:Mago,\n 3:Monge\n 4:Ninja')
            print('-'*20)
            try:    
                    escolha = int(input('Digite a Sua escolha:'))
         
        
            except ValueError:
               print('Usuario digitou um valor invalido!!')   
            except KeyboardInterrupt:
               print('ERRO!!Digite apenas uma das opções')    
  
            else:
                         
               if escolha >4:
                    print('OPS!!Digite apenas umas das opções acima')
             
               else:
                 try:
                   if escolha ==1:
                    print(f'O seu nome é {nome},sua idade é {idade} anos ','tipo é ''Guerreiro')
                    break
                   if escolha ==2:
                      print(f'O nome escolhido foi {nome},sua idade é {idade} anos e ','tipo é ''Mago')
                      break
                   if escolha ==3:
                      print(f'O nome escolhido foi {nome}, sua idade é {idade} anos ','seu tipo é ''Monge')
                      break
                   if escolha ==4:
                     print(f'O nome escolhido foi {nome}, sua idade é de {idade} e seu tipo é de Ninja')
                     break
                 except KeyboardInterrupt:
                     print('Erro digite uma opção válida')
                  
        while True:
         if atacar is True:
               try:
                    if escolha ==1:
                     print(f'O {nome} Guerreiro está atacando com uma Espada ...')
                     break
                    if escolha ==2:
                     print(f'O {nome} Mago está  atacando com Magia...')
                     break
                    if escolha ==3:
                     print(f'O {nome} Monge está  atacando com artes marciais... ')

                     break
                    if escolha ==4:
                     print(f'O {nome} Ninja está atacando com shuriken...')
                     break
                  
               except KeyboardInterrupt:
                  print('ERRO!!Usuário saiu inesperademente')
                  break