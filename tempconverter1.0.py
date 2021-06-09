#tempconvert.py
for i in range (10):
    val = input ('PLEASE INPUTE TEMPURE WITH SYMBLE. FOR EXAMPLE 32C):')
    if val[-1] in ['C' , 'c']:
        f = 1.8 * float(val[0:-1]) + 32
        print('CONVERTED TEMP IS :%.2fF'%f)
    elif val[-1] in ['F' , 'f']:
        c = (float(val[0:-1])-32) / 1.8
        print('CONVERTED TEMP IS : %.2fc'%c)
    else:
        print( 'inpute error' )
 
 
