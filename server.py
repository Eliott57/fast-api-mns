from fastapi import Request, Response, FastAPI, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from json import JSONDecodeError

import vehicle

app = FastAPI()

vehicles = []

@app.get('/')
def testApp():
    return JSONResponse({'message': 'App is running' })

@app.post('/vehicles/create')
async def createVehicle(request: Request):
    try:
        data = await request.json()

        type = data.get('type')
        name = data.get('name')
        brand = data.get('brand')
        speed = data.get('speed')
        kms = data.get('kms')

        if type == 'boat':
            isArmy = data.get('isArmy')

            newVehicle = vehicle.Boat(name, brand, speed, kms, isArmy)
        elif type == 'car':
            color = data.get('color')
            isDiesel = data.get('isDiesel')
            nbOfSeats = data.get('nbOfSeats')
            year = data.get('year')

            newVehicle = vehicle.Car(name, brand, speed, kms, color, isDiesel, nbOfSeats, year)
        elif type == 'bike':
            color = data.get('color')
            motor = data.get('motor')

            newVehicle = vehicle.Bike(name, brand, speed, kms, color, motor)
        elif type == 'plane':
            isArmy = data.get('isArmy')

            newVehicle = vehicle.Plane(name, brand, speed, kms, isArmy)

        vehicles.append(newVehicle)
        return newVehicle
    except JSONDecodeError:
        return JSONResponse({'error': 'No body found'})
    except:
        return JSONResponse({'error': 'Internal Server'})

@app.get('/vehicles')
def getVehicles():
    return vehicles

@app.get('/vehicles/number')
def getNumberOfVehicles():
    try:
        return len(vehicles)
    except JSONDecodeError:
        return JSONResponse({'error': 'No body found'})
    except:
        return JSONResponse({'error': 'Internal Server'})

@app.get('/vehicles/number/{type}')
def getNumberOfVehiclesByType(type: str):
    try:
        if type == 'boat':
            arr = [element for element in vehicles if isinstance(element, vehicle.Boat)]
        elif type == 'car':
            arr = [element for element in vehicles if isinstance(element, vehicle.Car)]
        elif type == 'bike':
            arr = [element for element in vehicles if isinstance(element, vehicle.Bike)]
        elif type == 'plane':
            arr = [element for element in vehicles if isinstance(element, vehicle.Plane)]

        return len(arr)
    except JSONDecodeError:
        return JSONResponse({'error': 'No body found'})
    except:
        return JSONResponse({'error': 'Internal Server'})

@app.get('/vehicles/getBy/{type}/{search}')
def getVehiclesBy(type: str, search: str):
    try:
        arr = []
        for element in vehicles:
            try:
                if str(getattr(element, type)) == str(search):
                    arr.append(element)
            except AttributeError:
                continue
        return arr
    except JSONDecodeError:
        return JSONResponse({'error': 'No body found'})
    except:
        return JSONResponse({'error': 'Internal Server'})
