# import の実行
import requests

def get_weather_data():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    payload = {'city':'130010'}
    
    weather_data = requests.get(url, params=payload).json()
    # print(weather_data)
    
    data = {
        'title':weather_data['title'],
        'date':weather_data['forecasts'][1]['date'],
        'telop':weather_data['forecasts'][1]['telop'],
        'min_temperature':weather_data['forecasts'][1]['temperature']['min']['celsius'],
        'max_temperature':weather_data['forecasts'][1]['temperature']['max']['celsius'],
        'copyright':weather_data['copyright']['provider'][0]['name'],
        'timestamp':weather_data['publicTime']
    }
    
    return data
    
    # print(weather_data['publicTime'])
    # print(weather_data['forecasts'][1]['date']) 
    # print(weather_data['forecasts'][1]['telop']) 
    # print(weather_data['forecasts'][1]['temperature']['min']['celsius']) 
    # print(weather_data['forecasts'][1]['temperature']['max']['celsius']) 
    
    
        
    # class Forecast:
    #     def __init__(self, date, temperature):
    #         self.date = date
    #         self.temperature = temperature
            
    #     def get_json(self):
            
    #         return {'日付': self.date}
    
