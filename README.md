# ml-engineer-assignment
the goal of this assignment is to convert the hf pipeline input to v2Format.

# Test out the URL deployed in TrueFoundry 
#### URL : https://ml-assignment-workspace-8000.demo1.truefoundry.com/predict
### custom input example
```json
{
  "hf_pipeline": "zero-shot-classification",
  "model_deployed_url": "https://zero-shot-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/zero-shot-class/infer",
  "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
  "parameters": {"candidate_labels": ["refund", "legal", "faq"]}
}
```
### output example
```json
"{\"sequence\": \"Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!\", \"labels\": [\"refund\", \"faq\", \"legal\"], \"scores\": [0.937849760055542, 0.04914167523384094, 0.013008514419198036]}"
```

## Local Setup steps
#### clone the ropository
```git
git clone https://github.com/nehaal10/ml-engineer-assignment.git
```
#### create virtual environment
```git
python -m venv .<give your virtual environment name>
```
#### then run main.py file to get access to localhost
```power shell
python main.py
```
#### copy paste the localhost url in the browser to try out the api
#### to deploy the the loacal host in TrueFoundry
```power shell
python deploy.py --workspace_fqn <place your TrueFoundry workspace function here>
```

## To Test Out Already Deployed Url
#### clone this repo as mentioned above in your virtual environment 
#### then open the file named getOutput.py and change the hf pipeline and inputs
#### then run this command
```git
python getOutput.py
```
