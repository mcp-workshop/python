import googlemaps
import os

api_key = os.getenv("GOOGLE_MAPS_API_KEY")

def get_travel_time(origin: str, destination: str, travel_mode: str = "driving", arrival_time: str = None) -> dict:
    gmaps = googlemaps.Client(key=api_key)
    directions = gmaps.directions(
        origin,
        destination,
        mode=travel_mode.lower(),
        arrival_time= arrival_time,
    )
    if not directions:
        raise Exception("No route found")
    leg = directions[0]['legs'][0]
    response = {
        "origin": leg['start_address'],
        "destination": leg['end_address'],
        "travel_mode": travel_mode,
        "duration_text": leg['duration']['text'],
        "duration_seconds": leg['duration']['value']
    }
    print(response)
    return response

def get_address_from_coordinates(latitude: float, longitude: float) -> str:
    gmaps = googlemaps.Client(key=api_key)
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    
    if not reverse_geocode_result:
        raise Exception("No address found for the given coordinates")
    
    return reverse_geocode_result[0]['formatted_address']
  
def get_coordinates_from_address(address: str) -> tuple:
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(address)
    
    if not geocode_result:
        raise Exception("No coordinates found for the given address")
    
    location = geocode_result[0]['geometry']['location']
    return (location['lat'], location['lng'])