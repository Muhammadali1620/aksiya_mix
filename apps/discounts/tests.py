import requests


response = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/')


print(response.json()[0]['Rate'])