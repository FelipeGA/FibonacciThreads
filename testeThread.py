from threading import Thread

NUM_THREADS = 4
threads = []
numeros = []

class testeThread(Thread):
	def __init__(self,num):
		Thread.__init__(self)
		self.num = num

	def run(self):
		pass

class Calculo(testeThread):
	def __init__(self,num,numero):
		testeThread.__init__(self,num)
		self.numero = numero
	
	def fibonacci(self,numeroTeste):
		if numeroTeste<0:
			print("Entrada incorreta!")
		elif numeroTeste==1:
			return 0
		elif numeroTeste==2:
			return 1
		else:
			return self.fibonacci(numeroTeste-1) + self.fibonacci(numeroTeste-2)

	def run(self):
		print('Inicianco thread'+str(self.num)+' com numero '+str(self.numero))
		
		print('Resultado thread ' + str(self.num) + ' é ' + str(self.fibonacci(self.numero)))
		
		
for j in range(0,NUM_THREADS):
	numeros.append(int(input('Digite:')))

for i in range(0,NUM_THREADS):	
	threads.append(Calculo(i,int(numeros[i])))
	
	threads[i].start()		

