## Genera la capa gold final

def capa_gold(data_anex_1_pla,
              data_anex_2_pla,
              data_divi_pla):
    ## Unión de Anexo 1 y Anexo 2
    pre_fin = data_anex_1_pla.merge(data_anex_2_pla, on="cod_muerte", how="left")
    ## Unión pre_fin con data divipola
    data_gold = pre_fin.merge(data_divi_pla, on = 'cod_dane', how='left')

    return data_gold