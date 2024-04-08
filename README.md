# Factiverse API Documentation

## Obtaining Credentials
To access Factiverse APIs, you need to acquire a `client_id` and a `client_secret`. These can be obtained along with pricing information by contacting the Factiverse sales team.

**Contact**: info@factiverse.ai

## Detailed API Documentation
For comprehensive information on the Factiverse API, visit:
[Factiverse API Documentation](https://api.factiverse.ai/v1/redoc)


## Accessing APIs via Curl
### Obtaining an Access Token
```bash
curl --request POST \
  --url https://auth.factiverse.ai/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"YOUR_CLIENT_ID","client_secret":"YOUR_CLIENT_SECRET","audience":"https://factiverse/api","grant_type":"client_credentials"}'
```


### Using the Access Token

```bash
# Example: Sending an API request
curl -X POST [api_endpoint] \
-H "Content-Type: application/json" \
-H "Authorization: Bearer [YOUR_ACCESS_TOKEN]" \
-d 'payload_json'
```
Note: Replace [api_endpoint] and ‘payload_json’ as per your requirements.

Fill the api_endpoint. For example, for factisearch (claim_search) it is https://api.factiverse.ai/v1/claim_search 
And fill the payload_json for the selected endpoint. For example, for claim_search

```
payload_json = '{
    "query": "The earth is not flat",
    "lang": "en",
    "searchEngine": ["fact_search_elasticsearch"]
}'
```


## Accessing APIs using Python
### Set Up Environment
1. **Install Python and Required Libraries**:
   ```bash
   pip install requests python-dotnev
   ```

2. **Import Libraries**:
   ```python
   import requests
   import json
   ```

3. **Define API Endpoint and Credentials**:
   ```python
   api_endpoint = "https://api.factiverse.no/v1/claim_search"
   token_url = "https://auth.factiverse.ai/authorize"  # Replace if different
   client_id = "your_client_id"  # Replace with your client ID
   client_secret = "your_client_secret"  # Replace with your client secret
   ```

4. **Obtain Access Token**:
   ```python
   def get_access_token(client_id, client_secret, token_url):
       payload = {
           "grant_type": "client_credentials",
           "client_id": client_id,
           "size": 10,
           "client_secret": client_secret,
       }
       response = requests.post(token_url, data=payload)
       if response.status_code == 200:
           return response.json()["access_token"]
       else:
           raise Exception(f"Failed to obtain token: {response.status_code} {response.text}")

   access_token = get_access_token(client_id, client_secret, token_url)
   ```

5. **Create Request Headers**:
   ```python
   headers = {
       "Content-Type": "application/json",
       "Authorization": f"Bearer {access_token}"
   }
   ```

6. **Define the Payload for claim_search**:
   ```python
   payload = {
       "query": "The earth is not flat",  # Your search query
       "lang": "en",  # Language code
       "searchEngine": ["fact_search_elasticsearch"]
   }
   ```

7. **Make the Request**:
   ```python
   response = requests.post(api_endpoint, headers=headers, json=payload)
   ```

8. **Handle the Response**:
   ```python
   if response.status_code == 200:
       # Successful request
       data = response.json()
       print(json.dumps(data, indent=4))
   else:
       # Handle errors
       print("Error:", response.status_code, response.text)
   ```

## This repository provides a python example.

1.  **Install Python and Required Libraries**:
   ```bash
   pip install requests python-dotnev
   ```

2. **Fill in `CLIENT_ID` and `CLIENT_SECRET` you got from Factiverse in .env**
3. **Run the python script:**
   ```bash
   python -m src.factisearch_example
   ```

