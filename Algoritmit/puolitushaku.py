def puolitushaku(lista, kohde):
    """Puolitushaku, toimii vain numeerisiin pienimmästä suurimpaan järjesteltyihin listoihin."""
    yrityksia, ensimmainen, viimeinen = 0, 0, len(lista)-1

    while ensimmainen <= viimeinen:
        yrityksia += 1
        keskikohta = (ensimmainen + viimeinen) // 2
        # Jos listan keskikohta on sama kuin haettu kohde, palautetaan tulos ja kuinka monta yritystä meni
        if lista[keskikohta] == kohde:
            return [keskikohta, yrityksia]
        # Jos listan keskikohta on pienempi kuin haettu kohde, nostetaan haun ensimmäinen elementti keskikohdan eteen
        elif lista[keskikohta] < kohde:
            ensimmainen = keskikohta + 1
        # Jos listan keskikohta on suurempi kuin haettu kohde, tiputetaan haun viimeinen elementti keskikohdan taakse
        else:
            viimeinen = keskikohta - 1
    # Jos lista käytiin läpi ilman, että kohde löytyi listasta, palautetaan None
    return None

