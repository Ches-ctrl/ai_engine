import requests
from datetime import datetime
import json
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

def fetch_jobs(title_filter: str = "Data Engineer", location_filter: str = "United States") -> None:
    """Fetch jobs from API and save to JSON"""
    url = "https://active-jobs-db.p.rapidapi.com/active-ats-24h"

    querystring = {
        "title_filter": title_filter,
        "location_filter": location_filter
    }

    headers = {
        "x-rapidapi-key": "dfd4045927mshedc7f1ec385d46bp166d3bjsn92bbc50de45d",
        "x-rapidapi-host": "active-jobs-db.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        jobs_data = response.json()

        if not isinstance(jobs_data, list):
            logging.error(f"Unexpected API response format: {type(jobs_data)}")
            return []

        # Create unique filename for each search
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        json_dir = Path('data/jobs_json')
        json_dir.mkdir(parents=True, exist_ok=True)

        filename = f'jobs_{title_filter.replace(" ", "_")}_{timestamp}.json'
        json_path = json_dir / filename

        # Save with metadata
        output_data = {
            "metadata": {
                "search_title": title_filter,
                "search_location": location_filter,
                "timestamp": timestamp,
                "total_jobs": len(jobs_data)
            },
            "jobs": jobs_data
        }

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        logging.info(f"Saved {len(jobs_data)} jobs to {json_path}")

        # Verify the save
        with open(json_path, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
            if len(saved_data["jobs"]) != len(jobs_data):
                logging.error(f"Save verification failed! Expected {len(jobs_data)} jobs but saved {len(saved_data['jobs'])}")

        return jobs_data

    except requests.RequestException as e:
        logging.error(f"API request failed: {str(e)}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse API response: {str(e)}")
        raise
    except IOError as e:
        logging.error(f"Failed to save jobs data: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        # Fetch data engineer jobs
        jobs = fetch_jobs("Data Engineer", "United States")
        print(f"Found {len(jobs)} Data Engineer jobs")

        # Fetch software engineer jobs
        jobs = fetch_jobs("Software Engineer", "Remote")
        print(f"Found {len(jobs)} Software Engineer jobs")

    except Exception as e:
        print(f"Error: {str(e)}")
