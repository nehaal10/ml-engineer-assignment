# ml-engineer-assignment
the goal of this assignment is to convert the hf pipeline input to v2Format.

# Test out the URL deployed in TrueFoundry 
## URL : https://ml-assignment-workspace-8000.demo1.truefoundry.com
### custom input
```json
{
  "hf_pipeline": "zero-shot-classification",
  "model_deployed_url": "https://zero-shot-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/zero-shot-class/infer",
  "inputs": "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
  "parameters": {"candidate_labels": ["refund", "legal", "faq"]}
}
```
