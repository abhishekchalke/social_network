
import requests as r


url = 'http://127.0.0.1:8000/users/api/login/'

token = 'JCmDQ22RKJnJnY8qRlMaTjgEwW6tT5FQ'
head = {'Authorization': f'Token {token}'}

print("head",head)
data = {
    "email": "Girish@gmail.com",
    "password": "qwaszx"
}

res = r.post(url, json=data, verify=False)
# res = r.post(url, headers=head)

print("res", res)
print(res.text)



