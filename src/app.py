import logging
import requests
from flask import Flask, jsonify, abort

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SWAPI_URL = 'https://swapi.dev/api/people/'


def fetch_and_sort_data():
    try:
        logger.info("Fetching data from SWAPI People endpoint.")
        response = requests.get(SWAPI_URL)
        
        if response.status_code != 200:
            logger.error(f"Failed to fetch data from SWAPI: {response.status_code}")
            abort(500, description="Failed to fetch data from SWAPI.")
        
        data = response.json()
        people = data.get('results', [])
        
        if not people:
            logger.warning("No data found in the response.")
            abort(404, description="No data found.")
        
        # Sort data by 'name' in ascending order
        sorted_people = sorted(people, key=lambda person: person['name'].lower())
        
        logger.info(f"Sorted {len(sorted_people)} people by name.")
        return sorted_people
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception: {e}")
        abort(500, description="Error occurred while fetching data.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        abort(500, description="An unexpected error occurred.")


@app.route('/sorted-people', methods=['GET'])
def get_sorted_people():
    sorted_people = fetch_and_sort_data()
    return jsonify(sorted_people)


if __name__ == '__main__':
    logger.info("Starting microservice.")
    app.run(debug=True, host='0.0.0.0', port=5000)

