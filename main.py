import time
from fastapi import FastAPI
import requests
import calculation
import data_processing

app = FastAPI()

URL = "https://datahub.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/st_park_p/records?limit=10&offset=0&timezone=UTC"

def fetch_data():
    """Get data and return it in JSON"""
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()["results"]

@app.get("/data")
def get_data():
    """Route FastAPI"""
    data = fetch_data()
    return {"message": "Get data sucess", "data": data}

def process_data(data):
    """Data processing and calculations"""
    processed_data = []
    
    for parking in data:
        name = parking.get("nom")
        spot = parking.get("np_total")
        free_spaces = parking.get("libres")
        size = data_processing.spot_labeling(spot)
        taken, ratio = calculation.space_taken(spot,free_spaces)
        processed_data.append({
            "name": name,
            "size": size,
            "spot": data_processing.none_value_labeling(spot),
            "free_spaces": data_processing.none_value_labeling(free_spaces),
            "taken": taken,
            "ratio": ratio
        })

    return processed_data

    
def display_data(processed_data):
    """Console display"""
    print("\nProcessed Data :\n")
    print(f"{'Name':<50} {'Size':<10} {'Spot':<10} {'Free':<10} {'Taken':<10} {'Ratio (%)':<10}")
    print("-" * 70)
    for item in processed_data:
        print(f"{item['name']:<50} {item['size']:<10} {item['spot']:<10} {item['free_spaces']:<10} {item['taken']:<10} {item['ratio']:<10}")

if __name__ == "__main__":
    while True:
        try:
            start_time = time.perf_counter()

            data = fetch_data()
            processed_data = process_data(data)
            display_data(processed_data)

            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Execution time : {elapsed_time:.4f} second")
        except Exception as e:
            print(f"ERROR : {e}")

        print("\n Next refresh in 20 sec\n")
        time.sleep(20)

