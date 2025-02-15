def display():
    print("<--Tejas ingle solution-->")
    print("\n-:-  Salary status  -->:")
    bs = float(input("\nEnter your basic salary:-> "))
    choice = int(input("\n--> Choose the month(1)/Year(2): "))
    return bs, choice  # return both bs and choice



def hraf(bs, hr=10):  # pass bs as an argument
    hra = (hr * bs) / 100
    print(f"HRA calculated: {hra}")
    return hra  # return the calculated hra



def taf(bs,  ta=0.05):  # pass bs and hra as arguments
    ta = ta * bs  # corrected the calculation
    print(f"TA calculated: {ta}")
    return ta  # return the ta value




def paf(bs, pa=0.02):  # return pf value
    pf = pa * bs # adjusted the formula
    print(f"PF calculated: {pf}")
    return pf  # return the calculated PF




def nsf(bs,hra,ta,pf):
    ns=bs+hra+ta-pf
    print(f"\nGross Salary calculated: {ns}")
    
    return ns

# Main logic






bs, choice = display()  

# Get both bs and choice from display

if choice == 1:
    print("\n")
    hra = hraf(bs)  # get the HRA for month
    ta = taf(bs)  # calculate TA and store it
    pa = paf(bs)
    print("\n-------------------------------------------") 
    ns=nsf(bs,hra,ta,pa)
      # calculate PF and store it

elif choice == 2:
    hra = hraf(bs, hr=12)  # get the HRA for year
    ta = taf(bs, hra)  # calculate TA and store it
    pa = paf(bs, hra, ta)  # calculate PF and store it
else:
    print("Invalid choice.")




if(0<ns<1200000):
   print("\n-------------------------------------------")
   ns=nsf(bs,hra,ta,pa)
   print("\n----no tax reduction...----")
   print(f" \n:) Account in credit amount--{ns}")
   print("\n")

elif(1200000<ns<1600001):
   print("\n-------------------------------------------")
   ns=(15*ns)/100
   print("\n----15% tax reduction...----")
   print(f" \n:) Account in credit amount--{ns}")
   print("\n")

elif(1600000<ns<2000001):
    print("\n-------------------------------------------")
    ns=(20*ns)/100
    print("\n----20% tax reduction...----")
    print(f" \n:) Account in credit amount--{ns}")
    print("\n")

elif(2000000<ns<2400001):
   print("\n-------------------------------------------")
   ns=(25*ns)/100
   print("\n----25% tax reduction...----")
   print(f" \n:) Account in credit amount--{ns}")
   print("\n")

else:
   print("\n-------------------------------------------")
   ns=(30*ns)/100
   print("\n----30% tax reduction...----")
   print(f" \n:) Account in credit amount--{ns}")
   print("\n")
