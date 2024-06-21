import csv

def read_csv(path):
  with open(path, 'r') as readcsv:
    reader = csv.reader(readcsv, delimiter= ',')
    header =  next(reader)
    data = []
    for row in reader:
      dict_data = zip(header,row)
      country_dict = {key:value for key,value in dict_data}
      data.append(country_dict)
      
  return data   

if __name__ == '__main__':
  print(read_csv('/home/joseph/home/Documentos/Programación/Entornos_PIP/charts/csv/data.csv'))


