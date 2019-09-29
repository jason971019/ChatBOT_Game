# ChatBOT_Game
## Object
Doing a Bull and Cows game on a Telegram chatbot. Force users to guess at least 7 times. Cheating is a must. However, cheating must not be caught.
## Code
```Python
import random, os
from telegram.ext import Updater, CommandHandler
from random import sample
from itertools import combinations

answer_list = []

def valid(s): # Check whether a input is valid
    if len(s)!=4:
        return False
    if any(x not in '0123456789' for x in s):
        return False
    if any(x==y for x, y in combinations(s,2)):
        return False
    return True

def read_four_distinct_digits(): # Read string which has four distinct digits
    f = open(r'C:/Users/psy64/Dropbox/Introduction to Python/Guesses.txt')
    text = []
    for line in f:
        text.append(line)
    f.close()
    ret = text[-1][0:-1]
    if valid(ret):
        return ret
    print(str(ret)+' is not valid.')

def replace_AnswerList(ANS_list,ANS,GUESS,a,b): #建立所有可能答案，並將和曾猜過答案A、B值不同的可能答案剔除
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

if os.path.exists('Guesses.txt'):
    with open('Guesses.txt') as FILE:
        sentences = [sentence.strip() for sentence in FILE]
else:
    sentences = []

def start(bot, update):
    global test
    test = 0
    update.message.reply_text('Input four distinct digits: (ex. /guess 0123)')
    
def Guess(bot, update):
    global answer_list,test
    if True:
        sentence = update.message.text[7:].replace('\n', '')
        sentences.append(sentence)
        with open('Guesses.txt', 'a') as FILE:
            print(sentence, file=FILE)
    if test != 0:
        ans = random.sample(answer_list, 1)[0]
        print('The answer is changed:', ans)
        test+=1
    if test == 0:
        nums=5040
        answer_list=[None]*nums
        i=0
        for k in range(10):
            for h in range(10):
                for d in range(10):
                    for s in range(10):
                        if k!=h and k!=d and k!=s and h!=d and h!=s and d!=s:
                            answer_list[i]=k*1000+h*100+d*10+s
                            answer_list[i]="%04d"%answer_list[i]
                            i=i+1
        ans = ''.join(sample('0123456789',4))
        print('The answer is:',ans)
        test+=1
    guess = str(read_four_distinct_digits())
    print('The guess is: ',guess)
    if guess != ans:
        A = sum(1 for x,y in zip(guess,ans) if x==y)
        B = sum(1 for x in guess if x in ans)-A
        print(guess,'is {}A{}B.'.format(A,B))
        update.message.reply_text(str(guess)+' is '+ str(A) +'A' + str(B) + 'B')
        answer_list = replace_AnswerList(answer_list,ans,guess,A,B)
        update.message.reply_text('Input four distinct digits: (ex. /guess 0123)')
    else:
        update.message.reply_text('Congrats! The answer is '+ ans)
        update.message.reply_text('You have tried '+ str(test) +' times')
        update.message.reply_text('Typing /start to play again')

updater = Updater('BOT TOKEN')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('guess', Guess))

updater.start_polling()
updater.idle()
```
