for i in range(7):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
else:
    print("Loop completed without break")