# 0.1 - can you watch
# brute force method gedan, but sadly I could not think of any cleverer way to approach this problem
# by looping throw each digit in the user input and checking if num == 1 then increment count and proceed
def count_no_1s():
    while True:
        try:
            n = int(input("Enter an integer between 1-942: "))
        except ValueError:
            print("Please enter a valid integer 1-942")
            continue
        if 1 <= n <= 942:
            print(f'input number N: {n}')
            count = 0
            for i in range(1, n + 1):
                t = i
                while t != 0:
                    m = t % 10
                    t = t // 10
                    if m == 1:
                        count += 1
            print(f"from 1 to {n} the number '1' shows up : {count} times")
            break
        else:
            print('The integer must be in the range 1-942')


# 1.2 - 8 of game

import random


def eights_of_game():
    bag = []
    for i in range(0, 5):
        random_item = random.randint(1, 1000)
        bag.append(random_item)
    print(bag)
    while True:
        user_input = str(input("user : "))
        if user_input == "remove":
            if len(bag) > 5:
                user_remove_item = int(input("user : "))
                bag.remove(user_remove_item)
                print(bag)
            else:
                print("cannot remove, bag at minimum capacity")

        elif user_input == "enter":
            user_add_item = int(input("user : "))
            bag.append(user_add_item)
            print(bag)

        else:
            print("Please enter a valid input (remove,enter)")


# 2.3 - Show me
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk


def show_image(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()
    photo = ImageTk.PhotoImage(data=raw_data)
    label = Label(image=photo)
    label.image = photo
    label.place(x=175, y=175, height=350, width=350)


def show_me():
    root = Tk()
    root.geometry('700x'
                  '700')
    root.title("Show me!")
    root.config(bg="#263D42")
    dog_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOxwhJsSHOQ0O6WqW99tWmV1y7c-Z7iQmKgg&usqp=CAU"
    person_url = "https://pbs.twimg.com/profile_images/1532076095331348485/5gfRozAz_400x400.jpg"
    car_url = "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-1fwkhcm_90dc1edd.jpeg?region=0,0,300,450"

    car_button = Button(root, text="Show Car", command=lambda m=car_url: show_image(m))
    car_button.place(x=175, y=50, height=50, width=80)
    person_button = Button(root, text="Show Person", command=lambda m=person_url: show_image(m))
    person_button.place(x=350, y=50, height=50, width=80)

    dog_button = Button(root, text="Show Dog", command=lambda m=dog_url: show_image(m))
    dog_button.place(x=525, y=50, height=50, width=80)

    root.mainloop()


# count_no_1s()
# eights_of_game()
# show_me()
