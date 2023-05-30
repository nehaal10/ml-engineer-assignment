import requests
from url_hf_config import Config


class retrive:
    def __init__(self, url, hf_pipeline, inputs, parameters={}):
        self.api = url
        self.hf_pipeline = hf_pipeline
        self.inputs = inputs
        if len(list(parameters.keys())) == 0:
            self.parameters = {}
        else:
            self.parameters = parameters

    def get(self):
        payload = {
            "hf_pipeline": self.hf_pipeline,
            "model_deployed_url": Config.task_urls[self.hf_pipeline],
            "inputs": self.inputs,
            "patameters": self.parameters
        }

        response = requests.post(self.api, json=payload)

        output = response.json()

        return output


if __name__ == "__main__":
    ret = retrive(Config.custom_deployed_url, 'text-generation', 'hello all,')

    ans = ret.get()
    print(ans)
