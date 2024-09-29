import requests

def obter_temperatura(cidade):
    chave_api = 'DIGITE SUA CHAVE AQUI'  # Substitua pela sua chave de API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&lang=pt&appid={chave_api}'
    resposta = requests.get(url)
    dados = resposta.json()
    if dados.get('main'):
        temperatura = dados['main']['temp']
        print(f"A temperatura atual em {cidade} é de {temperatura}°C.")
    else:
        print(f"Não foi possível obter a temperatura para {cidade}.")

cidade = input("Digite o nome da cidade: ")
obter_temperatura(cidade)
