# Functions [check PDF description - examples / suggestions included]
# - get the raw data
# - function that prepares the dataset
# - function to retrieve data for each year
# - function to retrieve data for each country
# - function to perform average from an iterable (of year data or country data)
import pycountry


def get_raw_data():
    description_raw = ('Country', [
        '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
        '2019 '])
    data_raw = [
        ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
        ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
        ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
        ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
        ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
        ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
        ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
        ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
        ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
        ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
        ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
        ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
        ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
        ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
        ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
        ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
        ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
        ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
        ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
        ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
        ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
        ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
        ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
        ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
        ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
        ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
        ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
        ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
        ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
        ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
        ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
        ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
        ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
        ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
        ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
        ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
        ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
        ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
        ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
    ]
    return description_raw, data_raw


def convert_country_code_to_name(countries_list):
    # print(f'---->List of countries: {countries_list}')  # for testing purposes
    list_of_country_names_converted = []
    for country_code in countries_list:
        one_country_code = pycountry.countries.get(alpha_2=country_code)
        if one_country_code is None:
            # print(country_code) # for testing purposes
            list_of_country_names_converted.append(country_code)
        else:
            # print(one_country_code.alpha_2) # for testing purposes
            # print(one_country_code.name) # for testing purposes
            list_of_country_names_converted.append(one_country_code.name)
    return list_of_country_names_converted


def transform_list_of_tuples(list_of_tuples):
    list_of_lists = []
    for one_country in list_of_tuples:
        country_new = list(one_country)
        list_of_lists.append(country_new)
    return list_of_lists


def separate_country_from_list(data_as_list):
    countries = []
    data_per_country = []
    for each_country in data_as_list:
        country = each_country.pop(0)
        countries.append(country)
        data_per_country.append(each_country[0])
    print(f'----> {countries}')
    print(f'----> {data_per_country}')
    return countries, data_per_country


def prepare_dataset(description, raw_data):
    pass

    # return processed_data


if __name__ == '__main__':
    description, raw_data = get_raw_data()
    description_as_list = list(description)
    print(f'Description as a list: {description_as_list}')

    raw_data_as_list = transform_list_of_tuples(raw_data)
    print(f'Raw data as list: {raw_data_as_list}')

    # remove 'Country' string
    description_as_list.pop(0)
    # remove the outer list of a double list
    years_as_list = description_as_list[0]
    list_of_countries, list_of_data_per_country = separate_country_from_list(raw_data_as_list)

    print(f'list of years: {years_as_list}')
    print(f'List of countries:{list_of_countries}')
    print(f'List of data per country: {list_of_data_per_country}')

    list_of_country_names = convert_country_code_to_name(list_of_countries)
    print(f'List of the countries with name: {list_of_country_names}')

    description_as_list.append(list_of_data_per_country)
    # years_processed.append(years_as_list)
    print(f'!!!!!!!List of years and data {description_as_list}')

    new_dict_data = dict()
    for country_data in raw_data:
        new_dict_data = {
            country_data[0], [
                {"year": year,
                 "coverage": coverage
                 for (year,coverage) in map(None, description[1],country_data[1])}
            ]
        }

