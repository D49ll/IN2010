import sys

def check(inputs, sorted_f):
    with open(sorted_f, 'r') as f:
        outputs = [int(x) for x in f.readlines()]
    if outputs == inputs:
        return True
    else:
        return False
   

def main(filname):
    names = ['heap', 'insertion','quick','selection']
    #names2 = ['heap','quick']

    with open(filname, 'r') as f:
        inputs = [int(x) for x in f.readlines()]
    inputs.sort()

    for name in names:
        if check(inputs, filname+'_'+name+'.out'):
            print(f'{name} sort is correct')
        else:
            print(f'{name} sort is not correct')

if __name__ == "__main__":
    main(sys.argv[1])
