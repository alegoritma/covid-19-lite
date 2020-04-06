from requests import get
WORLDOMETER_URL = "https://www.worldometers.info/coronavirus/"


def fetch(url=WORLDOMETER_URL):
    return get(url)
