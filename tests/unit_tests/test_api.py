# Importing the necessary Python libraries
import json
from fastapi.testclient import TestClient
from container.api import api



## TEST CLIENT INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Instantiating the FastAPI test client
client = TestClient(api)

# Loading in the test data from JSON file
with open('test_json.json', 'rb') as f:
    test_json =  json.load(f)



## UNIT TEST CREATION
## ---------------------------------------------------------------------------------------------------------------------
# Creating a unit test for the "invocations" (predict) endpoint
def test_invocations_endpoint():
    response = client.post('/invocations', json = test_json)
    assert response.status_code == 200
    assert response.json() == {'survival_prediction': 0}

# Creating a unit test for the "ping" (health) endpoint
def test_ping_endpoint():
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'status': 'healthy!'}