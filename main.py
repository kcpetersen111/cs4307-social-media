#!/usr/bin/env python3
import dbSetup

def main():
    db = dbSetup.Migration()

    print("Welcome to a nother social media\n")
    while True:
        print()
        ui = input("What do you want to do?\n> ")
        if(ui == "exit"):
            db.close()
            quit(0)
        
        else:
            print("That is an unknown command")
        
    
    
if __name__ == "__main__":
    main()