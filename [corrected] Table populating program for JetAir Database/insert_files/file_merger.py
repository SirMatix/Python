def first_merge():
    country = [line for line in open("1 insert statements for country table.txt")]
    city = [line for line in open("2 insert statements for city table.txt")]
    postcode_air = [line for line in open("3 insert statements for postcode table.txt")]

    with open("_1_ insert.txt", "w") as file:
        for i in range(len(country)):
            file.write(country[i])
        for i in range(len(city)):
            file.write(city[i])
        for i in range(len(postcode_air)):
            file.write(postcode_air[i])
        
### '_2_ INSERT.TXT' ###                   

def second_merge():
    postcode = [line for line in open("5 insert statements for postcode table.txt")]
    p_model = [line for line in open("6 insert statements for plane model table.txt")]
    plane = [line for line in open("7 insert statements for plane table.txt")]
    qualification = [line for line in open("8 insert statements for qualifications table.txt")]
    passanger = [line for line in open("9 insert statements for passanger table.txt")]
    employee = [line for line in open("10 insert statements for employee table.txt")]
    pilot = [line for line in open("11 insert statements for pilot table.txt")]
    route = [line for line in open("12 insert statements for route table.txt")]
    price = [line for line in open("13 insert statements for price table.txt")]
    flight = [line for line in open("14 insert statements for flight table.txt")]
    ticket = [line for line in open("15 insert statements for ticket table.txt")]
    reservation = [line for line in open("16 insert statements for reservation table.txt")]

    with open("_2_ insert.txt", "w") as file:
        for i in range(len(postcode)):
            file.write(postcode[i])
        for i in range(len(p_model)):
            file.write(p_model[i])
        for i in range(len(plane)):
            file.write(plane[i])
        for i in range(len(qualification)):
            file.write(qualification[i])
        for i in range(len(passanger)):
            file.write(passanger[i])
        for i in range(len(employee)):
            file.write(employee[i])
        for i in range(len(pilot)):
            file.write(pilot[i])
        for i in range(len(route)):
            file.write(route[i])
        for i in range(len(price)):
            file.write(price[i])
        for i in range(len(flight)):
            file.write(flight[i])
        for i in range(len(ticket)):
            file.write(ticket[i])
        for i in range(len(reservation)):
            file.write(reservation[i])
