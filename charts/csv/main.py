import read_csv as rc
import charts as c
import modulos as ms

def main():
  #path = './csv/data.csv'
  #Country = str(input('Escriba el pais a filtrar: ')).capitalize()
  #data = rc.read_csv(path)
  
  #filtered_data = ms.get_country(Country, path)
  #labels, values = ms.get_age_population(filtered_data)
  labels, values = ms.get_column(ms.data())
  c.pie_plot(labels,values) 

if __name__ == '__main__':
  main()