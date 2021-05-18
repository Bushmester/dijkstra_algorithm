import os

from dotenv import load_dotenv


load_dotenv()

TESTING_DATA = os.getenv("TESTING_DATA")
MEASUREMENTS = os.getenv("MEASUREMENTS")
