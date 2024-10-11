def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade >= 18 < 65:
        return f'{idade} anos, voto obrigatório.'
    elif idade >= 16 < 18 or idade > 65:
        return f'{idade} anos, voto opcional.'
    else:
        return f'{idade} anos, voto negado'
print(voto(1946))