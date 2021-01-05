import hug
import requests

@hug.get('/')
def temp(city: hug.types.text ):
    key = '5eb8acfd55b37163529efa9cbd1acbfb'
    try:
        if city == None :
            city = 'Chicago'

        call = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
        data = requests.get(call)
        city_data = data.json()
        return f"<h1>Temperature in {city_data['name']} is {round(city_data['main']['temp']-273)}</h1>"
    except:
        return "<h1>try again</h1>"