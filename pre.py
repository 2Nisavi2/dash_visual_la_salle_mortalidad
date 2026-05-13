print("INICIANDO LECTURA DE FUENTES BRONZE 🥉-----------------------------")
from modulo_data.lectura import cargar_archivos_excel
data = cargar_archivos_excel("data")

print("GENERANDO TRANSFORMACIONES A SILVER 🥈-----------------------------")
from modulo_data.tratamiento_data import transformacion_data
data_gold = transformacion_data(data['anexo_1'], data['anexo_2'], data['anexo_3'])

print("CREANDO CAPA GOLD 🥇-----------------------------------------------")
from modulo_data.capa_gold import capa_gold
capa_gold_data = capa_gold(data_gold[0], data_gold[1], data_gold[2])

print("ALMACENANDO CAPA GOLD 🎖️-------------------------------------------")
from modulo_data.almacenamiento_gold import almacenar_gold
almacenar_gold(capa_gold_data, "data/parquet_gold")

print("PREPROCESAMIENTO FINALIZADO 🎉-------------------------------------")