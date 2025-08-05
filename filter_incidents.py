#!/usr/bin/env python3
"""
Script to fetch Seattle Fire Department data and filter incidents within one mile
of specified coordinates.
"""

import json
import requests
import math
from typing import List, Dict, Any

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the distance between two points on Earth using the Haversine formula.
    Returns distance in miles.
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in miles
    r = 3956
    
    return c * r

def fetch_fire_data(api_url: str) -> List[Dict[str, Any]]:
    """
    Fetch fire incident data from the Seattle API.
    """
    try:
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def filter_incidents_by_distance(incidents: List[Dict[str, Any]], 
                                target_lat: float, 
                                target_lon: float, 
                                max_distance_miles: float = 1.0) -> List[Dict[str, Any]]:
    """
    Filter incidents to only those within the specified distance of the target coordinates.
    """
    filtered_incidents = []
    
    for incident in incidents:
        try:
            # Extract latitude and longitude from the incident
            incident_lat = float(incident.get('latitude', 0))
            incident_lon = float(incident.get('longitude', 0))
            
            # Skip if coordinates are invalid
            if incident_lat == 0 and incident_lon == 0:
                continue
                
            # Calculate distance
            distance = haversine_distance(target_lat, target_lon, incident_lat, incident_lon)
            
            # Add distance to incident data for display
            incident_with_distance = incident.copy()
            incident_with_distance['distance_miles'] = round(distance, 3)
            
            # Filter by distance
            if distance <= max_distance_miles:
                filtered_incidents.append(incident_with_distance)
                
        except (ValueError, TypeError) as e:
            # Skip incidents with invalid coordinate data
            continue
    
    # Sort by distance
    filtered_incidents.sort(key=lambda x: x['distance_miles'])
    return filtered_incidents

def read_coordinates_from_file(filename: str) -> tuple:
    """
    Read coordinates from the data.txt file.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        api_url = None
        latitude = None
        longitude = None
        
        for line in lines:
            line = line.strip()
            if line.startswith('API Access:'):
                api_url = line.split(':', 1)[1].strip()
            elif line.startswith('My latitude:'):
                latitude = float(line.split(':', 1)[1].strip())
            elif line.startswith('My longitude:'):
                longitude = float(line.split(':', 1)[1].strip())
        
        return api_url, latitude, longitude
        
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None, None, None
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        return None, None, None

def display_incidents(incidents: List[Dict[str, Any]]):
    """
    Display filtered incidents in a readable format.
    """
    if not incidents:
        print("No incidents found within one mile of the specified coordinates.")
        return
    
    print(f"\nFound {len(incidents)} incidents within one mile:")
    print("=" * 80)
    
    for i, incident in enumerate(incidents, 1):
        print(f"\n{i}. Incident #{incident.get('incident_number', 'N/A')}")
        print(f"   Type: {incident.get('type', 'N/A')}")
        print(f"   Address: {incident.get('address', 'N/A')}")
        print(f"   Date/Time: {incident.get('datetime', 'N/A')}")
        print(f"   Distance: {incident.get('distance_miles', 'N/A')} miles")
        print(f"   Coordinates: {incident.get('latitude', 'N/A')}, {incident.get('longitude', 'N/A')}")

def main():
    """
    Main function to orchestrate the data fetching and filtering process.
    """
    print("Seattle Fire Department Incident Filter")
    print("=" * 40)
    
    # Read coordinates from data.txt
    api_url, target_lat, target_lon = read_coordinates_from_file('data.txt')
    
    if not all([api_url, target_lat, target_lon]):
        print("Error: Could not read coordinates from data.txt")
        return
    
    print(f"Target coordinates: {target_lat}, {target_lon}")
    print(f"API URL: {api_url}")
    print("\nFetching fire incident data...")
    
    # Fetch all incidents
    incidents = fetch_fire_data(api_url)
    
    if not incidents:
        print("No data received from the API.")
        return
    
    print(f"Retrieved {len(incidents)} total incidents")
    
    # Filter incidents within one mile
    filtered_incidents = filter_incidents_by_distance(incidents, target_lat, target_lon, 1.0)
    
    # Display results
    display_incidents(filtered_incidents)
    
    # Save filtered results to a file
    output_file = 'filtered_incidents.json'
    with open(output_file, 'w') as f:
        json.dump(filtered_incidents, f, indent=2)
    
    print(f"\nFiltered results saved to {output_file}")

if __name__ == "__main__":
    main() 