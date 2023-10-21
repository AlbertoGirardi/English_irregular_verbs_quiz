import pandas as pd



print("QUIZ VERBI IRREGOLARI")

data_file = 'data\\verbs.csv'


lista_verbi = pd.read_csv( data_file, header = 0, index_col=0 )

for verb in lista_verbi:
    print(verb)

