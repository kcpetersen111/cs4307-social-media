#!/usr/bin/env python3
import dbSetup
import user
import context

# will be the userID once logged in but should make sure that is not null
usr = None
cont = None

#for debugging
usr = "c919a566-a788-4ace-9528-6a7910928c04"
cont = "home"
#for debugging

def checkLogedin():
        if (not usr):
            print("You need to login first")
            return False
        return True

def checkContext():
        if (not cont):
            print("You need to switch to a context first")
            return False
        return True

def checkUiLength(ui,l):
        if (len(ui) != l):
            print("Not enough arguments")
            return False
        return True

def main():
    db = dbSetup.Migration()
    
    global usr, cont

    print("Welcome to a nother social media\n")
    while True:
        print()
        if (usr):
            print("Welcome ",user.GetName(db, usr)," current context: ",cont,"\n")
        ui = input("What do you want to do?\n> ").lower().split() 
        ui = ui if len(ui)!=0 else ["ThisIsAMagicNumberToMakeSureNothingCrashesAndIDontWantToComeUpWithABetterIdea","ThatHas","EnoughStuffForTheChecks"]
        
        if(ui[0] == "exit"):
            db.commit()
            db.close()
            quit(0)
        elif (ui[0] == "user" and ui[1] == "create"):
            if (checkUiLength(ui,4)):
                user.Create(db, ui[2], ui[3])
        elif (ui[0] == "user" and ui[1] == "list"):
            user.ListUsers(db)
        elif (ui[0] == "user" and ui[1] == "login"):
            if (checkUiLength(ui,4)):
                usr = user.Login(db, ui[2], ui[3])
        elif (ui[0] == "context" and ui[1] == "list"):
            if (checkLogedin()):
                context.List(db, usr)
        elif (ui[0] == "context" and ui[1] == "create"):
            if (checkLogedin() and checkUiLength(ui,3)):
                cont = context.Create(db, usr, ui[2])
        elif (ui[0] == "context" and ui[1] == "switch"):
            if (checkLogedin() and checkUiLength(ui,3)):
                cont = context.SwitchContext(db, usr, ui[2])
            if (not cont):
                print("Unable to switch to ",ui[2])
        elif (ui[0] == "see" and ui[1] == "feed"):
            if (checkLogedin() and checkContext()):
                context.SeeFeed(db, usr, cont)
        elif (ui[0] == "post"):
            if (checkLogedin() and checkContext()):
                context.Post(db, usr, cont, ui[1:])
        elif (ui[0] == "follow"):
            if (checkLogedin() and checkContext() and checkUiLength(ui,3)):
                context.Follow(db, usr, cont, ui[1], ui[2])
        
        else:
            print("That is an unknown command")
        
    
    
if __name__ == "__main__":
    main()
