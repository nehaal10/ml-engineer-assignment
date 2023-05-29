# ml-engineer-assignment
the goal of this assignment is to convert the hf pipeline input to v2Format.

# Test out the URL deployed in TrueFoundry 
## URL : https://ml-assignment-workspace-8000.demo1.truefoundry.com/predict
### custom input
```json
{
  "hf_pipeline": "zero-shot-classification",
  "model_deployed_url": "https://zero-shot-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/zero-shot-class/infer",
  "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
  "parameters": {"candidate_labels": ["refund", "legal", "faq"]}
}
```
### output
```json
"{\"sequence\": \"Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!\", \"labels\": [\"refund\", \"faq\", \"legal\"], \"scores\": [0.937849760055542, 0.04914167523384094, 0.013008514419198036]}"
```

## Local Setup steps
#### clone the ropository
```git
git clone 
```
