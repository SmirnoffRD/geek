def lucky_ticket(ticket_number):
    if len(str(ticket_number)) > 6:
        print('Oshibka')
    elif len(str(ticket_number)) < 6:
        k = '0'*(6 - len(str(ticket_number)))
        ticket_number = str(k + str(ticket_number))
    #for first_numbers in ticket_number:
    sum_f = 0
    sum_l = 0
    for x in ticket_number[0:3]:
        sum_f += int(x)
    for y in ticket_number[3:]:
        sum_l += int(y)
    otvet = ''
    if sum_l == sum_f:
        otvet = "Vi viiigrali"
    else:
        otvet = "Ne povezlo"
    return otvet



res = lucky_ticket(9573)
print(res)
