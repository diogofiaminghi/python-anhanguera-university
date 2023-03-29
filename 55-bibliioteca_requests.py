import requests

info = requests.get('https://api.github.com/events')
info.headers

print(info.headers['date']) # Data de extração
print(info.headers['server']) # Servidor de origem
print(info.headers['status']) # Status HTTP da extração, 200 é ok
print(info.encoding) # Encoding do texto
print(info.headers['last-modified']) # Data da última modificação da informação