import requests
import os
from flask import Flask

query_actor = """query Actor {
    actor(where: {id: "clrgc0jejnxgq0cuweyp1g4vl"}) {
    name
    biography
    photo {
      id
    }
    episodes {
      id
      shows {
        id
      }
    }
  }
}
"""

url = os.getenv("URL")
token = os.getenv("HYGRAPH_TOKEN")
headers = {"Authorization": f"Bearer {token}"}
app = Flask(__name__)


@app.route("/get_actor")
def get_actor():
    payload = {"query": query_actor}
    r = requests.post(url, json=payload, headers=headers)
    json_data = r.json()
    return {"actor": json_data}
