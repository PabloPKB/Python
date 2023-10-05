"""
Criando datas com módulo datetime
datetime (ano, mês, dia)
datetime (ano, mês, dia, horas, minutos, segundos)
"""
from datetime import datetime

data_str_data = '2022-04-20 07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2022, 4, 20, 7, 36, 23)
data = datetime.strptime(data_str_data, data_str_fmt)

print(data)
