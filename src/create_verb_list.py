import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy

data_file = 'data\\verbs.csv'


def get_verbo():                #get verb paradigm

    inf = input('\n\nInfinitive:')
    past = input('\nPast form:')
    part = input('\nPast participle:')
    ita = input('\nItalian:')
    print('\n\n')
    return ( inf, past, part, ita )

lista_verbi = pd.DataFrame( columns=['infinitive', 'past', 'past participle', 'italiano'] )

print("Add the verbs. Press ctrl+c to exit and save")


try:

    while True:

        verbo_nuovo = get_verbo()
        print( verbo_nuovo )
 
        lista_verbi.loc[len( lista_verbi )] = verbo_nuovo


except KeyboardInterrupt:

    print('\n\n\nSaving to file')
    
    lista_verbi.to_csv( data_file )


print( lista_verbi )
