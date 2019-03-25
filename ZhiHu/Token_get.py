import requests

ak = 'CqPpHNnlapbprVdTbd1ZXNst'
sk = 'GWGuQPQSlDEQK9zmDA7AQqtVhX4PPDRo'

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(ak, sk)

res = requests. post(host)
print(res.text)