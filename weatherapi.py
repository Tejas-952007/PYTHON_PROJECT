import requests

# Function to get weather data from OpenWeatherMap API for curruent data shows in Celsius
def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # params is dictorary
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for using as Fahrenheit
    }
    
    # Send a GET request to the API 
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        weather_data = response.json()  # Parse the JSON response
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to display weather data
def display_weather(weather_data):
    if weather_data:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        
        # Print the weather information
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc.capitalize()}")
    else:
        print("No weather data to display.")

# Main function to run the program
def main():
    api_key = 'bcee902a010bd1993f9e8ecf4070425a'  # my OpenWeatherMap API key
    city = input("Enter city name: ")
    
    # Get weather data for the specified city
    weather_data = get_weather(api_key, city)
    
    # Display the weather data
    if weather_data:
        display_weather(weather_data)

# Entry point of the program
if __name__ == "__main__":
    main()