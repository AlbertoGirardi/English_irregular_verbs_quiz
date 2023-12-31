import time
import pandas as pd
import random
import sys





def report():
  
    print(f"\nerrors:\t{errors}/{total}\t{ round( errors/total * 100 ,3 ) }%")


print("quiz verbi irregolari\n\nto exit ctrl+c\n\n")

data_file = 'data\\verbs.csv'

try:
    lista_verbi = pd.read_csv( data_file, header = 0, index_col=0 )

except FileNotFoundError:

    try:
        lista_verbi = pd.read_csv( "verbs.csv", header = 0, index_col=0 )

    except FileNotFoundError:
        print("FILE NOT FOUND!!!")
        sys.exit()

errors = 0
total = 0

t0 = time.time()

indexs = []
verbs = []
error_list = []
num = 1

try:

    for index, verb in lista_verbi.iterrows():
        indexs.append(index)
        verbs.append(verb)

    for _ in range( len( lista_verbi ) ):

        index = indexs.pop( random.randint( 0, len(indexs)-1 ) )
        #print(indexs)
        verb = verbs[index]

        choose= [0,1,2,3]

        q = choose.pop( random.randint(0,2) ) 

        print(f'{num}/{len( lista_verbi )}')
        print(f"{lista_verbi.columns[q].upper():<25}:\t{verb.iloc[q].upper()}\n" )

        for n in choose:
            total +=1
            if input( f"{lista_verbi.columns[n]:<25}:\t",  ).rstrip() == verb.iloc[n]:
                print('OK')


            else:
                print(f'Sbagliato: { verb.iloc[n] }')

                if n != 3:
                    errors += 1
                    error_list.append( verb.iloc[0] )
        num += 1

        report()
        print('\n\n\n')


except KeyboardInterrupt:
    print("\n\n\nconclusione test")

t2 = time.time()
print(f"time:\t{round((t2-t0)/60, 3)}")
report()

print(f"\nVerbi sbagliati: {error_list}")
