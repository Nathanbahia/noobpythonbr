from time import sleep
from random import shuffle, choice

class Card:
	''' 
	Criação da classe Card. Esta classe possui dois atributos:
		- Naipe e Valor (assim como as cartas da vida real)
		
	O método __init__ é o método construtor que recebe os parâmetros
	naipe e valor e os atribui às propriedades self.naipe e self.valor
	
	'''
	
	def __init__(self, naipe, valor):
		self.naipe = naipe
		self.valor = valor



	'''
	O método __str__ serve para definir como deve ser impresso o objeto da classe.
	
	Aqui, estou usando os valores das propriedades para formatar a exibição
	das cartas do modo como as conhecemos, pois como será apresentado na 
	classe Deck, a formação de um objeto Card se dá apenas com parâmetros numéricos.
	
	'''
	
	def __str__(self):
		''' Cartas especiais '''
		if   self.valor ==  1: valor = "Ás"
		elif self.valor == 11: valor = "Valete"            
		elif self.valor == 12: valor = "Rainha"
		elif self.valor == 13: valor = "Rei"
		else:
			''' Cartas normais '''
			valor = self.valor

		''' Os naipes são dados como números e alterados aqui abaixo '''
		if self.naipe == 0: return f"{valor} de Ouros"
		if self.naipe == 1: return f"{valor} de Copas"
		if self.naipe == 2: return f"{valor} de Espadas"
		if self.naipe == 3: return f"{valor} de Paus"



class Deck:
	'''
	Criação da classe Deck (baralho). Para a criação de um objeto desta
	classe não é necessária a passagem de parâmetros.
	
	Dentro do proprio método construtor __init__, através de um loop
	for, são criadas 52 instâncias da classe Card, que recebe o valor de
	naipe e valor a cada iteração do loop.
	
	Esses objetos criados são armazenados dentro da propriedade do Deck 
	self.cards. Ou seja, temos uma classe (Deck) que armazena cartas (Card)
	'''
	
	def __init__(self):
		self.cards = []

		for naipe in range(4):
			for valor in range(1, 14):
				newCard = Card(naipe, valor)
				self.cards.append(newCard)    
	
	
		''' A função shuffle embaralha nosso baralho '''
		shuffle(self.cards)


class Player:
	'''
	Criação da classe Player. Essa classe possui um parâmetro opcional (name),
	que caso não seja passado, recebe o valor padrão 'Programador'. 
	
	Essa classe possui uma lista como propriedade que representa a mão 
	do jogador, que assim como a propriedade self.cards do Deck, a propriedade
	self.hand do Player armazena objetos Cards.
	
	'''
	
	def __init__(self, name='Programador'):
		self.name = name
		self.hand = []    



	'''
	Esse método calcula a quantidade de pontos que o jogador tem em mãos,
	usando um loop for, é somado à variável score a propriedade valor de 
	cada instância de classe Card que ele possuir.
	'''
	
	def get_hand_score(self):
		score = 0
		for c in self.hand:
			score += c.valor
		return score



class Game:
	'''
	Aqui é que está toda a lógica do jogo.
	
	Essa classe usa como parâmetros para o método construtor __init__
	uma lista com objetos Player e um objeto Deck.
	
	Possui ainda como propriedades pré-determinadas self.round que vai 
	gerenciar as rodadas e self.winners que vai armazenas os vencedores.
	'''
	
	def __init__(self, players, deck):
		self.players = players
		self.deck = deck
		self.round = 0		
		self.winners = []
		
		
	''' Recebe um objeto player e retorna True se tiver mais de 21 pontos '''
	def check_if_is_not_over(self, p):        
		if p.get_hand_score() > 21:
			return True

	''' Recebe um objeto player e retorna True se tiver exatamente 21 pontos '''
	def check_if_win(self, p):        
		if p.get_hand_score() == 21:			
			return True
			

	'''
	Este método vou comentar depois kkk
	'''
	def give_cards(self):              
		if self.round < len(self.players):        
			carta = self.deck.cards.pop()    
			self.players[self.round].hand.append(carta)
			print(self.players[self.round].name, 'retirou a carta ', carta, ' \
e agora tem ', self.players[self.round].get_hand_score(), ' pontos.')

			if self.check_if_is_not_over(self.players[self.round]):
				print(self.players[self.round].name, ' está fora.')                
				del self.players[self.round]
				
				if len(self.players) > 1:                
					self.round = choice(list(range(len(self.players))))

			elif self.check_if_win(self.players[self.round]):
				print(self.players[self.round].name, ' venceu.')
				self.winners.append(self.players[self.round])                              
				del self.players[self.round]
				
				if len(self.players) > 1:                
					self.round = choice(list(range(len(self.players))))

			else:
				self.round += 1
				
		else:
			self.round = 0
			
		print('\n')		
		

''' Criação dos jogadores '''

p1 = Player('Nathan Bahia')
p2 = Player('Guido van Rossum ')
p3 = Player('Brendan Eich')
p4 = Player('Tim Berners-Lee')

''' Criação do baralho '''

deck = Deck()

''' Criação da lista de jogadores '''

players = [p1, p2, p3, p4] 

''' Criação do objetos Game '''

game = Game(players, deck)



'''
Loop principal que será executado enquanto ainda houver jogadores que 
não tenham vencido e que ainda não tenham estourado
'''

while len(game.players) > 0:
	game.give_cards()
	sleep(.3)

'''
Após o término do loop while acima, se houverem ganhadores, seus nomes
serão exibidos aqui
'''	
if len(game.winners) > 0:
	print("Vencedor (es):")
	for winner in game.winners:
		print(winner.name)
	
else:
	print("Ninguém venceu!")	
