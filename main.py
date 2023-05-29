from fastapi import FastAPI
import requests
from v2_convert import ConvertV2
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
import base64


app = FastAPI()


def convert_url_to_base(input_data):
    input_data = base64.b64encode(requests.get(input_data).content)
    input_data = input_data.decode('utf8')
    return input_data


class PredictRequest(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: str
    parameters: Dict[str, Any] = Field(default_factory=dict)


@app.post('/predict')
def predict(request: PredictRequest):
    hf = request.hf_pipeline
    model_url = request.model_deployed_url
    inputs = request.inputs
    parameters = request.parameters

    if hf == 'object-detection':
        inputs = convert_url_to_base(inputs)

    payload = ConvertV2.v2_format(hf, inputs, parameters)

    res = requests.post(model_url, json=payload)

    output = res.json()['outputs'][0]['data'][0]

    return output
