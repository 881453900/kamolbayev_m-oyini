import random

QIZIL = "\033[31m"
YASHIL = "\033[32m"
SARIQ = "\033[33m"
KO_K = "\033[34m"
TOZALASH = "\033[0m"

def oyin():
    print(f"\n{KO_K}==============================={TOZALASH}")
    print(f"{KO_K}      KAMOLBAYEV_M O'YINI      {TOZALASH}")
    print(f"{KO_K}==============================={TOZALASH}")
    
    try:
        maksimal_son = int(input("Sonlar chegarasini kiriting (masalan, 100): "))
        imkoniyat = int(input("Nechta urinish berilsin? (masalan, 7): "))
    except ValueError:
        print(f"{QIZIL}Iltimos, faqat butun son kiriting!{TOZALASH}")
        return

    yashirin_son = random.randint(1, maksimal_son)
    urinish = 0
    print(f"\n{SARIQ}1 dan {maksimal_son} gacha son o'yladim. {imkoniyat} ta imkoniyatingiz bor!{TOZALASH}")

    while urinish < imkoniyat:
        print(f"\nSizda {SARIQ}{imkoniyat - urinish}{TOZALASH} ta imkoniyat qoldi.")
        try:
            taxmin = int(input("Soningizni kiriting: "))
        except ValueError:
            print(f"{QIZIL}Iltimos, faqat butun son kiriting!{TOZALASH}")
            continue
        urinish += 1

        if taxmin < yashirin_son:
            print(f"{QIZIL}Kattaroq son kiriting! ⬆️{TOZALASH}")
        elif taxmin > yashirin_son:
            print(f"{QIZIL}Kichikroq son kiriting! ⬇️{TOZALASH}")
        else:
            print(f"\n{YASHIL}🎉 Tabriklayman! {urinish} ta urinishda topdingiz! 🏆{TOZALASH}\n")
            return

    print(f"\n{QIZIL}😢 Yutqazdingiz! Men o'ylagan son {yashirin_son} edi.{TOZALASH}\n")

oyin()
