# conda activate allpy310

# Данные о токенах с платформы DexScreener

import requests
import json

# API endpoint
API_URL = "https://api.dexscreener.com/token-boosts/top/v1"

def fetch_token_data():
    """Fetch token data from the API and display all relevant details including icons and links."""
    try:
        # Make the API request
        response = requests.get(API_URL)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()

            # Iterate through the tokens and display relevant details
            for token in data:
                url = token.get("url", "N/A")
                chain_id = token.get("chainId", "N/A")
                token_address = token.get("tokenAddress", "N/A")
                header = token.get("header", "No header available")
                icon = token.get("icon", "No icon available")
                description = token.get("description", "No description available")

                # Handle links if available
                links = token.get("links", [])
                formatted_links = "\n".join(
                    [f"{link.get('type', 'Link')}: {link.get('url', 'No URL')}" for link in links]
                )

                # Print the token details
                print(f"URL: {url}")
                print(f"Chain ID: {chain_id}")
                print(f"Token Address: {token_address}")
                print(f"Header: {header}")
                print(f"Icon: {icon}")
                print(f"Description: {description}")
                print(f"Links:\n{formatted_links if links else 'No links available'}")
                print("-" * 40)

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_token_data()
