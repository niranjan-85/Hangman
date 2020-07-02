
import random

def show_user(list,temp,word):
    for i in range(len(list)):
        if list[i]==word:
            temp[i]=word
    return temp


def generate_phrase(index,my_list):
    print("Your question: {}".format(*words_list[index].values()))


words_list=[
    {'Iron man':'Genius,millionaire,playboy,philanthropist'},
    {'Captain America':'I can do this all day'}
]
x=random.randrange(0,2)
generate_phrase(x,words_list)
temp=[]
main_word=[]
for i in words_list[x].keys():
    for word in i:
        if word != " ":
            temp.append("_")
        else:
            temp.append(" ")
        main_word.append(word)

print(*temp)
while(1):
    user=input("\nEnter your letter")
    result=show_user(*words_list[x].keys(), temp, user)
    print(*result)
    if(result==main_word):
        print("Congrats !! You Win")
        break








