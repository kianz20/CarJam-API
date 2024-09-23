[CarJam](https://www.carjam.co.nz/) is a resource for finding information about cars registered in NZ.

Unofficial Python API for Carjam

## Installation
``pip install git+https://github.com/kianz20/CarJam-API``

## Basic car details
```python
import carjam
client = carjam.Client()
details = client.basic_details('aaa000')
```

## Car model details
```python
import carjam
client = carjam.Client()
details = client.model_details('aaa000')
```

## Car images
```python
import carjam
client = carjam.Client()
image = client.image('aaa000')
```

## Car Odometer Details
```python
import carjam
client = carjam.Client()
image = client.odometer_history('aaa000')
```

## NZ Fleet Details
```python
import carjam
client = carjam.Client()
image = client.fleet_details(1)
```

## Development and Contribution
I welcome any contributions to this project, so feel free!
