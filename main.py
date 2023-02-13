import requests
s_city="saint petersburg,RU"
appid="6c1291c9bd0a4a79bea6e26575327e03"

res=requests.get("https://api.openweathermap.org/data/2.5/weather",
    params={'q':s_city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

print("город:",s_city)
print("погодные условия:",data['weather'][0]['description'])
print("Температура:",data['main']['temp'])
print("Минимальрая температура:",data['main']['temp_min'])
print("Максимальная температура:",data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])

res=requests.get("http://api.openweathermap.org/data/2.5/forecast",
      params={'q':s_city,'units':'metrice','lang':'ru','APPID':appid})
data=res.json()
print("Прогноз погодны на неделю:")

for i in data['list']:
    print("Дата<",i['dt_txt'],">\r\nТемпература<",
   '{0:+3.0f}'.format(i['main']['temp']),">\r\nПогодные условия<",
   i['weather'][0]['description'], "> \r\nСкорость ветра <", i['wind']['speed'], "> \r\nВидимость <", i['visibility'], ">")
    print("_______________________________")
