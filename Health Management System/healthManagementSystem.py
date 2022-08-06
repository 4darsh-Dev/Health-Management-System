
toLog = ["Diet-Log", "Excercise-Log", "Exit"]
userList = ["Rohan","Shreya", "Danerys"]


class User:
    '''Contains the details of the users who have the access to the system'''
    def __init__(self, user1, user2, user3) -> None:
        self.user1 = user1
        self.user2 = user2
        self.user3 = user3
        
    def printFunc(self):
        # optional if you want to print the userNames for checking purpose
        print(f"User : {self.user1}")
        print(f"User : {self.user2}")
        print(f"User : {self.user3}")




class Log(User):
    '''For writing and displaying logging details of the user'''

    def logDietFunc(self,userName, toWrite):
        # takes username and diet details to write and save the details in given file

        if userName == self.user1:
            with open("rohan_diet_log.txt", 'a') as f:
                f.write(toWrite)
                print("\nLogged Successfully! ")

        elif userName == self.user2:
            with open("shreya_diet_log.txt", 'a') as f:
                f.write(toWrite)
                print("\nLogged Successfully! ")

        elif userName == self.user3:
            with open("danerys_diet_log.txt", 'a') as f:
                f.write(toWrite)
                print("\nLogged Successfully! ")
        else:
            print("Invalid Input! ")

    def logExerciseFunc(self, userName, toWrite):
        # takes the username and exercise details and save the details in given file

        if userName == self.user1:
            with open("rohan_exercise_log.txt", 'a') as f:
                f.write(toWrite)
                print("\nLogged Successfully! ")

        elif userName == self.user2:
            with open("shreya_exercise_log.txt", 'a') as f:
                f.write(toWrite)
                print("\nLogged Successfully! ")

        elif userName == self.user3:
            with open("danerys_exercise_log.txt", 'a') as f:
                f.write(toWrite)
                print("\nLogged Successfully! ")
        else:
            print("Invalid Input! ")
    
    def retriveDietFunc(self, userName):
        # takes the username and then gives the diet log details of the desired user 

        if userName == self.user1:
            with open("rohan_diet_log.txt", 'r') as f:
                content = f.read()
                print(f"\nDiet Log Details:-\n\n\t{content}")
        elif userName == self.user2:
            with open("shreya_diet_log.txt" , 'r') as f:
                content = f.read()
                print(f"\nDiet Log Details:-\n\n\t{content}")
        elif userName == self.user3:
            with open("danerys_diet_log.txt", 'r') as f:
                content = f.read()
                print(f"\nDiet Log Details:-\n\n\t{content}")

    def retriveExerciseFunc(self, userName):
        # takes the username and then gives the exericse log details of the desired user 

        if userName == self.user1:
            with open("rohan_exercise_log.txt", 'r') as f:
                content = f.read()
                print(f"\nExercise Log Details:-\n\n\t{content}")
        elif userName == self.user2:
            with open("shreya_exercise_log.txt" , 'r') as f:
                content = f.read()
                print(f"\nExercise Log Details:-\n\n\t{content}")
        elif userName == self.user3:
            with open("danerys_exercise_log.txt", 'r') as f:
                content = f.read()
                print(f"\nExercise Log Details:-\n\n\t{content}")
                


myLog = Log("Rohan", "Shreya","Danerys")



if __name__ == "__main__":
    welcomeMsg = '''\n========Welcome to the Health Management System (HMS)========
What you want to do?
  1. Log/Record Data
  2. Retrive Data
  3. Exit'''
    while(True):
        print(welcomeMsg)
        
        userInput = int(input("Enter a choice : "))
        if userInput == 1:
            # to choose what you want to do in (HMS)
            print("List of Users :-")
            for item in userList:
                print(f" * {item}")

            userName = int(input("\nEnter User: "))
            if userName == 1:
                print("Available Log Options :-")
                for item in toLog:
                    # for priting the avaiable log options # it is for logging data
                    print(f" * {item}")
                        
                userLog = int(input("\nChoose log option : "))
                if userLog == 1:
                    # you've chose diet log
                    dietDetails = input("\nEnter Diet Info : ")
                    myLog.logDietFunc("Rohan", dietDetails)

                elif userLog == 2:
                    # you've chose excercise log
                    exerciseDetails = input("\nEnter Excercise Info : ")
                    myLog.logExerciseFunc("Rohan", exerciseDetails)

                elif userLog == 3:
                    exit()
                
                else:
                    print("Invalid Choice!")


            elif userName == 2 :
                print("Available Log Options :-")
                for item in toLog:
                    # for priting the avaiable log options
                    print(f" * {item}")
                        
                userLog = int(input("\nChoose log option : "))
                if userLog == 1:
                    # you've chose diet log
                    dietDetails = input("\nEnter Diet Info : ")
                    myLog.logDietFunc("Shreya", dietDetails)
                        
                elif userLog == 2:
                    # you've chose excercise log
                    exerciseDetails = input("\nEnter Excercise Info : ")
                    myLog.logExerciseFunc("Shreya", exerciseDetails)

                elif userLog == 3:
                    exit()
                
                else:
                    print("Invalid Choice!")


            elif userName == 3:
                print("Available Log Options :-")
                for item in toLog:
                    # for priting the avaiable log options
                    print(f" * {item}")
                        
                userLog = int(input("\nChoose log option : "))
                if userLog == 1:
                    # you've chose diet log
                    dietDetails = input("\nEnter Diet Info : ")
                    myLog.logDietFunc("Danerys", dietDetails)
                        
                elif userLog == 2:
                    # you've chose excercise log
                    exerciseDetails = input("\nEnter Excercise Info : ")
                    myLog.logExerciseFunc("Danerys", exerciseDetails)

                elif userLog == 3:
                    exit()

                else:
                    print("Invalid Choice!")


            else:
                print("Invalid Choice! ")

        elif userInput == 2:
            # to choose what you want to do in (HMS) # it is for retirving data
            print("List of Users :-")
            for item in userList:
                print(f" * {item}")

            userName = int(input("\nEnter User: "))
            if userName == 1:
                print("Available Log Options :-")
                for item in toLog:
                    # for priting the avaiable log options
                    print(f" * {item}")
                        
                userLog = int(input("\nChoose log option : "))
                if userLog == 1:
                    # you've chose diet log
                    myLog.retriveDietFunc("Rohan")

                elif userLog == 2:
                    # you've chose excercise log
                    myLog.retriveExerciseFunc("Rohan")

                elif userLog == 3:
                    exit()

                else:
                    print("Invalid Choice!")


            elif userName == 2 :
                print("Available Log Options :-")
                for item in toLog:
                    # for priting the avaiable log options
                    print(f" * {item}")
                        
                userLog = int(input("\nChoose log option : "))
                if userLog == 1:
                    # you've chose diet log
                    myLog.retriveDietFunc("Shreya")
                        
                elif userLog == 2:
                    # you've chose excercise log
                    myLog.retriveExerciseFunc("Shreya")
                
                elif userLog == 3:
                    exit()
                
                else:
                    print("Invalid Choice!")


            elif userName == 3:
                print("Available Log Options :-")
                for item in toLog:
                    # for priting the avaiable log options
                    print(f" * {item}")
                        
                userLog = int(input("\nChoose log option : "))
                if userLog == 1:
                    # you've chose diet log
                    myLog.retriveDietFunc("Danerys")
                        
                elif userLog == 2:
                    # you've chose excercise log
                    myLog.retriveExerciseFunc("Danerys")
                
                elif userLog == 3:
                    exit()
                
                else:
                    print("Invalid Choice!")


            else:
                print("Invalid Choice! ")
            
        elif userInput == 3:
            exit()
        else:
            print("Invalid Choice! ")

         

    
