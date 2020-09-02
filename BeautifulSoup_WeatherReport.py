import bs4
import requests

# GET THE CURRENT HOURLY TEMPERATURE FOR BIRMINGHAM,AL FROM THE WEATHER CHANNEL
html_source = requests.get('https://weather.com/weather/hourbyhour/l/d20ef0ab981eddeccb6fd6a2d668969fb6fb6f2ae3a5d2d627a89bd8b566ea41')
get_page = bs4.BeautifulSoup(html_source.text, 'html.parser')

# FETCH THE HOUR DATA & GREET THE USER ACCORDINGLY
get_page.select('#detailIndex0 > summary > div > div > h2')
get_current_weather_hour = get_page.select('#detailIndex0 > summary > div > div > h2')
current_weather_hour = get_current_weather_hour[0]
greeting_message_AM = 'Good Morning! Now fetching your weather report for: '
greeting_message_PM = 'Good Afternoon! Now fetching your weather report for: '
find_AM = "am"
find_PM = "pm"

for h in current_weather_hour:
    weather_hour = h
    if str.find(weather_hour, find_PM) != -1:
        print(greeting_message_PM + weather_hour)
    else:
        print(greeting_message_AM + weather_hour)

# FETCH THE TEMPERATURE DATA & UPDATE THE USER ACCORDINGLY
get_page.select('#detailIndex0 > summary > div > div > div._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp > span')
get_current_temperature = get_page.select('#detailIndex0 > summary > div > div > div._-_-components-src-molecule-DaypartDetails-DetailsSummary-DetailsSummary--temperature--1kVVp > span')
current_weather_temperature = get_current_temperature[0]

temperature_message_hot = 'Stay in the AC, unless you will be near a body of water! The current temperature is: '
temperature_message_warm = 'It is warmer out than you might prefer. The current temperature is: '
temperature_message_pleasant = 'I am pleased to report, it is pleasant outside. The current temperature is: '
temperature_message_cool = 'Get excited! It is cool out there! The current temperature is: '
temperature_message_cold = 'Brrrr! It is your kind of weather! The current temperature is: '

for t in current_weather_temperature:
    weather_temperature = t
    temperature_length = len(weather_temperature)
    temperature_length = temperature_length - 1
    temperature_digits = (weather_temperature[0:temperature_length])
    if 80 < int(temperature_digits):
        temperature_message = temperature_message_hot
    elif 68 < int(temperature_digits) < 80:
        temperature_message = temperature_message_warm
    elif 55 < int(temperature_digits) < 69:
        temperature_message = temperature_message_pleasant
    elif 48 < int(temperature_digits) < 56:
        temperature_message = temperature_message_cool
    else:
        temperature_message = temperature_message_cold

print(temperature_message + weather_temperature)
