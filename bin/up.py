import time

class Up:
	def __init__(self, up, up_failed, up_errors, up_test):
		pass

	def send(packet, status_server):
		up = [packet]
		up_failed = False
		up_errors = None
		up_test = False
		if(up_errors == None and up_failed == False or up_test != False): # em caso de nenhuma falha apresentada, faça:
			while True:
				try: #Execute o envio dos pacotes, caso ocorra tudo bem...
					#enviar aqui os pacotes
					up = { 'packet_buffer': [packet], 'machine_status': "UP" }
					print(up)
					return up
				except:
					#avisar ao watchdog_timer que falhou e precisa reiniciar
					return { 'packet_buffer': "NO_PACK", 'machine_status': "ERROR", 'error_type':"NONE" }
				finally:
					print("Reiniciando requisição...")
					#continua executando e enviando sinal caso não esteja em estado "DOWN"
		return up

	def _test_up(packet):
		up_test = [packet]
		return up_test



time.sleep(3)
