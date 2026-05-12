## Espacio de almacenamiento de diccionarios de variables categóricas

## Área de Defunción
dicc_area_defuncion = {1: 'Cabecera municipal',
                       2: 'Centro poblado',
                       3: 'Rural disperso',
                       9: 'Sin información'}

## Sitio defunción
dicc_sitio_defuncion = {1: 'Hospital/clínica',
                        2: 'Centro/puesto de salud',
                        3: 'Casa/domicilio',
                        4: 'Lugar de trabajo',
                        5: 'Via pública',
                        6: 'Otro',
                        9: 'Sin información'}

## Meses
dicc_meses = {1: 'Enero',
              2: 'Febrero',
              3: 'Marzo',
              4: 'Abril',
              5: 'Mayo',
              6: 'Junio',
              7: 'Julio',
              8: 'Agosto',
              9: 'Septiembre',
              10: 'Octubre',
              11: 'Noviembre',
              12: 'Diciembre'}

## Sexo
dicc_sexo = {1: 'Masculino',
             2: 'Femenino',
             3: 'Indeterminado'}

## Estado Civil
dicc_estado_civil = {1: 'No estaba casado(a) y llevaba dos o más años viviendo con su pareja',
                     2: 'No estaba casado(a) y llevaba menos de dos años viviendo con su pareja',
                     3: 'Estaba separado(a), divorciado(a)',
                     4: 'Estaba viudo(a)',
                     5: 'Estaba soltero(a)',
                     6: 'Estaba casado(a)',
                     9: 'Sin información'}

## Grupo de Edad
dicc_grupo_edad = {'00': 'Menor de una hora',
                    '01': 'Menor de un día',
                    '02': 'De 1 a 6 días',
                    '03': 'De 7 a 27 días',
                    '04': 'De 28 a 29 días',
                    '05': 'De 1 a 5 meses',
                    '06': 'De 6 a 11 meses',
                    '07': 'De 1 año',
                    '08': 'De 2 a 4 años',
                    '09': 'De 5 a 9 años',
                    '10': 'De 10 a 14 años',
                    '11': 'De 15 a 19 años',
                    '12': 'De 20 a 24 años',
                    '13': 'De 25 a 29 años',
                    '14': 'De 30 a 34 años',
                    '15': 'De 35 a 39 años',
                    '16': 'De 40 a 44 años',
                    '17': 'De 45 a 49 años',
                    '18': 'De 50 a 54 años',
                    '19': 'De 55 a 59 años',
                    '20': 'De 60 a 64 años',
                    '21': 'De 65 a 69 años',
                    '22': 'De 70 a 74 años',
                    '23': 'De 75 a 79 años',
                    '24': 'De 80 a 84 años',
                    '25': 'De 85 a 89 años',
                    '26': 'De 90 a 94 años',
                    '27': 'De 95 a 99 años',
                    '28': 'De 100 años y más',
                    '29': 'Edad desconocida'}

## Nivel Educativo
dicc_nivel_educativo = {1: 'Preescolar',
                         2: 'Básica primaria',
                         3: 'Básica secundaria',
                         4: 'Media académica o clásica',
                         5: 'Media técnica',
                         6: 'Normalista',
                         7: 'Técnica profesional',
                         8: 'Tecnológica',
                         9: 'Profesional',
                         10: 'Especialización',
                         11: 'Maestría',
                         12: 'Doctorado',
                         13: 'Ninguno',
                         99: 'Sin información'}

## Categorización de edades
dicc_grupo_edad_categoria = {
    # Mortalidad neonatal
    0: "Mortalidad neonatal (Menor de 1 mes)",
    1: "Mortalidad neonatal (Menor de 1 mes)",
    2: "Mortalidad neonatal (Menor de 1 mes)",
    3: "Mortalidad neonatal (Menor de 1 mes)",
    4: "Mortalidad neonatal (Menor de 1 mes)",
    # Mortalidad infantil
    5: "Mortalidad infantil (1 a 11 meses)",
    6: "Mortalidad infantil (1 a 11 meses)",
    # Primera infancia
    7: "Primera infancia (1 a 4 años)",
    8: "Primera infancia (1 a 4 años)",
    # Niñez
    9: "Niñez (5 a 14 años)",
    10: "Niñez (5 a 14 años)",
    # Adolescencia
    11: "Adolescencia (15 a 19 años)",
    # Juventud
    12: "Juventud (20 a 29 años)",
    13: "Juventud (20 a 29 años)",
    # Adultez temprana
    14: "Adultez temprana (30 a 44 años)",
    15: "Adultez temprana (30 a 44 años)",
    16: "Adultez temprana (30 a 44 años)",
    # Adultez intermedia
    17: "Adultez intermedia (45 a 59 años)",
    18: "Adultez intermedia (45 a 59 años)",
    19: "Adultez intermedia (45 a 59 años)",
    # Vejez
    20: "Vejez (60 a 84 años)",
    21: "Vejez (60 a 84 años)",
    22: "Vejez (60 a 84 años)",
    23: "Vejez (60 a 84 años)",
    24: "Vejez (60 a 84 años)",
    # Longevidad / Centenarios
    25: "Longevidad / Centenarios (85 a 100+ años)",
    26: "Longevidad / Centenarios (85 a 100+ años)",
    27: "Longevidad / Centenarios (85 a 100+ años)",
    28: "Longevidad / Centenarios (85 a 100+ años)",
    # Edad desconocida
    29: "Edad desconocida (Sin información)"
}