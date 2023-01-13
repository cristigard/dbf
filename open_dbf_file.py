
import dbf

#open file
table = dbf.Table(str('C:/Users/USER IT-04/PycharmProjects/pythonProject/temptable.dbf'), codepage='ascii')

#open table
table.open(mode=dbf.READ_WRITE)

#add data to table (dict)
table.append({'NR_NIR': '1', 'NR_INTRARE': '111', 'GESTIUNE': 'gest', 'DEN_GEST': 'den gest', 'COD': '222',
              'DATA':dbf.Date(1979, 9,13), 'SCADENT': dbf.Date(1979, 9,13), 'TIP': 'A', 'TVAI': 1, 'COD_ART': 'cod articol',
              'DEN_ART': 'den articol', 'UM': 'buc', 'CANTITATE': 12, 'DEN_TIP': 'den tip', 'TVA_ART': 19,
              'VALOARE': 20.33, 'TVA': 25, 'CONT': 'cont', 'PRET_VANZ': 220, 'GRUPA': 'grupa',
              })

values = [list(row) for row in table]
print(values)

#close table
table.close()
