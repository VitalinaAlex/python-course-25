import requests

api_key = "893fae8d919eb221b5866fa794eedbeb"  # https://home.openweathermap.org/api_keys
city = input("Enter your city: ")

url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=uk")

response = requests.get(url)

print("HTTP status:", response.status_code)  # перевіряємо код відповіді

data = response.json()
print("API response:", data)  # отримуємо тіло запиту 

if response.status_code != 200:
    print("City not found or API error.")
else:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
