KDV_ORANI = 20
TRT_PAYI = 12
KULTUR_BAKANLIGI = 1


def otv_oran_hesapla(fiyat):
    if fiyat < 1_500:
        return 25
    elif fiyat < 3_000:
        return 40
    else:
        return 50
