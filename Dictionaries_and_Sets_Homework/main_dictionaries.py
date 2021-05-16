def separation_based_on_sex(list_of_data):
    # this function separates the single list into two separate lists based on sex
    list_of_data_females = []
    list_of_data_males = []
    for data in list_of_data:
        if 'Female' in data:
            list_of_data_females.append(data)
        else:
            list_of_data_males.append(data)
    return list_of_data_females, list_of_data_males


def replace_substring(list_of_data, existing_substring, future_substring):
    # this function replaces one substring  with a new one (in this case, 'Female'/'Male' is replaced with 'F'/'M')
    new_list_of_data = []
    for data in list_of_data:
        new_list_of_data.append(data.replace(existing_substring, future_substring))
    return new_list_of_data


def split_each_element(list_of_data):
    # this function splits an entire string in multiple elements in a list based on "space" char
    new_list_of_data = []
    for data in list_of_data:
        new_list_of_data.append(data.split())
    return new_list_of_data


def reorder_elements(list_of_data):
    # this function sets the correct order of elements in the list
    new_list_of_data = []
    for data in list_of_data:
        data.insert(2, int(data[0]))
        data.pop(0)
        if data[3] != ':':
            data[3] = float(data[3])
        new_list_of_data.append(data)
    return new_list_of_data


def list_data_based_on_year(list_of_data, year_needed):
    health_index_by_year = {
        country: [sex, health_index]  # key:value
        for (country, year, sex, health_index) in list_of_data
        if year == year_needed  # condition
    }
    return health_index_by_year


def group_data_by_year_for_country(list_of_data, country):
    one_country = {
        year: [sex, health_index]
        for (country, year, sex, health_index) in list_of_data
        if country == 'Germany'
    }
    return one_country


def concatenated_key(list_of_tuples):
    list_of_list = []
    for data in list_of_tuples:
        list_of_list.append(list(data))
    # print(list_of_list)

    for data in list_of_list:
        data[0] = data[0] + '_' + str(data[1])  # concatenate element
    # print(list_of_list)

    list_of_tuples_new = []
    for data in list_of_list:
        list_of_tuples_new.append(tuple(data))
    # print(list_of_tuples_new)

    health_index_country_key = {
        country_year: [year, sex, health_index]
        for (country_year, year, sex, health_index) in list_of_tuples_new
    }
    return health_index_country_key


def select_data_based_on_index_and_sex(dict_of_data, health_index, sex=None):
    sex_to_remove = 'None'
    if sex == 'F':
        sex_to_remove = 'M'
    elif sex == 'M':
        sex_to_remove = 'F'
    for country in dict_of_data.copy():
        if dict_of_data[country][2] != ':' and dict_of_data[country][2] < health_index or dict_of_data[country][
            1] == sex_to_remove:
            # print(dict_of_data[country][2])  # for testing purposes
            dict_of_data.pop(country)
    return dict_of_data


def remove_year(dict_of_data, year):
    for country in dict_of_data.copy():
        if dict_of_data[country][0] == year:
            dict_of_data.pop(country)
    return dict_of_data


if __name__ == '__main__':
    self_perceived_health_total = ["2017 Belgium Males 33.4", "2017 Bulgaria Males 51", "2017 Czechia Males 24.3",
                                   "2017 Denmark Males 21.1", "2017 Germany Males 19.8", "2017 Estonia Males 4.8",
                                   "2017 Ireland Males 44", "2017 Greece Males 55", "2017 Spain Males 23.1",
                                   "2017 France Males 20.6", "2017 Croatia Males 22.4", "2017 Italy Males 21.1",
                                   "2017 Cyprus Males 56.4", "2017 Latvia Males 1", "2017 Lithuania Males 6.6",
                                   "2017 Luxembourg Males 26", "2017 Hungary Males 20.3", "2017 Malta Males 41.2",
                                   "2017 Netherlands Males 24.9", "2017 Austria Males 29.7", "2017 Poland Males 23",
                                   "2017 Portugal Males 15.7", "2017 Romania Males :", "2017 Slovenia Males 21.2",
                                   "2017 Slovakia Males 22.3", "2017 Finland Males 27.6", "2017 Sweden Males 32.7",
                                   "2017 Iceland Males 41.7", "2017 Norway Males 32.3", "2017 Switzerland Males 36",
                                   "2017 UnitedKingdom Males 38.4", "2017 Montenegro Males 28.2",
                                   "2017 NorthMacedonia Males 17.9", "2017 Serbia Males 15.6", "2017 Turkey Males 8",
                                   "2017 Kosovo Males :", "2018 Belgium Males 28.9", "2018 Bulgaria Males 36.6",
                                   "2018 Czechia Males 25.1", "2018 Denmark Males 27.2", "2018 Germany Males 19",
                                   "2018 Estonia Males 4.5", "2018 Ireland Males 49.8", "2018 Greece Males 54.3",
                                   "2018 Spain Males 28.1", "2018 France Males 20.9", "2018 Croatia Males 23",
                                   "2018 Italy Males 22", "2018 Cyprus Males 56", "2018 Latvia Males 1.2",
                                   "2018 Lithuania Males 6.4", "2018 Luxembourg Males 23.7", "2018 Hungary Males 12.6",
                                   "2018 Malta Males 30.5", "2018 Netherlands Males 22.4", "2018 Austria Males 31.6",
                                   "2018 Poland Males 12", "2018 Portugal Males 15.3", "2018 Romania Males :",
                                   "2018 Slovenia Males 25.6", "2018 Slovakia Males 17.2", "2018 Finland Males 26.8",
                                   "2018 Sweden Males 36.9", "2018 Iceland Males 34.7", "2018 Norway Males 25.2",
                                   "2018 Switzerland Males 35.7", "2018 UnitedKingdom Males 36.1",
                                   "2018 Montenegro Males 27.1", "2018 NorthMacedonia Males 17.3",
                                   "2018 Serbia Males 16.5", "2018 Turkey Males 5.6", "2018 Kosovo Males 39.6",
                                   "2017 Belgium Females 26.4", "2017 Bulgaria Females 6.1",
                                   "2017 Czechia Females 17.1", "2017 Denmark Females 29.2",
                                   "2017 Germany Females 17.4", "2017 Estonia Females 4.3", "2017 Ireland Females 44.7",
                                   "2017 Greece Females 52.3", "2017 Spain Females 20.8", "2017 France Females 18.3",
                                   "2017 Croatia Females 16.3", "2017 Italy Females 17.9", "2017 Cyprus Females 55.2",
                                   "2017 Latvia Females 1.1", "2017 Lithuania Females 0.4",
                                   "2017 Luxembourg Females 22.2", "2017 Hungary Females 8.9",
                                   "2017 Malta Females 39.4", "2017 Netherlands Females 16",
                                   "2017 Austria Females 27.7", "2017 Poland Females 3.3", "2017 Portugal Females 13",
                                   "2017 Romania Females :", "2017 Slovenia Females 17.5", "2017 Slovakia Females 12.2",
                                   "2017 Finland Females 23.8", "2017 Sweden Females 27.6", "2017 Iceland Females 31.9",
                                   "2017 Norway Females 27.1", "2017 Switzerland Females 29.8",
                                   "2017 UnitedKingdom Females 32.6", "2017 Montenegro Females 26.8",
                                   "2017 NorthMacedonia Females 7.9", "2017 Serbia Females 7.9",
                                   "2017 Turkey Females 4.9", "2017 Kosovo Females :", "2018 Belgium Females 25.3",
                                   "2018 Bulgaria Females 10", "2018 Czechia Females 19.9", "2018 Denmark Females 29.6",
                                   "2018 Germany Females 18.5", "2018 Estonia Females 1.1", "2018 Ireland Females 48.6",
                                   "2018 Greece Females 50.3", "2018 Spain Females 24.9", "2018 France Females 17",
                                   "2018 Croatia Females 16.1", "2018 Italy Females 20.2", "2018 Cyprus Females 52.8",
                                   "2018 Latvia Females 1.5", "2018 Lithuania Females 1.5",
                                   "2018 Luxembourg Females 24.2", "2018 Hungary Females 14.5",
                                   "2018 Malta Females 29.6", "2018 Netherlands Females 16.9",
                                   "2018 Austria Females 27.3", "2018 Poland Females 13.1",
                                   "2018 Portugal Females 11.8", "2018 Romania Females :", "2018 Slovenia Females 12.7",
                                   "2018 Slovakia Females 10.1", "2018 Finland Females 20", "2018 Sweden Females 26",
                                   "2018 Iceland Females 36.3", "2018 Norway Females 25.1",
                                   "2018 Switzerland Females 31.7", "2018 UnitedKingdom Females 31.9",
                                   "2018 Montenegro Females 22.5", "2018 NorthMacedonia Females 11.6",
                                   "2018 Serbia Females 11.5", "2018 Turkey Females 5.8", "2018 Kosovo Females 41.6"]
    self_perceived_health_females, self_perceived_health_males = separation_based_on_sex(self_perceived_health_total)
    print(
        f'Length of list of data only with female is: {len(self_perceived_health_females)} and its contains are: {self_perceived_health_females}')
    print(
        f'Length of list of data only with male is: {len(self_perceived_health_males)} and its contains are: {self_perceived_health_males}')
    self_perceived_health_females = replace_substring(self_perceived_health_females, 'Females', 'F')
    self_perceived_health_males = replace_substring(self_perceived_health_males, 'Males', 'M')
    print(
        f'Length of list of data only with "F" is: {len(self_perceived_health_females)} and its contains are: {self_perceived_health_females}')
    print(
        f'Length of list of data only with "M" is: {len(self_perceived_health_males)} and its contains are: {self_perceived_health_males}')
    self_perceived_health_females = split_each_element(self_perceived_health_females)
    self_perceived_health_males = split_each_element(self_perceived_health_males)
    print(
        f'After split: -> Length of list of data only with "F" is: {len(self_perceived_health_females)} and its '
        f'contains are: {self_perceived_health_females}')
    print(
        f'After split: -> Length of list of data only with "M" is: {len(self_perceived_health_males)} and its '
        f'contains are: {self_perceived_health_males}')
    self_perceived_health_females = reorder_elements(self_perceived_health_females)
    print(f'Reordered list: {self_perceived_health_females}')
    self_perceived_health_males = reorder_elements(self_perceived_health_males)
    print(f'Reordered list: {self_perceived_health_males}')
    print('------------------->The dataset will have the following structure:[(‘France’, 2017, M, 12), …]')
    self_perceived_health_females_tuples = [tuple(data) for data in self_perceived_health_females]
    self_perceived_health_males_tuples = [tuple(data) for data in self_perceived_health_males]
    print(f'structure:[(‘France’, 2017, F, 12), …] for females: {self_perceived_health_females_tuples}')
    print(f'structure:[(‘France’, 2017, M, 12), …] for males: {self_perceived_health_males_tuples}')
    print('-------------------> two dicts for each Females and Males, that group all data by country for each year > '
          'health_index_2017 = { '
          '‘France’: [sex, health_index]} > health_index_2018 = {‘France’: [sex, health_index]}')
    health_index_2017_females = list_data_based_on_year(self_perceived_health_females_tuples, 2017)
    print(
        f'Length is: {len(health_index_2017_females)} and the dict for year 2017 and Females is: {health_index_2017_females}')
    health_index_2018_females = list_data_based_on_year(self_perceived_health_females_tuples, 2018)
    print(
        f'Length is: {len(health_index_2018_females)} and the dict for year 2018 and Females is: {health_index_2018_females}')
    health_index_2017_males = list_data_based_on_year(self_perceived_health_males_tuples, 2017)
    print(
        f'Length is: {len(health_index_2017_males)} and the dict for year 2017 and Males is: {health_index_2017_males}')
    health_index_2018_males = list_data_based_on_year(self_perceived_health_males_tuples, 2018)
    print(
        f'Length is: {len(health_index_2018_males)} and the dict for year 2018 and Males is: {health_index_2018_males}')
    print(
        '-------------------> one dict that groups all data by year for Germany > germany = {2017: [sex, health_index]}')
    germany = group_data_by_year_for_country(self_perceived_health_females_tuples, 'Germany')
    print(f'all data by year for Germany for Females: {germany}')
    print('-------------------> one dict that groups all data by country and year, by using year in the key together '
          'with the country name > health_index = {‘France_2017’: [year, sex, health_index]}')
    health_index_males = concatenated_key(self_perceived_health_males_tuples)
    health_index_females = concatenated_key(self_perceived_health_females_tuples)
    print(f'Grouping data, by concatenated key "Males": {health_index_males}')
    print(f'Grouping data, by concatenated key "Females": {health_index_females}')
    print('-------------------> starting from the previous health_index dict, display only the data where the '
          'health_index > 5')
    dictionary_with_bigger_health_index = select_data_based_on_index_and_sex(health_index_females, 5)
    print(
        f'Health index for females bigger than 5 has size {len(dictionary_with_bigger_health_index)} and contents: {dictionary_with_bigger_health_index}')
    print('-------------------> starting from the previous health_index dict, display only the data where the '
          'health_index > 5 and sex is ‘F’')
    # In order to solve this, a dictionary with both females and males is needed.
    # Since country_year key will have duplicate, due to 2 sets of data ("Females" and "Males"),
    # a dict health_index_total_different_years will be created, containing data as follows:
    # {'Belgium_2017': [2017, 'M', 33.4], 'Belgium_2018': [2018, 'F', 25.3], etc}
    health_index_males_2017 = remove_year(health_index_males, 2018)
    health_index_females_2018 = remove_year(health_index_females, 2017)
    print(
        f'Health index for males for year 2017 has size {len(health_index_males_2017)} and contents: {health_index_males_2017}')
    print(
        f'Health index for females for year 2018 has size {len(health_index_females_2018)} and contents: {health_index_females_2018}')
    health_index_total_different_years = dict(health_index_females_2018)
    health_index_total_different_years.update(health_index_males_2017)
    # print(health_index_total_different_years)  # for testing purposes
    dictionary_with_bigger_health_index_and_females = select_data_based_on_index_and_sex(
        health_index_total_different_years, 6, 'F')  # 5 is too small
    print(
        f'data where the health_index > 6 and sex is ‘F’ has size {len(dictionary_with_bigger_health_index_and_females)} and contents: {dictionary_with_bigger_health_index_and_females}')
