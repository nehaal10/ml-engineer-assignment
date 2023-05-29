'''config file which contails all urls and hf_pipeline names'''


class Config:
    task_urls = {
        "object-detection": "https://test-object-detect-nikhil-ws.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech/v2/models/test-object-detect/infer",
        "text-generation": "https://text-generation-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/text-generation/infer",
        "token-classification": "https://token-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/token-class/infer",
        "zero-shot-classification": "https://zero-shot-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/zero-shot-class/infer"
    }
