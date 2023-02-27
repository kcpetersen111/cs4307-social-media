#!/usr/bin/env python3
import dbSetup
import user

def main():
    db = dbSetup.Migration()
    
    # will be the userID once logged in but should make sure that is not null
    usr = None

    print("Welcome to a nother social media\n")
    while True:
        print()
        ui = input("What do you want to do?\n> ").lower().split() 
        ui = ui if len(ui)!=0 else ["ThisIsAMagicNumberToMakeSureNothingCrashesAndIDontWantToComeUpWithABetterIdea","ThatHas","EnoughStuffForTheChecks"]
        
        if(ui[0] == "exit"):
            db.close()
            quit(0)
        elif (ui[0] == "user" and ui[1] == "create"):
            if (len(ui) != 4):
                print("Not enough arguments")
                continue
            user.Create(db, ui[2], ui[3])
        elif (ui[0] == "user" and ui[1] == "list"):
            user.ListUsers(db)
        elif (ui[0] == "user" and ui[1] == "login"):
            if (len(ui) != 4):
                print("Not enough arguments")
                continue
            usr = user.Login(db, ui[2], ui[3])
        else:
            print("That is an unknown command")
        
    
    
if __name__ == "__main__":
    main()