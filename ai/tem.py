import requests

api_key = "openweathermap api_key"
city = "ubon ratchathani"

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

respon = requests.get(url).json()
des = respon['weather'][0]['description']
tem = respon['main']['temp'] - 273.15
tem = '%.2f' %(tem)
print(tem)
