def check_alpha(x):
    f = False
    for char in x:
        c = char.isnumeric()
        if char.isnumeric() == True and f == False:
            # Check if first number in number list is 0
            if char == "0" and f == False:
                print("0")
                return False
            
            f = True
        
                   
        if f == True and char.isalpha() == True:
            return False
            
    return True  

def validate(l, p):
    if l >= 2 and l <= 6:
            if p[0].isalpha() and p[1].isalpha(): # if first two character are letter(Isalpha from tutorialpoint.com)
                #print("True")
                l = l
                #print(l)
    else:
        return False
            
    return True 
           
def main():
    while True: 
        plates = input("Check your plate here *") #get the plate

        plates_to_list = list(plates.upper()) # convert plate to upper and list
        p = plates_to_list
        l = len(p)

        validate(l, p)
        check_alpha(p)

        if validate(l, p) == True and check_alpha(p) == True:
            print("Valid Plate")
            break

        else:
            print("Invalid plate")    
        
            


main()
