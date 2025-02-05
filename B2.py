"""******************************
Pāvels Petrovs, pp23055
B2. Dots naturāls skaitlis n < 1000. Izdrukāt doto skaitli romiešu pierakstā.
Programma izveidota: 01.10.2023
******************************"""

def NormalToRoman(n): #Definēta funkcija 'NormalToRoman', kas kā argumentu pieņem veselu skaitli 'n' un atgriež virkni.
    a = "" #Inicializē tukšu virknes mainīgo 'a', kurā tiks saglabāts romiešu ciparu atveidojums.
    Normal_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    Roman_numbers = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    for i in range(13): #Ar šo rindu tiek sākta 'for' cikls. Cikls turpinās 13 reizes.
        while n >= Normal_numbers[i]: #Šīs cikls darbojas tik ilgi, kamēr ieejas skaitļa 'n' vērtība ir lielāka vai vienāda ar kārtējo elementu masīvā 'Normal_numbers'. Tā nodrošina ieejas skaitļa konvertēšanu uz tā attēlojumu ar romiešu cipariem.
            a += Roman_numbers[i] #Atbilstošais romiešu ciparu atveidojums tiek pievienots virknei 'a'.
            n -= Normal_numbers[i] #Šis atņemšanas solis ir izšķirošs, lai atrastu atlikušo skaitļa daļu, kas jāpārvērš romiešu ciparos.
        
    return a

while True:
    n = int(input("Ievadiet naturālu skaitļu n: "))
    if (n <= 0): #Pārbaude, vai 'n' ir naturāls skaitlis.
        print("N nav naturals skaitlis")
        print()
        continue #Ja 'n' nav naturāls skaitlis, tad programma atkal prasa ievadīt naturālu skaitļu 'n'.
    elif (n > 1000): #Pārbaude, vai 'n' nav lielāks nekā 1000.
        print("N ir lielāks nekā 1000")
        print()
        continue #Ja 'n' ir lielāks nekā 1000, tad programma atkal prasa ievadīt naturālu skaitļu 'n'.


    a = NormalToRoman(n) #Tiek izsaukta funkcija 'NormalToRoman', un tās atgrieztā vērtība tiek piešķirta mainīgajam 'a'.
    print("Romiešu pieraksts:", a)

    ok = int(input("Vai turpināt (1) vai beigt (0)?\n",))
    print()
    if ok != 1: #Pārbauda, ​​vai vērtība 'ok' nav vienāda ar 1. 
                #Ja tā, programma beidzas. Ja 'ok' ir vienāds ar 1 programma atkārtojas no sākuma, liekot lietotājam ievadīt jaunu vērtību 'n'.
        break

    