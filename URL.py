#Begining info for this script can be found at the following URL
#https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
#I used the foundaton of the original script, and built off that in an attempt to meet
#the criteria for the homework assignment. The weather options I used are located at 
#https://openweathermap.org/current
import requests, json

def StartMenu():
	print('''
	Let's check the weather!
		''')

def main():
	try:
		while True:
			StartMenu()
			city_name = input("Enter a city name or zip code : ")
			location = str(city_name)
			api_key = "e9a40e0f216dfc21c44b6806bbf83caa"
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=imperial"
			response = requests.get(complete_url) 

			x = response.json() 

			if x["cod"] != "404": 
					y = x["main"] 

	#	
		
	#pull current temperatures from config list
					current_temperature = y["temp"] 
					current_feelslike = y["feels_like"]

	#pull information on humidity levels
					current_humidity = y["humidity"] 

	#pull wind speed and gusts
					yy = x["wind"]
					current_speed = yy["speed"]
			#	current_gust = yy["gust"] - apparently no longer a valid category

	#display overall information
					z = x["weather"] 
					weather_main = z[0]["main"]
			#with gusts up to {current_gust} mph.
					print(f'''
	The temperature in {location} is now {current_temperature} deg (F), and feels like {current_feelslike} deg (F).
	The wind speed is {current_speed} mph
	The current humidity is {current_humidity}%
	Currently conditions are {weather_main.title()}
					''')
			else:
				print("Page not found")
	except:
		print({location}, "Not Found") 
main()