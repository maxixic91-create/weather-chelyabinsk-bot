"""
District data for Chelyabinsk city
Coordinates and descriptions for all 7 districts
"""

DISTRICTS = {
    "central": {
        "name": "Центральный",
        "coordinates": (61.2569, 55.1603),
        "description": "Центр города, проспект Ленина, Кировка, площадь Революции",
        "population": "~150 000"
    },
    "kalininsky": {
        "name": "Калининский",
        "coordinates": (61.4314, 55.2039),
        "description": "Северо-западная часть, ЧМЗ, парк Тищенко",
        "population": "~220 000"
    },
    "kurchatovsky": {
        "name": "Курчатовский",
        "coordinates": (61.4358, 55.1597),
        "description": "Северная часть, ЧТЗ, озеро Смолино",
        "population": "~210 000"
    },
    "leninsky": {
        "name": "Ленинский",
        "coordinates": (61.3414, 55.1328),
        "description": "Юго-западная часть, Теплотехнический институт",
        "population": "~180 000"
    },
    "metallurgichesky": {
        "name": "Металлургический",
        "coordinates": (61.4014, 55.0928),
        "description": "Южная часть, завод Мечел, металлургический комбинат",
        "population": "~140 000"
    },
    "sovetsky": {
        "name": "Советский",
        "coordinates": (61.2914, 55.1489),
        "description": "Юго-западный район, парк Гагарина, Шершневское водохранилище",
        "population": "~130 000"
    },
    "traktorozavodsky": {
        "name": "Тракторозаводский",
        "coordinates": (61.4814, 55.2039),
        "description": "Восточная часть, ЧТЗ, тракторный завод",
        "population": "~190 000"
    }
}

def get_district_by_key(key: str):
    """Get district data by key"""
    return DISTRICTS.get(key)

def get_all_districts():
    """Get all districts as list of tuples"""
    return list(DISTRICTS.items())

def get_district_names():
    """Get list of all district names"""
    return [data["name"] for data in DISTRICTS.values()]
