import requests

# We have put the localhost URL as default, feel free to change it
url = "http://127.0.0.1:3000/predict"
# This a simple example of input
input_simple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

res = requests.post(url, json=input_simple)
assert res.status_code == 200
print(res.json())
# This a example of input with several inputs
input_multiple = {
     "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
               [5.0, 0.98, 0.32, 18.9, 0.050, 75.0, 122.0, 0.401, 3.1, 0.21, 1.2]]
 }

res = requests.post(url, json=input_multiple)
assert res.status_code == 200
print(res.json())