from Clases import BandaEscolar

def save_data(diction:dict):
    with open(f'data.txt', 'w', encoding='utf-8') as data:
        for i in diction.values():
            data.write(
                f"{i.nombre.lower().strip()}:{i.institucion}:{i.codigo}:{i.categoria}:{i.puntaje_total}\n")
            for categoria, puntaje in i.puntaje.items():
                data.write(f"&{categoria}:{puntaje}\n")

def load_data(diction:dict):
    try:
        with open(f'data.txt', 'r', encoding='utf-8') as data:
            for line in data:
                line = line.strip()
                if line:
                    if line[0] == '&':
                        #PARA LOS PUNTAJES POR CATEGORIA
                        name_categoria, puntaje_categoria = line.split(':')
                        name_categoria = str(name_categoria).replace('&', '')
                        print(name_categoria, puntaje_categoria)
                        diction[next(reversed(diction))].puntaje[name_categoria] = int(puntaje_categoria)
                    else:
                        nombre, institucion, codigo, categoria, p_total = line.split(':')
                        b = BandaEscolar(nombre,institucion,codigo,categoria)
                    b.suma_total()
                    print(b.nombre, b.puntaje)
                    diction[codigo] = b
    except FileNotFoundError:
        # print("nO DATOS")
        with open(f'data.txt', 'w', encoding='utf-8') as data:pass
