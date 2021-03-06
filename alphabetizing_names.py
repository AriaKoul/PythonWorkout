import operator 


def alphabetize_names(list_of_dictionaries):
    return sorted(list_of_dictionaries, key = operator.itemgetter('last', 'first'))

PEOPLE = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}]

print(alphabetize_names(PEOPLE))
