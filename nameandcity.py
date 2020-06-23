#program that allows user to input name and birthplace
#ensures that birthplace is correct
#6/23/2020
first_name = input("What is your name? ")
home = input(first_name + " where were you born?(City and State) ")

answer_yes = "yes"
answer_no = "no"
answer = input(first_name + " are you from " + home + "? ")

if answer.lower() == answer_yes.lower():            #lowercase function converts upper to lowercase
    print(first_name + " you were born in " + home)
elif answer.lower() == answer_no.lower():
    home_correct = input(first_name+ " please enter your correct birthplace ")
    answer_new = input(first_name + " were you born in " + home_correct + "? ")

    if answer_new.lower() == answer_yes.lower():
        print("\n"+first_name + " you were born in " + home_correct)
    else:
        print("\nPlease restart your application")