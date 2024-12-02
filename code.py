#Here is the code for the program 
import random

def get_random_joke():
    jokes = [
        "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do programmers hate nature? It has too many bugs.",
        "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
        "Why do Python programmers prefer using functions? Because they can't handle the class!",
        "What do you call a snake that works for the government? A civil serpent!",
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "What is a programmer's favorite hangout place? Foo Bar.",
        "Hillary tried to write a program, but it kept crashing. Turns out, it needed a *Hillary* of error checking!",
        "Why did Hillary bring a ladder to the programming conference? Because he heard the talks were on a higher level!",
        "Hillary's code is so clean, it should come with a *Hillary* of approval!",
        "Why did Hillary always carry a pencil while coding? In case he needed to draw some conclusions!"
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print("Here's a random programming joke for you:
