import random
seed=0
def sushu():
    a=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,71, 73, 79, 83, 89, 97 ]
    # seed-=1
    num=random.randint(0,24)
    return a[num]
if __name__=='__main__':
    print((sushu()))
