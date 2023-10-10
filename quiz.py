def nowa_gra():

    odpowiedzi = []
    poprawne_odpowiedzi = 0
    pytanie_numer = 1

    for key in pytania:
        print("-------------------------")
        print(key)
        for i in opcje[pytanie_numer-1]:
            print(i)
        odpowiedz = input("Wpisz (A, B, C, lub D): ")
        odpowiedz = odpowiedz.upper()
        odpowiedzi.append(odpowiedz)

        poprawne_odpowiedzi += sprawdz_odpowiedz(pytania.get(key), odpowiedz)
        pytanie_numer += 1
# -------------------------
    wywietl_punkty(poprawne_odpowiedzi, odpowiedzi)

def sprawdz_odpowiedz(wynik, odpowiedz):

    if wynik == odpowiedz:
        print("Poprawna odpowiedź!")
        return 1
    else:
        print("Źle!")
        return 0

# -------------------------
def wywietl_punkty(poprawne_odpowiedzi, odpowiedzi):
    print("-------------------------")
    print("Wyniki!")
    print("-------------------------")

    print("Odpowiedzi: ", end="")
    for i in pytania:
        print(pytania.get(i), end=" ")
    print()# -------------------------

    print("Twoje odpowiedzi: ", end="")
    for i in odpowiedzi:
        print(i, end=" ")
    print()

    print("Twój wynik to "+str(poprawne_odpowiedzi)+" na 10!")

    if(poprawne_odpowiedzi>=8):
        print("Jesteś mistrzem.")

    elif(poprawne_odpowiedzi>=5):
        print("Całkiem nieźle.")

    else:
        print("Spróbuj jeszcze raz.")

def zagraj_ponownie():

    decyzja = input("Chcesz zagrać jeszcze raz? (tak lub nie): ")
    decyzja = decyzja.upper()

    if decyzja == "TAK":
        return True
    else:
        return False



pytania = {
 "Kto stworzył pythona?: ": "A",
 "W którym roku stworzono pythona?: ": "B",
 "Najwyższy szczyt świata?: ": "C",
 "Czy ziemia jest okrągła?: ": "A",
 "Czy opłacało sie iść do ekonoma?":"D",
 "Jak nazywa się najgłębsze jezioro w Polsce?":"C",
 "Jak nazywa się hymn polski?":"A",
 "Kogo rakiety spadły na ciągnik?":"B",
 "Czy zdam egzamin zawodowy?":"C",
 "Fajny quiz?":"A",

}

opcje = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
        ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
        ["A. Śnieżka", "B. Mont Blanc", "C. Mount Everest", "D. K2"],
        ["A. Tak","B. Nie", "C. Czasami", "D. Co to ziemia?"],
        ["A. Jeszcze jak","B. Raczej nie inaczej","C. Nie wiem","D. Nie"],
        ["A. Śniardwy","B. Twardy Dół", "C. Hańcza", "D. Wisła"],
        ["A. Mazurek Dąbrowskiego","B. Marsz Dąbrowskiego","C. Nie wiem","D. Koko koko euro spoko"],
        ["A. Rosyjskie","B. Nikt nie wie.","C. Ukraińskie","D. Polskie"],
        ["A. Na luzie","B. Może","C. Sam nie wiem","D. Nie"],
        ["A. No spoko","B. Może być", "C. Słaby", "D. Nie wiem"],
         ]

nowa_gra()

while zagraj_ponownie():
    nowa_gra()# -------------------------

print("Dzięki za grę!")

