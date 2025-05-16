import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=id"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        print(f"Cuaca di {city}: {weather}")
        print(f"Suhu: {temp}°C")
        print(f"Kelembapan: {humidity}%")
    else:
        print("Kota tidak ditemukan atau terjadi kesalahan.")

if __name__ == "__main__":
    api_key = "MASUKKAN_API_KEY_ANDA_DI_SINI"  # Ganti dengan API key OpenWeatherMap Anda
    city = input("Masukkan nama kota: ")
    get_weather(city, api_key)