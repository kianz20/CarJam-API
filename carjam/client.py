import json
import requests
from queue import Queue

class Client:
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 Firefox/71.0",
            "Accept": "*/*",
            "content-type": "application/json",
        }
        
    def basic_details(self, plate):
        '''
        Returns an a json object containing basic details about the car
        Example of output shape:
        {"plate":"FKK351","vin":"7AT0H63WX10005902","chassis":"ACT10-0005902","current_vehicle_odometer_unit":"K","reported_stolen":"U",
            "make":"TOYOTA","year_of_manufacture":2000,"vehicle_type":7,"usage_level":1.91,"average_fleet_mileage":10500}
        '''
        
        resp = self.session.post(f'https://www.carjam.co.nz/car/?plate={plate}')
        raw_data = resp.text
        
        basic_details_start = raw_data.find("window.report.idh.vehicle") + 28
        basic_details_end = raw_data.find("}", basic_details_start) + 1
        
        json_data = json.loads(raw_data[basic_details_start:basic_details_end])

        return json_data
    
    def model_details(self, plate):
        '''
        Returns an a json object containing model details about the car
        Example of output shape:
        {"car_id":0,"chassis_number":"ACT10-0005902","make":"TOYOTA","model":"OPA","grade":"I","manufacture_date":"2000-09","body":"TA-ACT10",
            "engine":"1AZFSE","drive":"FF","transmission":"CVT"}
        '''
        
        resp = self.session.post(f'https://www.carjam.co.nz/car/?plate={plate}')
        raw_data = resp.text
        
        model_details_start = raw_data.find("window.jph_search") + 50
        model_details_end = raw_data.find("\"image\"", model_details_start) - 1
        
        json_data = json.loads(raw_data[model_details_start:model_details_end] + "}")

        return json_data
    
    def image(self, plate):
        '''
        Returns an a json object containing image urls of the car
        Example of output shape:
        {'image': 'photos.carjam.co.nz/jph/_search_img_catalog_10102041_200404.jpg', 
            'orig_image': 'photos.carjam.co.nz/jph/_search_img_catalog_10102041_200404.jpg'}
        '''
        
        resp = self.session.post(f'https://www.carjam.co.nz/car/?plate={plate}')
        raw_data = resp.text
        
        model_details_start = raw_data.find("window.jph_search") + 50
        image_url_start = raw_data.find("\"image\"", model_details_start) 
        image_url_end = raw_data.find("}", image_url_start) + 1 
        
        json_data = json.loads("{" + raw_data[image_url_start:image_url_end])

        # Fix the URLs by removing the leading `//` and replacing backslashes with forward slashes
        json_data['image'] = json_data['image'].replace('\\/', '/').replace('//', '')
        json_data['orig_image'] = 'photos.carjam.co.nz' + json_data['orig_image'].replace('\\/', '/').replace('/search/img/catalog/', '/jph/_search_img_catalog_')

        return json_data

        
    def odometer_history(self, plate): 
        '''
        Returns an array containing the odometer details of the car
        Example of output shape:
        [{"odometer_date":1678618800,"odometer_reading":"296662","odometer_unit":"K","odometer_source":"IW","days":7,"seconds":604800,
            "kms":359,"daily_usage":51.285714285714285}]
        '''
        
        resp = self.session.post(f'https://www.carjam.co.nz/car/?plate={plate}')
        raw_data = resp.text
        
        odometer_details_start = raw_data.find("window.report.idh.odometer_history") + 37
        odometer_details_end = raw_data.find("]", odometer_details_start) + 1
        
        json_data = json.loads(raw_data[odometer_details_start:odometer_details_end])
        
        return json_data