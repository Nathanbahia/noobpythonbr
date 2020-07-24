import os
from time import sleep
from random import randint, sample

class Guerreiro:
	def __init__(self, nome):
		self.nome = nome
		self.forca = randint(5, 10)
		self.defesa = randint(3, 7)
		self.vida = 10
		self.mana = 3
		
	def __str__(self):
		return f'{self.nome:<8} | Força: {str(self.forca):<3} | Defesa: {str(self.defesa):<3} | Vida: {str(self.vida):<3} | Mana: {str(self.mana):<3}'
		
	def atacar(self, outro):
		if self.forca > outro.defesa:
			forca_do_ataque = self.forca - outro.defesa
			outro.vida -= forca_do_ataque
			
			print(f'\n{self.nome} causa {forca_do_ataque} de danos em {outro.nome}\n')
			
		else:
			print(f'\n{self.nome} não tem força suficiente para atacar {outro.nome}\n')
			
	def usar_magia_ataque(self, outro):
		if self.mana >= 1:
			poder_da_magia = randint(1, 5)
			outro.vida -= poder_da_magia
			self.mana -= 1		
			print(f'\n{self.nome} causa {poder_da_magia} de danos usando magia em {outro.nome}\n')
		else:
			print(f'\n{self.nome} tenta usar magia em {outro.nome}, mas falha\n')
			
	def usar_magia_saude(self):
		if self.mana >= 1:
			vida_recuperada = randint(1, 5)
			self.vida += vida_recuperada
			self.mana -= 1			
			print(f'\n{self.nome} recupera {vida_recuperada} pontos de vida\n')
		else:
			print(f'\n{self.nome} tenta usar magia para recuperar a saúde, mas falha\n')
		
	def checar_se_esta_vivo(self):
		if self.vida > 0:
			return True
		else:
			return False

guerreiro1 = Guerreiro('Gandalf')
guerreiro2 = Guerreiro('Aragorn')
guerreiro3 = Guerreiro('Legolas')			

guerreiros  = [
	guerreiro1,	
	guerreiro2,
	guerreiro3,	
]			

while True:
	if len(guerreiros) > 1:
		
		try: 
			os.system('clear')
		except: 
			os.system('cls')
		
		[print(i + 1, g) for i, g in enumerate(guerreiros)]
			
		atacante, defensor = sample(guerreiros, 2)		 
		
		tipo_de_movimento = randint(0, 10)
		
		if tipo_de_movimento < 5:		
			atacante.atacar(defensor)
		
		elif tipo_de_movimento < 8:		
			atacante.usar_magia_ataque(defensor)
			
		else:
			atacante.usar_magia_saude()
					
		
		for g in guerreiros:
			if g.vida <= 0:
				print(f'\n{g.nome} está morto\n')
				del guerreiros[guerreiros.index(g)]
		
		sleep(1)
		
	else:		
		print(f'\n\nApós uma dura batalha, {guerreiros[0].nome} foi o vencedor!\n\n')
		break
		
input('Tecle ENTER para finalizar...')
