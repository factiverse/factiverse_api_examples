"""This script demonstrates how to use the Factiverse API to search for claims."""
import json
import os
from typing import Dict, List

import dotenv
import requests

api_endpoint = "https://api.factiverse.ai/v1/claim_search"
token_url = "https://auth.factiverse.ai/oauth/token"
dotenv.load_dotenv()

def get_access_token(client_id: str, client_secret: str, token_url: str) -> str:
    """Get access token from Factiverse API.

    Args:
        client_id: Client ID.
        client_secret: Client secret.
        token_url: Token URL.

    Raises:
        Exception: If token request fails.

    Returns:
        Access token.
    """
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        return response.json()["access_token"] 
    else:
        raise Exception(f"Failed to obtain token: {response.status_code} {response.text}") 


def factisearch(query: str, access_token: str, lang: str="en") -> requests.Response:
    """Search for claims.

    Args:
        query: Query string.
        lang: Language code.
        access_token: Access token for Factiverse API.

    Returns:
        Response object.
    """
    headers = {
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "query": query,
        "lang": lang, # Language code
        "searchEngine": ["fact_search_elasticsearch"],
        "size": 10,
    }
    response = requests.post(api_endpoint, headers=headers, json=payload)
    return response
        
if __name__ == '__main__':
    client_id = os.getenv("CLIENT_ID") # Fill in this value in .env
    client_secret = os.getenv("CLIENT_SECRET") # Fill in this value in .env
    access_token = get_access_token(client_id, client_secret, token_url)
    response = factisearch("Earth is not flat", access_token)
    if response.status_code == 200:
    # Successful request
        data = response.json() 
        print(json.dumps(data, indent=4))
    else:
        # Handle errors
        print("Error:", response.status_code, response.text)
    
