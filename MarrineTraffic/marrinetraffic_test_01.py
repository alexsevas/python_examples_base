import requests
import sys

def get_ship_position(ship_id):

    url = "https://www.marinetraffic.com/en/ais/details/ships/shipid:{}".format(ship_id)

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "user-agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def main():
    from datetime import datetime

    data = get_ship_position("3121988")
    ts = datetime.utcfromtimestamp(data["lastPos"])
    print("Last known position: {} / {} @ {}".format(data["lat"], data["lon"], ts))

    return 0


if __name__ == "__main__":

    sys.exit(main())