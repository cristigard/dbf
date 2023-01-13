import dbf

#open file
table = dbf.Table(str('C:/Users/USER IT-04/PycharmProjects/pythonProject/temptable.dbf'), codepage='ascii')

#open table
table.open(mode=dbf.READ_WRITE)

#add new column to table
table.add_fields('TELEPHONE C(10)')

#add data to new format table
table.append({'NR_NIR': '1', 'NR_INTRARE': '111', 'GESTIUNE': 'gest', 'DEN_GEST': 'den gest', 'COD': '222',
              'DATA':dbf.Date(1979, 9,13), 'SCADENT': dbf.Date(1979, 9,13), 'TIP': 'A', 'TVAI': 1, 'COD_ART': 'cod articol',
              'DEN_ART': 'den articol', 'UM': 'buc', 'CANTITATE': 12, 'DEN_TIP': 'den tip', 'TVA_ART': 19,
              'VALOARE': 20.33, 'TVA': 25, 'CONT': 'cont', 'PRET_VANZ': 220, 'GRUPA': 'grupa', 'TELEPHONE': '123456789'
              })

table.close()





