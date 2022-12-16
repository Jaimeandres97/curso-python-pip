import utils
import read_csv as read
import charts

def run():
  data = read.read_csv('./data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  country_perc = utils.population_percentage(data)
  country, percentage = country_perc
  charts.generate_pie_chart(country, percentage)
  
  #Solucion graficar poblacion de un pais
  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(keys, values, country['Country/Territory'])

  #Clase sobre modulos
  '''
  def run():
    keys,values = utils.get_population()
    print(keys,values) 
    
    country = input('Type Country => ')
    
    result = utils.population_by_country(data, country)
    print(result)
  '''

if __name__ == '__main__': 
  run()