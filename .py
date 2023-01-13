import dbf

#create a new dbf file
#optional -> set dbf type when create a new dbf file(add dbf_type='fp' at dbf.Table())
table = dbf.Table('temptable.dbf', 'NR_NIR C(16); NR_INTRARE C(16); GESTIUNE C(4); DEN_GEST C(36); COD C(8); '
                                    'DATA D; SCADENT D; TIP C(1); TVAI N(1,0); COD_ART C(16); DEN_ART C(60); '
                                    'UM C(5); CANTITATE N(14,3); DEN_TIP C(36); TVA_ART N(2,0); VALOARE N(15,2); '
                                    'TVA N(15,2); CONT C(20); PRET_VANZ N(15,2); GRUPA C(16)')
                                    
#or open an existing file
table = dbf.Table(str('C:/Users/USER IT-04/PycharmProjects/pythonProject/temptable.dbf'), codepage='ascii')

table.open(mode=dbf.READ_WRITE)

table.append({'NR_NIR': '1', 'NR_INTRARE': '111', 'GESTIUNE': 'gest', 'DEN_GEST': 'den gest', 'COD': '222',
              'DATA':dbf.Date(1979, 9,13), 'SCADENT': dbf.Date(1979, 9,13), 'TIP': 'A', 'TVAI': 1, 'COD_ART': 'cod articol',
              'DEN_ART': 'den articol', 'UM': 'buc', 'CANTITATE': 12, 'DEN_TIP': 'den tip', 'TVA_ART': 19,
              'VALOARE': 20.33, 'TVA': 25, 'CONT': 'cont', 'PRET_VANZ': 220, 'GRUPA': 'grupa',
              })

print(table)
