import requests
import json

url = "https://apidatos.ree.es/es/datos/generacion/no-renovables-detalle-emisiones-CO2?start_date=2019-01-01T00:00&end_date=2019-12-31T23:59&time_trunc=day"
data  = requests.get(url).text
js = json.loads(data)
fe = 0.0
samples = 0
for fe_d in js['included'][0]['attributes']['values']:
    fe = fe + float(fe_d['percentage'])
    samples = samples + 1
print(fe/samples)