[CarJam](https://www.carjam.co.nz/) is a resource for finding information about cars registered in NZ.

This unofficial python API allows you to interact with the site and retrieve data to use in other python projects.

[![Downloads](https://static.pepy.tech/badge/carjam)](https://pepy.tech/project/carjam)

This API may stop functioning if CarJam updates their website code.
It is provided "as-is" with no implied warranty.
No responsibility is assumed for any future issues or interruptions in API functionality as a result of using this library.

Find this library on PyPi [here](https://pypi.org/project/carjam/) and Github [here](https://github.com/kianz20/CarJam-API)

## Installation

`pip install carjam`

## Basic car details

```python
import carjam
client = carjam.Client()
details = client.basic_details('fkk351')
```

Returns an json object containing basic car details:

```json
{
	"plate": "FKK351",
	"vin": "7AT0H63WX10005902",
	"chassis": "ACT10-0005902",
	"current_vehicle_odometer_unit": "K",
	"reported_stolen": "U",
	"make": "TOYOTA",
	"year_of_manufacture": 2000,
	"vehicle_type": 7,
	"usage_level": 1.91,
	"average_fleet_mileage": 10500
}
```

## Car model details

```python
import carjam
client = carjam.Client()
details = client.model_details('fkk351')
```

Returns a json object containing more specific model details:

```json
{
	"car_id": 0,
	"chassis_number": "ACT10-0005902",
	"make": "TOYOTA",
	"model": "OPA",
	"grade": "I",
	"manufacture_date": "2000-09",
	"body": "TA-ACT10",
	"engine": "1AZFSE",
	"drive": "FF",
	"transmission": "CVT"
}
```

## Car fuel consumption

```python
import carjam
client = carjam.Client()
fuel_consumption = client.fuel_consumption("fkk351")
```

Returns a string containing the fuel consumption of the car in l/100km:

```txt
7.50 litres/100km
```

## Car images

```python
import carjam
client = carjam.Client()
image = client.image('fkk351')
```

Returns a json object containing links to the current and original image

```json
{
	"image": "photos.carjam.co.nz/jph/_search_img_catalog_10102041_200404.jpg",
	"orig_image": "photos.carjam.co.nz/jph/_search_img_catalog_10102041_200404.jpg"
}
```

## Car Odometer Details

```python
import carjam
client = carjam.Client()
odo_details = client.odometer_history('fkk351')
```

Returns a json object array containing odometer history

```javascript
[
  {
    "odometer_date": 1678618800,
    "odometer_reading": "296662",
    "odometer_unit": "K",
    "odometer_source": "IW",
    "days": 7,
    "seconds": 604800,
    "kms": 359,
    "daily_usage": 51.285714285714285
  },
  ...
]
```

## NZ Fleet Details

```python
import carjam
client = carjam.Client()
fleet_details = client.fleet_details(page=1)
```

Returns a JSON object containing the most registered cars in NZ, with 20 objects per call.
You can change the page parameter to retrieve additional sets of data.

```javascript
[
  {
    "make": "FORD",
    "model": "RANGER",
    "year": "2021",
    "count": "12463",
    "rank": "1"
  },
  ...
]
```

fleet_details() can also take optional filter variables:

```python
import carjam
client = carjam.Client()
filtered_fleet_details = client.fleet_details(page=1, make='TOYOTA', query="cor", fuel_type="PETROL")
```

Returns a JSON object containing the most registered cars in NZ filtered by the params, with 20 objects per call.
You can change the page parameter to retrieve additional sets of data.

```javascript
[
  {
    "make": "TOYOTA",
    "model": "COROLLA",
    "year": "2004",
    "count": "8428",
    "rank": "17"
  },
  ...
]
```

## Development and Contribution

I welcome any contributions to this project, so feel free!
