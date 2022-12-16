import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      #Metodo 1
      country_dict = dict(zip(header, row))
      '''
      Se puede crear un diccionario con el comando # dict(resultado del zip) o mediante el metodo: {key: value for key, value in iterable}

      Metodo 2:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      '''
      data.append(country_dict)
    return data
      
if __name__ == "__main__":
  data = read_csv('./data.csv')
  print(data)