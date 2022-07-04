import git

git remote add origin https://github.com/AlexanderZah/random_first.git
 git branch -M main 
git push -u origin main

import random

def is_valid(n):
    if n.isdigit():
        n=int(n)
        if n>=1 and n<=100:
            return True
        else:
            return False
    else :
        return False

num = random.randint(1,100)
print('Добро пожаловать в числовую угадайку,введите число от 1 до 100')
t = 0
answer = "д"
while answer == "д" :
    n = input()
    
    if is_valid(n) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        
    elif is_valid(n) == True:
        n = int(n)
        if n<num :
        
            print ('Ваше число меньше загаданного, попробуйте еще разок')
            t +=1
        elif n>num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            t+=1

        elif n == num:
            print('Вы угадали за',t,'попыток, поздравляем!')
            print ('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            print('Хотите сыграть еще? д = Да , н = Нет')
            answer = input()
            


    


