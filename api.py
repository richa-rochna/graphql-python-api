import requests
import os
from flask import Flask

query = """query DigitalBankingJourneysByBusinessLine() {
    dBJourneys(orderBy: title_ASC) {
      id
      title
      slug
      introStatement
    }
  }
"""

url = os.getenv("URL")
token = os.getenv("HYGRAPH_TOKEN")
headers = {"Authorization": f"Bearer {token}"}
app = Flask(__name__)


@app.route("/getJourney")
def get_actor():
    payload = {"query": query}
    r = requests.post(url, json=payload, headers=headers)
    json_data = r.json()
    return {"response": json_data}
