count_progress = 0
count_trailer = 0
count_retriever = 0
count_exclude = 0


def progression_outcome():
    global count_progress, count_trailer, count_retriever, count_exclude
    if pass_credit == 120:
        count_progress += 1
        print("Progress")
    elif pass_credit == 100:
        count_trailer += 1
        print("Progress (module trailer)")
    elif pass_credit <= 80 and defer_credit <= 120 and fail_credit <= 60:
        count_retriever += 1
        print("Module retriever")
    elif pass_credit <= 40 and defer_credit <= 40 and fail_credit <= 120:
        count_exclude += 1
        print("Exclude")


def histogram():
    print(f"""
{"-" * 60}  
Histrogram
Proggress {count_progress} : {count_progress * "*"}
Trailer {count_trailer} : {count_trailer * "*"}
Retriever {count_retriever} : {count_retriever * "*"}
Exclude {count_exclude} : {count_exclude * "*"}

{count_progress + count_trailer + count_retriever + count_exclude} outcomes in total.

{"-" * 60} 
    """)


while True:
    while True:
        try:
            pass_credit = int(input("Enter your total PASS credits:"))
            if pass_credit in range(0, 121, 20):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer Required")

    while True:
        try:
            defer_credit = int(input("Enter your total DEFER credits:"))
            if defer_credit in range(0, 121, 20):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer Required")

    while True:
        try:
            fail_credit = int(input("Enter your total FAIL credits:"))
            if fail_credit in range(0, 121, 20):
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer Required")

    if pass_credit + defer_credit + fail_credit == 120:
        progression_outcome()

        select = input("""
Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: """)
        if select == 'q':
            histogram()
            break
        elif select == 'y':
            continue
        else:
            print("Invalid Input")
    else:
        print("Total incorrect")
