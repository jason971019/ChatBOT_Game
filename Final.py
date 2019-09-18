import random, os
from telegram.ext import Updater, CommandHandler
from random import sample
from itertools import combinations

# Check whether a input is valid
def valid(s):
    if len(s)!=4:
        return False
    if any(x not in '0123456789' for x in s):
        return False
    if any(x==y for x, y in combinations(s,2)):
        return False
    return True

# Read string which has four distinct digits
def read_four_distinct_digits():
    while True:
        ret = input('Input four distinct digits: ')
        if valid(ret):
            return ret
        print(ret,'is not valid.')

def replace_AnswerList(ANS_list,ANS,GUESS,a,b):
    n=0
    ANS_list_len = len(ANS_list)
    for i in range(0,ANS_list_len):
        aa = sum(1 for x,y in zip(GUESS,str(ANS_list[i])) if x==y)
        bb = sum(1 for x in GUESS if x in str(ANS_list[i]))-aa
        if aa == a and bb == b:
            ANS_list[n] = ANS_list[i]
            n+=1
    for i in range(n,ANS_list_len):
        ANS_list.pop(n)
    return ANS_list

def change_ans(new_ANS_list):
    new_ANS = random.sample(new_ANS_list, 1)
    return new_ANS
        
    
    

updater = Updater('871622109:AAFbFqowD24iC-b2faWdUf2QO2EGEtp2GiA')

nums=5040
ans_list=[None]*nums
i=0
for k in range(10):
    for h in range(10):
        for d in range(10):
            for s in range(10):
                if k!=h and k!=d and k!=s and h!=d and h!=s and d!=s:
                    ans_list[i]=k*1000+h*100+d*10+s
                    ans_list[i]="%04d"%ans_list[i]
                    i=i+1

ans = ''.join(sample('0123456789',4))
print(ans)

guess = read_four_distinct_digits()
while guess != ans:
    A = sum(1 for x,y in zip(guess,ans) if x==y)
    B = sum(1 for x in guess if x in ans)-A
    print(guess,'is {}A{}B.'.format(A,B))
    ans_list = replace_AnswerList(ans_list,ans,guess,A,B)
    ans = change_ans(ans_list)
    print(ans)
    guess = read_four_distinct_digits()
    
print('Congrats! The answer is',ans)

updater.start_polling()
updater.idle()