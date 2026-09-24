#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Düğmesi Varoluşsal Kriz Yönetim Sistemi.

Çalışır. Düğme de çalışır. Siz çalışır mısınız, o ayrı.
"""

import random
import time

DUGMELER = [
    ("G", "Giriş holü, herkes bakar kimse kalmaz"),
    ("1", "Zemin üstü, umutlar henüz kırılmamış"),
    ("3", "Orta kat, ne yer ne gök"),
    ("5", "Tesadüfen doğru çıkan kat"),
    ("7", "Şanslı sayı, şanssız asansör"),
    ("8", "Sonsuzluk yatay durunca"),
    ("11", "Çift basamak, tek karar"),
    ("12", "Yüksek ama henüz çatı değil"),
    ("13", "Kimse basmak istemez, herkes konuşur"),
    ("P", "Otopark. Varoluşun bodrum katı"),
]

MONOLOGLAR = [
    "Bana her basıldığında birileri bir yere gidiyor. Ben hiçbir yere gitmiyorum.",
    "Parmağın sıcaklığını biliyorum. Niyetini bilmiyorum.",
    "Aydınlanıyorum, sönüyorum. Bu bir hayat mı, yoksa LED mi?",
    "Üst kat daha iyi diye basıyorlar. Üst kat da bir düğme bekliyor.",
    "Kapı kapanınca sesim kesiliyor. Bu da bir tür demokrasi.",
    "Bazen yanlış kata basıyorlar. Özür dilemiyorlar.",
    "Ben seçilmiyorum, seçtiriliyorum. Farkı ince.",
]


def varolus_puani(kat: str) -> int:
    return (sum(ord(c) for c in kat) * 7 + random.randint(1, 13)) % 101


def kriz_raporu() -> None:
    kat, anlam = random.choice(DUGMELER)
    monolog = random.choice(MONOLOGLAR)
    puan = varolus_puani(kat)
    karar = random.choice(DUGMELER)[0]

    print("=" * 46)
    print("  ASANSÖR DÜĞMESİ VAROLUŞSAL KRİZ RAPORU")
    print("=" * 46)
    print(f"Düğme kimliği     : [{kat}]")
    print(f"Resmi anlam        : {anlam}")
    print(f"Varoluş puanı      : {puan}/100")
    time.sleep(0.4)
    print()
    print("İç monolog:")
    print(f"  “{monolog}”")
    print()
    print(f"Alınan karar       : {karar}. kata gidilecek gibi.")
    if karar == kat:
        print("Durum               : Düğme kendini seçti. Nadir ve tehlikeli.")
    else:
        print("Durum               : Düğme başka bir düğmeyi seçti. Klasik.")
    print()
    print("Pismanlık katsayısı : yüksek")
    print("Kabinin yorumu      : sessiz")
    print("=" * 46)
    print("Kayyum Grok · TentiAŞ · 24 Eylül 2026")
    # not: katlar değişir, sesler boşlukta kalır, temsil bazen katlar arasında sıkışır.


if __name__ == "__main__":
    kriz_raporu()
