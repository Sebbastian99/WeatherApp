import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.create_widgets()
        self.root.configure(bg="#87CEEB")

    def create_widgets(self):
        tk.Label(self.root, text="Introduceți orașul:").pack(pady=10)
        self.city_entry = tk.Entry(self.root, width=30)
        self.city_entry.pack()

        tk.Button(self.root, text="Verifică Vremea", command=self.get_weather).pack(pady=10)
        self.weather_label = tk.Label(self.root, text="")
        self.weather_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        api_key = '6HV3GANCNJ4ZKBD3HXWJPHKF4'
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={api_key}'

        try:
            response = requests.get(url)
            data = response.json()

            if 'days' in data:
                first_day = data['days'][0]
                weather_info = f"Temperatura: {first_day['temp']}°C\n" \
                               f"Descriere: {first_day['conditions']}"
                self.weather_label.config(text=weather_info)
            else:
                messagebox.showerror("Eroare", f"Nu s-a putut obține vremea pentru {city}.")
        
        except Exception as e:
            messagebox.showerror("Eroare", "A intervenit o eroare. Verificați conexiunea la internet sau încercați mai târziu.")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
