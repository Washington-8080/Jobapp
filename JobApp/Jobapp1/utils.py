from django.shortcuts import render
import http.client
import json

def search_jobs(query, page=1, country='us', city=''):
    conn = http.client.HTTPSConnection("job-search-api1.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "eabda60bafmsh524608e76d10b6ap1f19cdjsn1261d937df1b",
        'x-rapidapi-host': "job-search-api1.p.rapidapi.com"
    }

    conn.request("GET", f"/v1/job-description-search?q={query}&page={page}&country={country}&city={city}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Decode the JSON response
    response_json = json.loads(data.decode("utf-8"))

    # Check if the 'data' key exists in the response
    if 'data' in response_json:
        jobs = response_json['data']
        # Process and return the job listings
        return jobs
    else:
        # Handle the error or unexpected response
        print("Error: 'data' key not found in the response.")
        print(f"Full response: {response_json}")
        return []

# Example usage:
# jobs = search_jobs('python developer', page=1, country='us', city='new york')
