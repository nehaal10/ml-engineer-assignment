'''main app'''


class ConvertV2:
    '''class convert_v2 has a function v2 which converts the hugging face inputs 
    to v2 format'''

    def v2_format(hf_pipline, input_data, parameters):
        '''here in v2_format function , we convert each to pipeline to its respective v2 format'''

        if hf_pipline == 'text-generation':
            payload = {
                "parameters": {
                    "content_type": "str"
                },
                "inputs": [
                    {
                        "name": "array_inputs",
                        "shape": [
                            1
                        ],
                        "datatype": "BYTES",
                        "data": [
                            input_data
                        ]
                    },
                    {
                        "name": "max_new_tokens",
                        "shape": [
                            -1
                        ],
                        "datatype": "BYTES",
                        "data": [
                            "20"
                        ],
                        "parameters": {
                            "content_type": "hg_json"
                        }
                    }
                ]
            }

        elif hf_pipline == 'zero-shot-classification':

            payload = {
                "id": "string",
                "parameters": {
                    "content_type": "string",
                    "headers": {}
                },
                "inputs": [
                    {
                        'name': "sequences",
                        'shape': [-1],
                        'datatype':"BYTES",
                        'parameters':{"content_type": "str"},
                        'data': input_data,
                    },
                    {
                        'name': "candidate_labels",
                        'shape': [-1],
                        'datatype':"BYTES",
                        'parameters':{"content_type": "str"}
                    },
                ],
                "outputs": [],
            }
            para = list(parameters.values())[0]
            payload['inputs'][-1]['data'] = []
            for i in para:
                payload['inputs'][-1]['data'].append(i)

        elif hf_pipline == 'token-classification':
            payload = {
                "id": "string",
                "parameters": {
                    "content_type": "string",
                    "headers": {}
                },
                "inputs": [
                    {
                        'name': "inputs",
                        'shape': [-1],
                        'datatype':"BYTES",
                        'parameters':{"content_type": "str"},
                        'data': input_data,
                    }
                ],
                "outputs": [],
            }
        elif hf_pipline == "object-detection":
            payload = {
                "id": "string",
                "parameters": {
                    "content_type": "string",
                    "headers": {}
                },
                "inputs": [
                    {
                        'name': "inputs",
                        'shape': [-1],
                        'datatype':"BYTES",
                        'parameters':{"content_type": "pillow_image"},
                        'data': input_data,
                    }
                ],
                "outputs": [],
            }

        return payload
