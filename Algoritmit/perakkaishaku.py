def perakkaishaku(lista, kohde):
    """Peräkkäishaku, toimii vain numeerisiin pienimmästä suurimpaan järjesteltyihin listoihin."""
    yrityksia, indx = 0, 0

    while indx <= len(lista)-1:
        yrityksia += 1
        if lista[indx] == kohde:
            return [indx, yrityksia]
        else:
            indx += 1
    return None