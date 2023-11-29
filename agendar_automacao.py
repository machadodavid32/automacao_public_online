import schedule
from time import sleep
import requests
from datetime import datetime

# montar uma função para obter cotação do dolar para real em intervalos fixos
def obter_cotacao_dolar():
    resultado = requests.get('https://economia.awesomeapi.com.br/json/last/usd-brl')
    cotacao_atual = resultado.json()['USDBRL'] ['ask']
    horario_atual = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    print(f'Dolar está em {cotacao_atual} no horário {horario_atual}')
    
# obter_cotacao_dolar()    
    
# Acima, estamos usando uma api para conseguir a cotação do dolar no dia atual. Essa api esta em
# formato json e precisamos conseguir a chave correta para incluir no codigo. Neste caso, aperte F9
# para marcar a linha a ser debugada, depois aperte F5 e F10
# vá em modo debug console(ao lado do terminal)digite a variável 'resultado.json()' 
# Lá, existe um dicionário em json. Você precisa do resultado atual do dolar na data de hoje e para
# para isso você precisar copiar a chave certa, que neste caso é 'ask': 
# Acesse a chave inicial> no debug console, digite resultado.json()['USDBRL'] e de o enter
# Você agora esta dentro da chave, depois faça resultado.json()['USDBRL'] ['ask'] para entrar
# na chave correta. Vai aparecer o valor do dolar no dia. Então copie essa linha
# resultado.json()['USDBRL'] ['ask']
# e a cole na função, conforme acima


# Agendar a execução deste software a cada x unidades de tempo
schedule.every(1).minute.do(obter_cotacao_dolar) # vai atualizar a cada um minuto - tem horas, dias e semanas também.

# Agendar a execução deste software em X horario e em X data
schedule.every().sunday.at('15:00').do(obter_cotacao_dolar)

print(f'Próximo agendamento irá ocorrer as {schedule.next_run()}')
while True:
    schedule.run_pending()
    sleep(1)