from vergi_hesaplama import config


def vergi_hesapla(fiyat, oran):
    return fiyat / 100 * (oran + 100)


def main(fiyat: int) -> int:
    oran = config.KDV_ORANI + config.TRT_PAYI + config.KULTUR_BAKANLIGI + config.otv_oran_hesapla(fiyat)

    sonuc = vergi_hesapla(fiyat=fiyat, oran=oran)

    print("FIYAT: ", sonuc)
    print("KDV ORANI:", sonuc / config.KDV_ORANI)
    print("TRT PAYI:", sonuc / config.TRT_PAYI)
    print("OTV PAYI:", sonuc / config.otv_oran_hesapla(fiyat))

    return sonuc
