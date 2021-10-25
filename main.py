prop, cnt_c, cnt_p, poz, conectori, ok = input(), 0, 0, 0, ['∧', '∨', '⇒', '¬', '⇔'], True


for i in prop:
    if (i in conectori or i == ')') and poz == 0:
        print("Conectorii sau paranteza inchisa nu poate sa apara pe prima pozitie. Nu, expresia nu este o propozitie bine definita")
        exit()

    if i in conectori and (i != '¬' and poz < 2):
        print("Un conector binar apare cel mai devreme pe pozitia 3. Nu, expresia nu este o propozitie bine definita")
        exit()

    elif i in conectori:
        cnt_c += 1

    if i == '(' or i == ')':
        if i == ')' and poz == 0:
            print("O propozitie bine definita nu poate sa inceapa cu o paranteza care se inchide. Nu, expresia nu este o propozitie bine definita")
            exit()
        else:
            cnt_p += 1
    poz += 1


if 2*cnt_c - cnt_p == 0:
    for i in range(len(prop)):
        if prop[i] == '(':
            if prop[i + 1] == '(' or (prop[i + 1] == '¬' or 'A' <= prop[i + 1] <= 'Z'):
                continue
            else:
                ok = False
                print("Pe pozitia", i, "se afla o paranteza, iar pe pozitia urmatoare se astepta o negatie, o paranteza deschisa sau o propozitie atomica. Nu, expresia nu este o propozitie bine definita")
                break

        if prop[i] == '¬':
            if 'A' <= prop[i + 1] <= 'Z' or prop[i + 1] == '(':
                continue
            else:
                ok = False
                print("Pe pozitia", i, "se afla o negatie iar pe pozitia urmatoare se asteapta o propozitie atomica sau o paranteza deschisa. Nu, expresia nu este o propozitie bine definita")
                break

        if 'A' <= prop[i] <= 'Z' and (prop[i - 1] != '∧' and prop[i - 1] != '∨' and prop[i - 1] != '⇒' and prop[i - 1] != '¬' and prop[i - 1] != '⇔'):
            if prop[i + 1] in conectori:
                continue
            else:
                ok = False
                print("Pe pozitia", i, "se afla o propozitie atomica, iar pe urmatoarea pozitie se asteapta obligatoriu un conector. Nu, expresia nu este o propozitie bine definita")
                break

        if 'A' <= prop[i] <= 'Z' and prop[i - 1] is conectori:
            if prop[i + 1] == ')':
                continue
            else:
                ok = False
                print("Pe pozitia", i, "se afla o propozitie atomica ce este precedata de un conector, iar pe urmatoarea pozitie se asteapta obligatoriu o paranteza. Nu, expresia nu este o propozitie bine definita")
                break

        if prop[i] in conectori:
            if prop[i + 1] == '(' or 'A' <= prop[i + 1] <= 'Z':
                continue
            else:
                ok = False
                print("Pe pozitia", i, "se afla un conector, iar pe urmatoarea pozitie se asteapta fie o paranteza deschisa, fie o propozitie atomica. Nu, expresia nu este o propozitie bine definita")
                break

else:
    if (cnt_p - 2 * cnt_c) % 2 == 0 and cnt_p - 2*cnt_c > 0:
        print("Se pot elimina", cnt_p - 2*cnt_c, "paranteze din captele expresiei si aceasta isi pastreaza sensul. Da, expresia este o propozitie bine definita")
        exit()
    else:
        print("Numarul de paranteze nu corespunde cu numarul de conectori, acesta trebuie sa fie cel putin '2*numarul de conectori'. Nu, expresia nu este o propozitie bine definita")
        print("Sunt", cnt_c, "conectori si", cnt_p, "paranteze")
        exit()

if ok:
    print("Da, expresia este o propozitie bine definita")