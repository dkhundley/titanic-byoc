# Importing the necessary Python libraries
import pickle
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse



## API SETUP AND INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Instantiating FastAPI
api = FastAPI()

# Loading the Titanic trained model
with open('../models/rfc_pipeline.pkl', 'rb') as f:
    rfc_pipeline = pickle.load(f)



## API ENDPOINTS
## ---------------------------------------------------------------------------------------------------------------------
# Defining the predict endpoint
@api.post('/invocations')
async def predict(request: Request):

    # Get the JSON response from the body of the request
    input_data = await request.json()

    # Transforming the input JSON data into a Pandas DataFrame
    input_df = pd.DataFrame([input_data])

    # Generating prediction from the model
    pred = int(rfc_pipeline.predict(input_df)[0])

    # Returning the prediction back to the caller
    return JSONResponse({'prediction': pred})


# Defining the health endpoint
@api.get('/ping')
async def health():
    return JSONResponse({'status': 'healthy!'})