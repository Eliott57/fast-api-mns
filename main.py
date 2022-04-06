import requests

url = 'http://127.0.0.1:8000/'

def testApp():
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers, timeout=1)
    print(r.json())

def createVehicle(json):
    headers = {'content-type': 'application/json'}
    r = requests.post(url + 'vehicles/create', json=json, headers=headers, timeout=1)
    return r.json()

def getVehicles():
    headers = {'content-type': 'application/json'}
    r = requests.get(url + 'vehicles', headers=headers, timeout=1)
    return r.json()

def getNumberOfVehicles():
    headers = {'content-type': 'application/json'}
    r = requests.get(url + 'vehicles/number', headers=headers, timeout=1)
    return r.json()

def getNumberOfVehiclesByType(type):
    headers = {'content-type': 'application/json'}
    r = requests.get(url + 'vehicles/number/{}'.format(type), headers=headers, timeout=1)
    return r.json()

def getVehiclesBy(type, search):
    headers = {'content-type': 'application/json'}
    r = requests.get(url + 'vehicles/getBy/{}/{}'.format(type, search), headers=headers, timeout=1)
    return r.json()


if __name__ == '__main__':

    vehicles = []

    #Creation of 3 boats
    createVehicle(dict({
        'type': 'boat',
        'name': 'Catamaran',
        'brand': 'Lagoon',
        'speed': 100,
        'kms': 5000,
        'isArmy': 0
    }))
    createVehicle(dict({
        'type': 'boat',
        'name': 'Catamaran',
        'brand': 'Nautitech',
        'speed': 100,
        'kms': 2000,
        'isArmy': 0
    }))
    createVehicle(dict({
        'type': 'boat',
        'name': 'Frégate',
        'brand': 'Marine Nationale',
        'speed': 30,
        'kms': 20000,
        'isArmy': 1
    }))

    # Creation of 2 cars
    createVehicle(dict({
        'type': 'car',
        'name': 'Citadine',
        'brand': 'DS',
        'speed': 170,
        'kms': 180000,
        'color': 'white',
        'isDiesel': 1,
        'nbOfSeats': 5,
        'year': 2011,
    }))
    createVehicle(dict({
        'type': 'car',
        'name': '4x4',
        'brand': 'BMW',
        'speed': 250,
        'kms': 0,
        'color': 'darkgray',
        'isDiesel': 1,
        'nbOfSeats': 5,
        'year': 2018,
    }))

    # Creation of 1 bike
    createVehicle(dict({
        'type': 'bike',
        'name': 'Harley',
        'brand': 'Harley Davidson',
        'speed': 170,
        'kms': 240000,
        'color': 'black',
        'motor': '2147'
    }))

    # Creation of 2 planes
    createVehicle(dict({
        'type': 'plane',
        'name': 'Boeing 777',
        'brand': 'Air France',
        'speed': 920,
        'kms': 500000,
        'color': 'white',
        'isArmy': 0
    }))
    createVehicle(dict({
        'type': 'plane',
        'name': 'Rafale',
        'brand': 'Armée de l\'air',
        'speed': 2205,
        'kms': 20000,
        'color': 'green',
        'isArmy': 1
    }))

    # Get all vehicles
    vehicles = getVehicles()

    # Get number of vehicles
    numberOfVehicles = getNumberOfVehicles()

    # Get number of each type of vehicles
    numberOfBoats = getNumberOfVehiclesByType('boat')
    numberOfCars = getNumberOfVehiclesByType('car')
    numberOfBikes = getNumberOfVehiclesByType('bike')
    numberOfPlanes = getNumberOfVehiclesByType('plane')

    # Get all army vehicles
    armyVehicles = getVehiclesBy('isArmy', '1')

    # Get all diesel vehicles
    dieselVehicles = getVehiclesBy('isDiesel', '1')

    # Get all vehicles with 100 in speed
    hundredSpeedVehicles = getVehiclesBy('speed', '100')

    print(f'There are {numberOfVehicles} vehicles.')
    print(f'{numberOfBoats} boats, {numberOfCars} cars, {numberOfBikes} bikes and {numberOfPlanes} planes.\n')

    print(f'Army vehicles are:')
    for armyVehicle in armyVehicles:
        print(f"{armyVehicle.get('name')} ({armyVehicle.get('brand')})")

    print(f'\nDiesel vehicles are:')
    for dieselVehicle in dieselVehicles:
        print(f"{dieselVehicle.get('name')} ({dieselVehicle.get('brand')})")

    print(f'\nHundred speed vehicles are:')
    for hundredSpeedVehicle in hundredSpeedVehicles:
        print(f"{hundredSpeedVehicle.get('name')} ({hundredSpeedVehicle.get('brand')})")