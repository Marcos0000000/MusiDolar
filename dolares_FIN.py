import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive",]

creds = ServiceAccountCredentials.from_json_keyfile_name(f"credenciales.json", scope,)
client = gspread.authorize(creds)
sheet_1 = client.open_by_url("https://docs.google.com/spreadsheets/d/14eJM34gLJXF9R5-iqQJc_V6s8D-aj5GKiG6eo5-QvBk/edit").sheet1

casa = ["oficial","blue","bolsa","contadoconliqui","cripto","mayorista","solidario"]
dolares_financieros = []
for i in casa:
    response = requests.get(f"https://api.argentinadatos.com/v1/cotizaciones/dolares/{i}")
    #print(response.json())
    dolares_financieros.append(response.json())

saltarse_filas = 3
print_dolares_sheet = ['Dolar Oficial','Dolar Blue','Dolar MEP','Dolar CCL','Dolar USDT','Dolar Mayorista']
for i in range(len(print_dolares_sheet)):
    sheet_1.update_cell(i+saltarse_filas,2,f"{str(print_dolares_sheet[i])}")
    sheet_1.update_cell(i+saltarse_filas,3,f"{str(dolares_financieros[i][-1]['venta']).replace(".",",")}")       ##Es para que lo tome Gsheets
    sheet_1.update_cell(i+saltarse_filas,4,f"{str(dolares_financieros[i][-2]['venta']).replace(".",",")}")
print("Listo")
