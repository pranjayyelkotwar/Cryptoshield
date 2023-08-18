import hashlib



def assgn1():
    original = 'adc351dc969292b15daa4fe0e036c5f9'
    for i in range(1000000):
        i = 'qstp-'+str(i).zfill(6)+'-is-fun'
        if hashlib.md5(i.encode()).hexdigest() == original:
            print('Password is: ' + i)
            break

#qstp-692430-is-fun
