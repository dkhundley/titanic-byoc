# Importing the necessary Python libraries
import cloudpickle
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse



## API SETUP AND INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Instantiating the FastAPI object
api = FastAPI()

# Loading the Titanic model from serialized pickle file
with open('../models/rfc_pipeline.pkl', 'rb') as f:
    rfc_pipeline = cloudpickle.load(f)



## API ENDPOINTS
## ---------------------------------------------------------------------------------------------------------------------
# Defining the predict endpoint
@api.post('/invocations')
async def predict(request: Request):

    # Getting the JSON from the body of the request
    input_json = await request.json()

    # Transforming the input JSON into a Pandas DataFrame
    input_df = pd.DataFrame(input_json, index = [0])

    # Getting the prediction from the Titanic model
    pred = int(rfc_pipeline.predict(input_df)[0])

    # Returning the prediction back to the caller
    return JSONResponse({'survival_prediction': pred})

# Defining the health endpoint
@api.get('/ping')
async def health():
    return JSONResponse({'status': 'healthy!'})