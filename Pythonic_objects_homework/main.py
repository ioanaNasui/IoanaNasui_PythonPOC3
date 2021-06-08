# Build two classes of your choice that can model a real-life example. The class needs to meet the following req:
# • at least 5 attributes each
# • at least 2 methods each
# • one class to inherit from another
# As a demonstration create at least 5 instances of one class (preferably the child class)
# and call all the methods it holds
# Ex: You can have one class (Country) that has general attributes about countries such as area,
# neighbors, cities etc.. and methods related to those attributes. The second class can be a specific country (Romania)
# that has more specific attributes such as attractions, universities etc.
# - use instance and class attributes
# - create at least one class method and static method
# - don't forget to implement __str__ and __repr__ (illustrating the differences between them)
# - do a validation with exception in __init__ if any of the attributes is not valid

if __name__ == '__main__':
    class Country(object):
        def __init__(self, country_name, area, population, climate, ue_member=None, cities=None):
            if type(country_name) is str:
                self.country_name = country_name
            else:
                raise Exception("Sorry, the country name must be a string")
            if (type(area) is int or type(area) is float) and area > 0:
                self.area = area
            else:
                raise Exception("Sorry, the country area must be a int or float and bigger than 0")
            if type(population) is int and population > 0:
                self.population = population
            else:
                raise Exception("Sorry, the country population must be a int and bigger than 0")
            if cities is not None:
                self.cities = list(cities)
            if type(climate) is str:
                self.climate = climate
            else:
                raise Exception("Sorry, the country climate must be a string")
            self.ue_member = 'Yes' if ue_member else 'No'

        def __iter__(self):
            return iter(self.cities)

        def __getitem__(self, index):
            return self.cities[index]

        def __repr__(self):
            class_name = type(self).__name__
            return f'Country: {self.country_name} with id: {id(self)}. Type: {class_name}'

        def density(self):
            return self.population / self.area

        def no_of_cities(self):
            return len(self.cities)


    class Romania(Country):  # Country is Romania, climate is temperate continental and is member of EU

        def __init__(self, area, population, attractions, universities, cities):
            self.attractions = list(attractions)
            self.universities = list(universities)
            super().__init__('Romania', area, population, 'temperate continental', 'Yes', cities)

        def __iter__(self):
            return iter(self.attractions)

        def __getitem__(self, index):
            return self.attractions[index]

        def __iter__(self):
            return iter(self.universities)

        def __getitem__(self, index):
            return self.universities[index]

        def __str__(self):
            if self.ue_member == 'Yes':
                is_ue_member = 'is an UE member'
            else:
                self.is_ue_member = 'is not an UE member'
            return f'{self.country_name} has an area of {self.area}, a population of {self.population}, a {self.climate} climate and {is_ue_member} '

        # def __str__(self):
        #    super().__str__(self)

        @staticmethod
        def density_fact(density):
            if density < 1500:
                return print('Monaco has a larger population density')
            else:
                return print('Monaco has smaller population density')

        def no_of_attractions(self):
            return len(self.attractions)

        def has_technical_university(self):
            for university in self.universities:
                if 'ehnica' in university:
                    return print('There is at least 1 technical university')
                else:
                    return print('There is no technical university')

list_of_attractions_North_West = ['Botanical Garden', "St. Michael's church", 'Village Museum', 'Art Museum',
                                  'Pharmacy Museum']
list_of_universities_North_West = ['Universitatea Tehnica din Cluj-Napoca', 'Babes-Bolyai', 'UMF', 'USAMV', 'UAD',
                                   'Academia de muzica']
list_of_cities_North_West = ['Cluj-Napoca', 'Zalau', 'Bistrita-Nasaud', 'Satu Mare']

list_of_attractions_North_East = ['Palatul culturii', 'Centru', 'Bojdeuca Ion Creanga']
list_of_universities_North_East = ['Universitatea Tehnica "Gheorghe Asachi"', 'Universitatea „Alexandru Ioan Cuza”',
                                   'Universitatea de Arte „George Enescu”', 'Facultatea de Teologie Ortodoxa', 'UMF',
                                   'USAMV']
list_of_cities_North_East = ['Iasi', 'Botosani', 'Suceava', 'Piatra Neamt', 'Targu-Neamt', 'Bacau']

list_of_attractions_West = ['Piata Unirii', 'Piata Victoriei', 'Castelul Huniade', 'Bastionul Maria Theresia',
                            'Parcul Rozelor', 'Cramele Recas']
list_of_universities_West = ['Universitatea Politehnica din Timisoara', 'Universitatea de vest din Timisoara', 'UMF',
                             'Universitatea de Stiinte Agricole si Medicină Veterinara']
list_of_cities_West = ['Arad', 'Timisoara', 'Oradea', 'Lugoj']

list_of_attractions_East = ['Mamaia', 'Cazino Constanta', 'Delfinariu Constanta', 'Centrul vechi']
list_of_universities_East = ['Academia Navala Mircea cel Batran', 'Universitatea Maritima Constanta',
                             'Universitatea Ovidius']
list_of_cities_East = ['Constanta', 'Braila', 'Galati', 'Buzau', 'Tulcea']

list_of_attractions_South = ['The old Town', 'Palace of the Parliament', 'Romanian Athenaeum']
list_of_universities_South = ['Universitatea politehnica Bucuresti', 'University of Bucharest']
list_of_cities_South = ['Bucuresti', 'Pitesti', 'Ploiesti', 'Craiova']

object_Romania_North_West = Romania(5555.2, 1111111, list_of_attractions_North_West, list_of_universities_North_West,
                                    list_of_cities_North_West)
object_Romania_North_East = Romania(4444.3, 2222222, list_of_attractions_North_East, list_of_universities_North_East,
                                    list_of_cities_North_East)
object_Romania_West = Romania(3333.4, 3333333, list_of_attractions_West, list_of_universities_West, list_of_cities_West)
object_Romania_East = Romania(2222.5, 4444444, list_of_attractions_East, list_of_universities_East, list_of_cities_East)
object_Romania_South = Romania(1111.6, 5555555, list_of_attractions_South, list_of_universities_South,
                               list_of_cities_South)

print(f'Country name is: {object_Romania_North_West.country_name}')
print(f'Climate is: {object_Romania_North_West.climate}')
print(f'Is {object_Romania_North_West.country_name} a EU member?: {object_Romania_North_West.ue_member}')
print(f'__str__ method:  {str(object_Romania_North_West)}')
print(f'__repr__ method: {repr(object_Romania_North_West)}')
print(f'__repr__ method: {repr(object_Romania_North_East)}')
print(f'Class method from parent: {object_Romania_North_West.density()}')
print(f'Class method from parent: {object_Romania_North_East.density()}')
density1 = object_Romania_North_West.density()
print(f'Static method from child: {object_Romania_North_West.density_fact(density1)}')
print(f'Class method from parent: {object_Romania_North_West.no_of_cities()}')
print(f'Class method from child: {object_Romania_North_West.no_of_attractions()}')
print(object_Romania_North_West.country_name)
print(object_Romania_North_West.has_technical_university())
print(object_Romania_East.has_technical_university())

# example to throw exception:
object_Romania_throws_exception = Romania(5555.6, 555555.3, list_of_attractions_South, list_of_universities_South,
                                list_of_cities_South)

# am 2 intrebari:
# 1: nu reusesc sa imi dau seama de ce imi printeaza si "None" din metoda "has_technical_university()"
# 2: daca pun metoda __str__ in parent class am eroare: takes 1 positional argument but 2 were given
