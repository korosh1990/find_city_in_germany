import requests
def find_city_in_germany(name):
    # API-Informationen für die Suche nach Städtenamen
    url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid=0f198f0be91798f02da1d86e85ea5866"

    # Senden Sie eine Anfrage an die API
    response = requests.get(url)

        # Überprüfen Sie den Antwortstatus
    if response.status_code == 200:
        data = response.json()
        city = data.get('name', 'Stadt nicht gefunden')
        country = data.get('sys', {}).get('country', 'Das Land hat nich gefunden')
        if country == 'DE':
            return f"{name} ist in Deutschland"
        else:
            return f"{name} ist nicht in Deutschland"
    else:
        return "Beim Abrufen der Daten ist ein Fehler aufgetreten"


# Den Namen der Stadt vom Benutzer abrufen
city_name = input("Bitte geben Sie einen Stätdenamen ein: ")

# Suche nach Städtenamen
result = find_city_in_germany(city_name)
print(result)
