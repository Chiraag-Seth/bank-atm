fail = "Sorry! That pin was actually incorrect"
pinInput = input("Please enter your card pin")
startInput = input("Would You Like To Deposit Or Withdraw Money")
if(startInput == "Deposit"):
    depositInput = input("How much would you like to deposit?")
    retryInput = input("Please enter your pin again to deposit the money")
    if(retryInput == pinInput):
        print("Okay! $",depositInput, "has entered your account")
    else:
        print(fail)
if(startInput == "Withdraw"):
    withdrawInput = input("How much would you like to withdraw?")
    redoInput = input("Please enter your pin again to withdraw the money")
    if(redoInput == pinInput):
        print("Okay! $", withdrawInput, "has exited your account")
    else:
        print(fail)
