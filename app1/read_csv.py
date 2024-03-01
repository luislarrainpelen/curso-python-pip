
import csv
'''
## 1 Asteriscos y filas en formato lista
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      print('***' * 5)
      print(row)


## 2 Solo header o primera fila
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    print(header)


## 3 Union de header y row produce TUPLAS pares Rank: 74
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
      iterable = zip(header, row)
      print('***' * 5)
      print(list(iterable))


## 4 Con dictionary comprehension, retorna varios diccionarios
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      print(country_dict)

'''

## 5 Retornar una lista con todos los diccionarios
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data


if __name__ == '__main__':
  read_csv('data.csv')

data = read_csv('data.csv')	


