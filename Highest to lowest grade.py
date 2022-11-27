math = int(input("Enter math grade: "))
ap = int(input("Enter ap grade: "))
pe = int(input("Enter pe grade: "))

if (math > ap and math > pe):
    print("the highest grade is", math)
    if (ap > pe):
        print("The second highest grade is", ap)
        print("the lowest grade is", pe)

    elif (pe > ap):
        print("The second highest grade is", pe)
        print("The lowest grade is", ap)

if (ap > math and ap > pe):
    print("the highest grade is", ap)
    if (math > pe):
        print("the second highest grade is", math)
        print("the lowest grade is", pe)

    elif (pe > math):
        print("The second highest grade is", pe)
        print("The lowest grade is", math)

if (pe > math and pe > ap):
    print("the highest grade is", pe)
    if (math > ap and math > pe):
        print("the second highest grade is", math)
        print("the lowest grade is", ap)

    elif (ap > math):
        print("The second highest grade is", ap)
        print("The lowest grade is", math)
