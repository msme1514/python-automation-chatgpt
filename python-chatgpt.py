import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to Open AI")
parser.add_argument("file_name", help="The file name to save python code")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt" : f"Write python script for {args.prompt}. Provide only code, no text",
    "max_tokens": 1000,
    "temperature" : 0
}

response = requests.post(api_endpoint,headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Respone failed with status code : {str(response.status_code)}" )