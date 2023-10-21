
import pandas as pd
import random



def report():

  
    print(f"\nerrors:\t{errors}\t{ round( errors/total * 100 ,3 ) }%")

print("QUIZ VERBI IRREGOLARI")

data_file = 'data\\verbs.csv'


lista_verbi = pd.read_csv( data_file, header = 0, index_col=0 )

errors = 0
total = 0

for index,verb in lista_verbi.iterrows():

    choose= [0,1,2,3]

    q = choose.pop( random.randint(0,2) ) 

    print(f"{lista_verbi.columns[q].upper():<25}:\t{verb.iloc[q].upper()}\n" )

    for n in choose:
        total +=1
        if input( f"{lista_verbi.columns[n]:<25}:\t",  ).rstrip() == verb.iloc[n]:
            print('OK')


        else:
            print(f'Sbagliato: { verb.iloc[n] }')

            if n != 3:
                errors += 1

    report()
    print('\n\n\n')