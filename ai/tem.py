import requests

api_key = "0bddcc3609d450dc7d5264d45b10ab09"
city = "ubon ratchathani"

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

respon = requests.get(url).json()
des = respon['weather'][0]['description']
tem = respon['main']['temp'] - 273.15
tem = '%.2f' %(tem)
print(tem)
