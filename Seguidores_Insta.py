#pinheirocfc@gmail.com	
#orientacoes em https://youtu.be/94zpnfo7svc

#Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Classe
class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.username_influencer = 'sigo_de_volta_a_todos' #quem sera o primeiro insta a ser aberto
		#https://github.com/mozilla/geckodriver/releases
		self.bot = webdriver.Firefox(executable_path = 'C:/Program Files (x86)/Mozilla Maintenance Service/geckodriver.exe')	

	# A função irá nos conectar ao Instagram
	def login(self):
		bot = self.bot
		# Navegue até a página de login do Instagram
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(3)

		# Encontre as caixas de e-mail e senha, insira nossas credenciais de login
		email = bot.find_element_by_name('username').send_keys(self.username)
		password = bot.find_element_by_name('password').send_keys(self.password)

		# Aguarde 1 segundo e pressione ENTER
		time.sleep(1)
		bot.find_element_by_name('password').send_keys(Keys.RETURN)

		# Aguarda 3 segundos do pos-login
		time.sleep(3)

	def buscar_seguidores(self, number_of_followers):
		bot = self.bot

		bot.get('https://instagram.com/' + self.username_influencer)
		time.sleep(2)

		bot.find_element_by_xpath('//a[@href="/' + self.username_influencer + '/followers/"]').click()

		time.sleep(1)

		popup = bot.find_element_by_class_name('isgrP')

		#lista de seguidores do influencer
		followers_array = []

		i = 1

		while len(followers_array) <= number_of_followers:
			bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
			time.sleep(0.4)

			followers = bot.find_elements_by_class_name('FPmhX')

			for follower in followers:
				if follower not in followers_array:
					followers_array.append(follower.text)

			i+=1

		self.followers = followers_array

	def Seguir_usuarios(self, number_to_follow):
		bot = self.bot

		for follower in self.followers:
			bot.get('https://instagram.com/' + follower)
			time.sleep(2)

			if(len(bot.find_elements_by_xpath("//*[contains(text(), 'Esta conta é privada')]")) > 0):
				#Se eles forem privados, não podemos ver sua lista de seguidores, então pule-os
				continue

			bot.find_element_by_xpath('//a[@href="/' + follower + '/followers/"]').click()
			time.sleep(3)

			follow = bot.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")

			i = 1

			for follower in follow:
				if(i != 1):
					bot.execute_script("arguments[0].click();", follower)
					print("seguiu")
					time.sleep(1)
				if(i > number_to_follow):
					break

				i+=1

			time.sleep(2)

#variavel com usuario + senha do instagram
insta = InstagramBot('AQUI SEU EMAIL DE LOGIN', 'AQUI SUA SENHA')
time.sleep(3)

#1 Passo - fazer login
insta.login()

#2 Passo Buscar seguidores
insta.buscar_seguidores(5)

#Segue os seguidores dos influencers
insta.Seguir_usuarios(10)

	