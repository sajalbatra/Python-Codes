basic_sal=int(input("enter basic salary: "))
gender=input("enter gender in lower case: ")
if basic_sal>=10000 and basic_sal<=35000:
    CCA=500
    if gender=='male':
        HRA=3000
        DA=0.25*(basic_sal)
    else:
        HRA=3200
        DA=0.30*(basic_sal)
    PF=0.10*(basic_sal+HRA)
elif basic_sal >=40000 and basic_sal<=75000:
    CCA=700
    if gender=='male':
        HRA=5000
        DA=0.27*(basic_sal)
    else:
        HRA=5500
        DA=0.32*(basic_sal)
    PF=0.15*(basic_sal+DA)
NET_SALARY =basic_sal+DA+HRA+CCA+PF
print("the net salary is : ",NET_SALARY)
