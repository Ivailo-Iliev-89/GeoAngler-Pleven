import requests
from bs4 import BeautifulSoup


def get_weather_data(lat, lon):
    """
    Изчислява въз основа на точно подадени данни времето на всяка една локация за риболов(Ако е зададена такава)
    """
    api_key = "3e4585b26548cd46e046be97cc79ac48"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'temp': round(data['main']['temp']),
                'wind_speed': data['wind']['speed'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            return weather

    except Exception as e:
        print(f"Timekeeping error: {e}")

    return None


def get_pleven_weather():
    """
    Взима точните данни за времето в Плевен
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.41&longitude=24.62&current_weather=true"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            current = data.get('current_weather', {})

            temp = round(current.get('temperature', 0))
            weather_code = current.get('weathercode', 0)

            weather_icons = {
                0: "☀️",
                1: "🌤️", 2: "⛅", 3: "☁️",
                45: "🌫️", 48: "🌫️",
                51: "🌧️", 53: "🌧️", 55: "🌧️",
                61: "🌧️", 63: "🌧️", 65: "🌧️",
                71: "❄️", 73: "❄️", 75: "❄️",
                80: "🌦️", 81: "🌦️", 82: "🌧️",
                95: "⛈️",
            }

            icon = weather_icons.get(weather_code, "🌤️")

            return {
                'temp': f"{temp}°C",
                'icon': icon,
                'success': True
            }
    except Exception as e:
        print(f"Грешка при вземане на времето: {e}")

    return {'temp': "--°C", 'icon': "🌤️", 'success': False}


def evaluate_fishing_conditions(change):
    """
    Оценява условията за риболов въз основа на изменението на нивото (в см)
    """
    if change is None or change == "" or change == "null":
        return {'status': "Няма данни", 'icon': "➡️", 'color': "#666666", 'class': "text-secondary"}

    try:
        change = int(change)
    except (ValueError, TypeError):
        return {'status': "Няма данни", 'icon': "➡️", 'color': "#666666", 'class': "text-secondary"}

    rules = [
        ((16, float('inf')), "❌ Рязко качване (Мътна вода)",
         "⬆️", "#d9534f", "text-danger"),
        ((6, 15), " Слаба активност (Водата качва)", "⬆️", "#5bc0de", "text-info"),
        ((-5, 5), " Стабилно ниво (Идеално време!)",
         "➡️", "#5cb85c", "text-success"),
        ((-15, -6), " Слаба активност (Водата пада)", "⬇️", "#5bc0de", "text-info"),
        ((float('-inf'), -16), "⚠️ Рязко падане (Рибата не кълве)",
         "⬇️", "#f0ad4e", "text-warning"),
    ]

    for (low, high), status, icon, color, css_class in rules:
        if low <= change <= high:
            return {
                'status': status,
                'icon': icon,
                'color': color,
                'class': css_class
            }

    return {'status': "Променливи условия", 'icon': "➡️", 'color': "#5bc0de", 'class': "text-info"}


def get_danube_levels():
    """
    Взима точните данни за нивата на река Дунав и препраща информацията в реално време
    """
    url = "https://www.appd-bg.org/bg/level-bul"
    headers = {'User-Agent': 'Mozilla/5.0'}
    regions = {
        'Оряхово': ['с. Горни Вадин', 'с. Байкал', 'с. Гиген', 'гр. Гулянци'],
        'Никопол': ['с. Дъбован', 'с. Загражден', 'гр. Никопол', 'с. Сомовит'],
        'Свищов': ['гр. Свищов'],
        'Белене': ['гр. Белене']
    }

    coords = {
        'с. Горни Вадин': (43.6766, 24.2872), 'с. Байкал': (43.7139, 24.4223),
        'с. Гиген': (43.7022, 24.4842), 'гр. Гулянци': (43.6394, 24.6931),
        'с. Дъбован': (43.7226, 24.7675), 'с. Загражден': (43.7383, 24.8735),
        'гр. Никопол': (43.7014, 24.8947), 'с. Сомовит': (43.6841, 24.9392),
        'гр. Белене': (43.6453, 25.1274), 'гр. Свищов': (43.6190, 25.3533)
    }

    stations_data = {place: {'level': '---', 'change': '0',
                             'temp_water': '---'} for place in coords}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')

        def update_places(places_list, lvl, chg, tmp):
            for place in places_list:
                stations_data[place].update(
                    {'level': lvl, 'change': chg, 'temp_water': tmp})

        if tables:
            for row in tables[0].find_all('tr'):
                cols = [td.text.strip() for td in row.find_all('td')]
                if len(cols) >= 6:
                    base_name = next(
                        (k for k in regions if k in cols[0]), None)
                    if base_name:
                        update_places(regions[base_name],
                                      cols[2], cols[4], cols[5])

        if len(tables) > 1:
            for row in tables[1].find_all('tr'):
                cols = [td.text.strip() for td in row.find_all('td')]
                if len(cols) == 5:
                    name_auto = cols[0].lower()
                    if 'корабия' in name_auto or 'corabia' in name_auto:
                        update_places(regions['Оряхово'],
                                      cols[2], cols[3], cols[4])
                    elif 'ислаз' in name_auto or 'islaz' in name_auto:
                        update_places(['с. Дъбован', 'с. Загражден'],
                                      cols[2], cols[3], cols[4])

    except Exception as e:
        print(f"Грешка при скрапване: {e}")

    try:
        n_lvl = int(stations_data['гр. Никопол']['level'])
        s_lvl = int(stations_data['гр. Свищов']['level'])
        stations_data['гр. Белене'].update({
            'level': str(int((n_lvl + s_lvl) / 2)),
            'change': stations_data['гр. Никопол']['change'],
            'temp_water': stations_data['гр. Никопол']['temp_water']
        })
    except:
        pass

    processed_data = []
    for name, info in stations_data.items():
        try:
            val_change = int(info['change'].replace(
                '+', '').replace(' см', ''))
        except:
            val_change = 0

        assessment = evaluate_fishing_conditions(val_change)
        temp_air = '--°C'
        weather_info = get_weather_data(*coords[name])

        if weather_info and 'temp' in weather_info:
            temp_air = f"{weather_info['temp']}°C"

        lvl = f"{info['level']} см" if 'см' not in info['level'] and info['level'] != '---' else info['level']
        chg = f"{'+' if val_change > 0 else ''}{info['change']}"

        if 'см' not in chg and chg != '0':
            chg += ' см'

        t_water = info['temp_water']
        if t_water != '---' and '°C' not in t_water:
            t_water += '°C'

        processed_data.append({
            'name': name, 'level': lvl, 'change': chg,
            'trend_icon': assessment['icon'], 'trend_class': assessment['class'],
            'temp_water': t_water, 'temp_air': temp_air,
            'fishing_status': assessment['status'], 'status_color': assessment['color']
        })

    return processed_data
