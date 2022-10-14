import requests
import pathlib
BASE=pathlib.Path(__file__)
parent=BASE.parent


file_path=parent/'trial_file_1.pdf'
file_path=file_path.as_posix()

url = "http://localhost:5004/api/v1/payslip_document_classification/jobs"

payload={}
files=[
  ('file2',('PAYSLIP-2.PDF~wJdGPCP3e1~99~9954498360389682815.pdf8650012045297067581-suffix.pdf',open(file_path,'rb'),'application/pdf'))
]
headers = {
  'security-header': 'f4c33723-2d7e-4777-b5da-68f4b3e22313',
  'publish-iteration-name': 'Iteration3'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
