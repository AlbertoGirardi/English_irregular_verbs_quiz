import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy

data_file = 'data\\verbs.csv'


def get_verbo():                #get verb paradigm

    inf = input('\n\nInfinitive:').rstrip()
    past = input('\nPast form:').rstrip()
    part = input('\nPast participle:').rstrip()
    ita = input('\nItalian:').rstrip()
    print('\n\n')
    return ( inf, past, part, ita )


try: 
    lista_verbi = pd.read_csv( data_file, header = 0, index_col=0 )
    print( lista_verbi )


except FileNotFoundError:

    lista_verbi = pd.DataFrame( columns=['infinitive', 'past', 'past participle', 'italiano'] )

print("Add the verbs. Press ctrl+c to exit and save")


try:

    while True:

        verbo_nuovo = get_verbo()
        print( verbo_nuovo )

        if input('Correct?ENTER for yes\t') == '':
 
            lista_verbi.loc[len( lista_verbi )] = verbo_nuovo

        else:
             print("\ncorrect the entry:\n")


except KeyboardInterrupt:

    print('\n\n\nSaving to file')

    lista_verbi = lista_verbi.drop_duplicates()
    
    lista_verbi.to_csv( data_file )


print( lista_verbi )
