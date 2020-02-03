import random


save_path = "insert_files\\"
read_path = "program_data\\"
list_of_files = ["list of countries.txt",
                 "list of cities.txt",
                 "airport_postcode.txt",
                 "airportpostcode cityID.txt",
                 "postcode index.txt",
                 "postcode CityID list.txt",
                 "list of first names.txt",
                 "list of last names.txt",
                 "list of street names.txt",
                 "Plane_model_list.txt",
                 "pilot index.txt",
                 "airport_indexes.txt"
                 ]


list_of_inserts = ["1 insert statements for country table.txt",
                   "2 insert statements for city table.txt",
                   "3 insert statements for postcode table.txt",
                   "5 insert statements for postcode table.txt",
                   "9 insert statements for passanger table.txt",
                   "7 insert statements for plane table.txt",
                   "10 insert statements for employee table.txt",
                   "11 insert statements for pilot table.txt",
                   "12 insert statements for route table.txt",
                   "13 insert statements for price table.txt",
                   "14 insert statements for flight table.txt",
                   "15 insert statements for ticket table.txt",
                   "16 insert statements for reservation table.txt"                  
                   ]

message = " table insert statements produced"

ene = '\n'



##########################################################################################
########################## INSERT GENERATING SECTION #####################################
##########################################################################################



def make_country_insert():
    table_name = "Country"
    file_path = save_path + list_of_inserts[0]
    data_path = read_path+ list_of_files[0]
    insert1 = "INSERT INTO Country VALUES"
    insert2 = "('','"
    insert3 = "'),"
    insert4 = "');"

    lineList = [line.rstrip(ene) for line in open(data_path)]
    
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(len(lineList)):
            if i == len(lineList)-1:
                file.write(insert2 + lineList[i] + insert4 + ene)
            else:
                file.write(insert2 + lineList[i] + insert3 + ene)
            
    success = table_name + message
    return success

def make_city_insert():
    table_name = "City"
    data_path = read_path + list_of_files[1]
    file_path = save_path + list_of_inserts[1]
    insert1 = "INSERT INTO City VALUES"
    insert2 = " ('','"
    insert3 = "', '186'),"
    insert4 = "', '186');"

    lineList = [line.rstrip(ene) for line in open(data_path)]

    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(len(lineList)):
            if i == len(lineList)-1:
                file.write(insert2 + lineList[i] + insert4 + ene)
            else:
                file.write(insert2 + lineList[i] + insert3 + ene)

    success = table_name + message
    return success


def postcode_airport():
    table_name = "Postcode"
    data_path = read_path + list_of_files[2]
    data_path1 = read_path + list_of_files[3]
    lineList = [line.strip(ene) for line in open(data_path)]
    lineList2 =[line.strip(ene) for line in open(data_path1)]
    file_path = save_path + list_of_inserts[2]
    insert1 = "INSERT INTO postcode VALUES"
    insert2 = "('','"
    insert3 = "', '"
    insert4 = "'),"
    insert5 = "');"

    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(len(lineList)):
            postcode = str(lineList[i])
            cityID = str(lineList2[i])
            if i == len(lineList)-1:
                file.write(insert2 + postcode + insert3 + cityID + insert5 + ene)
            else:
                file.write(insert2 + postcode + insert3 + cityID + insert4 + ene)

    success = table_name + message
    return success

def gen_post_code():
    data_path = read_path + list_of_files[4]
    lineList = [line.rstrip('\n') for line in open(data_path)]
    number = random.randint(0,len(lineList)-1)
    letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    f_letter = letters[random.randint(0,len(letters)-1)]
    s_letter = letters[random.randint(0,len(letters)-1)]
    postcode_index = lineList[number]
    if len(postcode_index) > 2:
        postcode = postcode_index + " " + str(random.randint(0,9)) + f_letter + s_letter
    else:
        postcode = postcode_index + str(random.randint(0,9)) + " " + str(random.randint(0,9)) + f_letter + s_letter
    postcode_list = postcode, number+1
    return postcode_list

def postcode_insert():
    table_name = "Postcode"
    insert1 = "INSERT INTO postcode VALUES"
    insert2 = "('','"
    insert3 = "', '"
    insert4 = "'),"
    insert5 = "');"
    file_path = save_path + list_of_inserts[3]

    cityID_list = []
    
    print("generating postcode table insert statements...")
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(num_of_postcodes):
            postcode = gen_post_code()
            cityID_list.append(postcode[1])
            if i == num_of_postcodes-1:
                file.write(insert2 + postcode[0] + insert3 + str(postcode[1]) + insert5 + ene)
            else:
                file.write(insert2 + postcode[0] + insert3 + str(postcode[1]) + insert4 + ene)
    data_path = read_path + list_of_files[5]
    with open(data_path, "w") as file:
        for i in range(len(cityID_list)):
            file.write(str(cityID_list[i]) + '\n')

    success = table_name + message
    
    return success

def city_post_list():
    data_path = read_path + list_of_files[5]
    cityID_list = [line.rstrip(ene) for line in open(data_path)]
    postcodeID = random.randint(1,num_of_postcodes)
    cityID = cityID_list[postcodeID-1]
    city_post = [cityID, postcodeID]
    return city_post

def gen_first_name():
    data_path = read_path+ list_of_files[6]
    lineList = [line.rstrip(ene) for line in open(data_path)]
    number = random.randint(0,len(lineList)-1)
    first_name = lineList[number]
    return first_name

def gen_last_name():
    data_path = read_path+ list_of_files[7]
    lineList = [line.rstrip(ene) for line in open(data_path)]
    number = random.randint(0,len(lineList)-1)
    last_name = lineList[number]
    return last_name

def gen_phone_num():
    prefix = "+44"
    number = ""
    for i in range(1,11):
        number += str(random.randint(0,9))
    number = prefix + number
    return number

def gen_dob():
    day = random.randint(1,31)
    month = random.randint(1,12)
    year = random.randint(1940,2001)
    dob = str(year) + "-" + str(month) + "-" + str(day)
    return str(dob)

def gen_street_name():
    data_path = read_path + list_of_files[8]
    lineList = [line.rstrip(ene) for line in open(data_path)]
    number = random.randint(0,len(lineList))
    street_name = lineList[number]
    street_end = ("Street","Road","Close","Avenue", "Alley")
    street_name = street_name + " " +  street_end[random.randint(0,len(street_end)-1)]
    return street_name

def gen_pass_num():
        letters = "ABCDEFGHIJKLMNOPRSTUWXYZ"
        first_letter = letters[random.randint(0,len(letters)-1)]
        second_letter = letters[random.randint(0,len(letters)-1)]
        number = ""
        for i in range(0,9):
            number += str(random.randint(0,9))
        passport_num = first_letter + second_letter + " " + number
        return passport_num

def passanger_insert():
    table_name = "Passanger"
    file_path = save_path + list_of_inserts[4]
    insert1 = "INSERT INTO Passanger VALUES"
    insert12 = "('', '"
    insert2 = "', '"
    insert3 = "', '"
    insert4 = "', '" 
    insert5 = "', '"
    insert6 = "' , '"
    insert7 = "', "
    insert8 = " , "
    insert9 = " , '"
    insert10 = "'),"
    insert11 = "');"

    print("generating passanger table insert statements...")

    
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(0,num_of_passangers):
            first = str(gen_first_name())
            last = str(gen_last_name())
            dob = str(gen_dob())
            phone = str(gen_phone_num())
            s_num = str(random.randint(1,100))
            street = str(gen_street_name())
            city_post = city_post_list()
            cityID = str(city_post[0])
            postID = str(city_post[1])
            passport = str(gen_pass_num())
            if i == num_of_passangers-1:
                part1 = insert12 + first + insert2 + last + insert3 + dob + insert4 + phone + insert5
                part2 = s_num + insert6 + street + insert7 + cityID + insert8 + postID + insert9 + passport + insert11
                file.write(part1 + part2 + ene)
            else:
                part1 = insert12 + first + insert2 + last + insert3 + dob + insert4 + phone + insert5
                part2 = s_num + insert6 + street + insert7 + cityID + insert8 + postID + insert9 + passport + insert10
                file.write(part1 + part2 + ene)

    success = table_name + message
    return success

def gen_purchase_date():
    day = random.randint(1,31)
    month = random.randint(1,12)
    year = random.randint(2013,2014)
    date = str(year) + "-" + str(month) + "-" + str(day)
    return str(date)

def gen_insurance_date():
    day = random.randint(1,31)
    month = random.randint(1,12)
    year = random.randint(2015,2018)
    date = str(year) + "-" + str(month) + "-" + str(day)
    return str(date)

def gen_p_model():
    data_path = read_path + list_of_files[9]
    lineList = [line.rstrip(ene) for line in open(data_path)]
    number = random.randint(0,len(lineList)-1)
    p_model = lineList[number]
    returnList = [number,p_model]
    return returnList

def gen_price(number):
    price_list = [77400, 89600, 220000, 714, 714]
    price = price_list[number]
    return price

def plane_insert():
    table_name = "Plane"
    file_path = save_path + list_of_inserts[5]
    insert1 = "INSERT INTO Plane VALUES"
    insert11 = "(''," 
    insert2 = ", '"
    insert3 = "', '" 
    insert4 = "', '" 
    insert5 = "'),"
    insert6 = "');"
    

    print("generating plane table insert statements...")
    
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(0,num_of_planes):
            returnList = gen_p_model()
            p_model = returnList[0]
            p_model_list.append(returnList[1])
            purchase_date = gen_purchase_date()
            insurance_date = gen_insurance_date()
            price = str(gen_price(p_model))
            if i == num_of_planes-1 :
                file.write(insert11+str(p_model+1)+insert2+purchase_date+insert3+insurance_date+insert4+price+insert6+ene)
            else:
                file.write(insert11+str(p_model+1)+insert2+purchase_date+insert3+insurance_date+insert4+price+insert5+ene)

    success = table_name + message
    return success


def gen_position():
    positions = ("Manager","Pilot","Flight Attendant","Ticket_Agent")
    salaries = (100000,65000,40000,28250)
    number = random.randint(0,len(positions)-1)
    position_salary = [positions[number],salaries[number]]
    return position_salary

def employee_insert():
    table_name = "Employee"
    file_path = save_path + list_of_inserts[6]
    data_path = read_path + list_of_files[10]
    
    insert1 = "INSERT INTO Employee VALUES"
    insert15 = "('', '" 
    insert2 = "', '" 
    insert3 = "', '" 
    insert4 = "', '" 
    insert5 = "', '" 
    insert6 = "', '" 
    insert7 = "'," 
    insert8 =  ", " 
    insert9 = ", '" 
    insert10 ="', '" 
    insert11 = "'),"
    insert12 = "');"
    

    
    positions = []
    salaries = []
    
    for i in range(f_number_of_employees*4):
        position = gen_position()
        if position[0] == "Manager" and "Manager" in positions and positions.count("Manager") == num_of_managers :
            position = gen_position()
        elif position[0] == "Pilot" and "Pilot" in positions and positions.count("Pilot") == num_of_pilots:
            position = gen_position()
        elif position[0] == "Flight Attendant" and "Flight Attendant" in positions and positions.count("Flight Attendant") == num_of_flight_att:
            position = gen_position()
        elif position[0] == "Ticket_Agent" and "Ticket_Agent" in positions and positions.count("Ticket_Agent") == num_of_ticket_a:
            position = gen_position()
        else:
            positions.append(position[0])
            salaries.append(position[1])


    print("Checks generated managers: " + str(positions.count("Manager")))
    print("Checks generated pilots: " + str(positions.count("Pilot")))
    print("Checks generated flight attendants: " + str(positions.count("Flight Attendant")))
    print("Checks generated ticket agents: " + str(positions.count("Ticket_Agent")))
    print("Checks total number of employees: " + str(f_number_of_employees))
    print(ene)
    print("generating employee table insert statements...")


    pilot_index = []
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(0,f_number_of_employees):
            first = str(gen_first_name())
            last = str(gen_last_name())
            dob = str(gen_dob())
            phone = str(gen_phone_num())
            s_num = str(random.randint(1,100))
            street = str(gen_street_name())
            city_post = city_post_list()
            cityID = str(city_post[0])
            postID = str(city_post[1])
            position = str(positions[i])
            
            if position == 'Pilot':
                pilot_index.append(i+1)
                
            salary = str(salaries[i])

            if i == f_number_of_employees-1:
                part1 = insert15 + first + insert2 + last + insert3 + dob + insert4 + phone + insert5 + s_num + insert6
                part2 = street + insert7 + cityID + insert8 + postID + insert9 + salary + insert10 + position + insert12
                file.write(part1 + part2 + ene)
            else:
                part1 = insert15 + first + insert2 + last + insert3 + dob + insert4 + phone + insert5 + s_num + insert6
                part2 = street + insert7 + cityID + insert8 + postID + insert9 + salary + insert10 + position + insert11
                file.write(part1 + part2 + ene)

    with open(data_path, 'w') as file:
        for i in range(0,len(pilot_index)):
            file.write(str(pilot_index[i]) + '\n')
            
    success = table_name + message
    
    return success

def pilot_insert():
    table_name = "Pilot"
    data_path = read_path + list_of_files[10]
    file_path = save_path + list_of_inserts[7]
    
    insert1 = "INSERT INTO Pilot VALUES"
    insert11 = " (''," 
    insert2 = ", " 
    insert3 = "),"
    insert4 = ");"
    
    pilot_index = [line.rstrip('\n') for line in open(data_path)]
    print("generating pilot table insert statements...")
    
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(0,len(pilot_index)):
            EID = str(pilot_index[i])
            QID = str(random.randint(1,2))
            if i == len(pilot_index)-1:
                file.write(insert11 + EID + insert2 + QID + insert4 + ene)                
            else:
                file.write(insert11 + EID + insert2 + QID + insert3 + ene)

    success = table_name + message
    
    return success    


def gen_route():
    data_path = read_path + list_of_files[11]
    airport = [line.rstrip('\n') for line in open(data_path)]
    number = random.randint(0,len(airport)-1)
    number2 = random.randint(0,len(airport)-1)
    airport_depart = airport[number]
    airport_arrival = airport[number2]
    route = [airport_depart, airport_arrival]
    return route

def route_insert():
    table_name = "Route"
    file_path = save_path + list_of_inserts[8]
    insert1 = "INSERT INTO Route VALUES"
    insert11 = "('', '"
    insert2 = "', '"
    insert3 = "'),"
    insert4 = "');"
    
    print("generating route table insert statements...")
    
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(num_of_routes):
            route = gen_route()
            airD = str(route[0])
            airA = str(route[1])
            if i == num_of_routes-1:
                file.write(insert11 + airD + insert2 + airA + insert4 + ene)
            else:
                file.write(insert11 + airD + insert2 + airA + insert3 + ene)

    success = table_name + message
    return success

def price_insert():
    table_name = "Prices"
    file_path = save_path + list_of_inserts[9]
    prices = [120, 110, 100, 200, 500]
    seat_index_from = ["NC1","NC21","NC,41","BC01","FC01",]
    seat_index_to = ["NC20", "NC40", "NC60", "BC30","FC15"]
    insert1="INSERT INTO Price VALUES"
    insert22 = "('', '" 
    insert2 ="', " 
    insert3 = ", '" 
    insert4 = "', '" 
    insert5 = "'),"
    insert6 = "');"
    
    print(ene)
    print("generating price table insert statements...")
    
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(len(prices)):
            price = str(prices[i])
            seat_num_from = seat_index_from[i]
            seat_num_to = seat_index_to[i]
            route_id = str(random.randint(1,num_of_routes))
            if i == len(prices)-1:
                file.write(insert22 + price + insert2 + route_id + insert3 + seat_num_from + insert4 + seat_num_to + insert6 + ene)
            else:
                file.write(insert22 + price + insert2 + route_id + insert3 + seat_num_from + insert4 + seat_num_to + insert5 + ene)
        
    success = table_name + message
    return success

def gen_date():
    day = random.randint(1,31)
    month = random.randint(1,12)
    year = random.randint(2019,2019)
    date = str(year) + "-" + str(month) + "-" + str(day)
    return str(date)

def gen_times(duration):
    dep_hour = random.randint(1,23)
    dep_hour1 = dep_hour
    if dep_hour1 // 10 == 0:
        dep_hour1 = "0" + str(dep_hour1)
    dep_minute = random.randrange(0,60,5)
    dep_minute1 = dep_minute
    if dep_minute // 10 == 0:
        dep_minute1 = "0" + str(dep_minute)
    second = "00"
    dep_time = str(dep_hour1) + ":" + str(dep_minute1) + ":" + second
    if duration % 60 == 0:
        arr_hour = dep_hour + (duration//60)
        if arr_hour == 24:
            arr_hour1 = 00
        if arr_hour // 10 == 0:
            arr_hour = "0" + str(arr_hour)
        arr_time = str(arr_hour) + ":" + str(dep_minute) + ":" + second
    elif duration % 60 != 0:
        arr_hour = dep_hour + (duration//60)
        if arr_hour == 24:
            arr_hour = 00
        if arr_hour // 10 == 0:
            arr_hour = "0" + str(arr_hour)
        arr_minute = abs(dep_minute + (duration%60) - 60)
        if arr_minute // 10 == 0:
            arr_minute = "0" + str(arr_minute)
        arr_time = str(arr_hour) + ":" + str(arr_minute) + ":" + second

    times = [dep_time, arr_time]
    return times

def gen_num_of_pass(plane_model):
    if plane_model == 'A318':
        num_of_pass = random.randint(66,132)
    elif plane_model == 'A319':
        num_of_pass = random.randint(80,160)
    elif plane_model == '737':
        num_of_pass = random.randint(94,188)
    elif plane_model == '205' or plane_model == '206':
        num_of_pass = 6

    return num_of_pass

def flight_insert():
    table_name = "Flight"
    file_path = save_path + list_of_inserts[10]
    insert1= "INSERT INTO Flight VALUES"
    insert11 = "('', "
    insert2 = ", " 
    insert3 = ", '"
    insert4 = "', '" 
    insert5 = "', '"
    insert6 = "', '"
    insert7 = "'),"
    insert8 = "');"
    

    print("generating flight table insert statements...")
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(num_of_flights):
            planeID = random.randint(1,num_of_planes)
            routeID = random.randint(1,num_of_routes)
            f_date = gen_date()
            duration = [60, 90, 120]
            num = random.randint(0,len(duration)-1)
            times = gen_times(duration[num])
            f_dep_time = times[0]
            f_arr_time = times[1]
            f_num_of_pass = gen_num_of_pass(p_model_list[planeID-1])
            flight_pass.append(f_num_of_pass)
            if i == num_of_flights-1:
                file.write(insert11+str(planeID)+insert2+str(routeID)+insert3+str(f_date)+insert4+str(f_dep_time)+insert5+str(f_arr_time)+insert6+str(f_num_of_pass)+insert8+ene)
            else:
                file.write(insert11+str(planeID)+insert2+str(routeID)+insert3+str(f_date)+insert4+str(f_dep_time)+insert5+str(f_arr_time)+insert6+str(f_num_of_pass)+insert7+'\n')
        
    success = table_name + message
    return success


def gen_seat_number():
    prices = [120, 110, 100, 200, 500]
    seat_index_list = ["NC", "BC", "FC"]
    num = random.randint(0,len(seat_index_list)-1)
    seat_index = seat_index_list[num]
    
    if seat_index == "NC":
        number = random.randint(1,60)
        if number < 21:
            price_id = 1
            seat_number = seat_index + str(number)
        elif number > 20 and number < 41:
            price_id = 2
            seat_number = seat_index + str(number)
        elif number > 40 and number < 61:
            price_id = 3
            seat_number = seat_index + str(number)
    elif seat_index == "BC":
        number = random.randint(1,30)
        price_id = 4
        seat_number = seat_index + str(number)
    elif seat_index == "FC":
        number = random.randint(1,15)
        price_id = 5
        seat_number = seat_index + str(number)

    seat_price =[seat_number, price_id]
    
    return seat_price

def gen_t_date():
    day = random.randint(1,31)
    month = random.randint(1,12)
    year = random.randint(2018,2019)
    date = str(year) + "-" + str(month) + "-" + str(day)
    return str(date)

def ticket_insert():
    table_name = "Ticket"
    file_path = save_path + list_of_inserts[11]
    insert1 = "INSERT INTO Ticket VALUES"
    insert11 = "('"
    insert12 = "'," 
    insert2 = ", " 
    insert3 = ", '" 
    insert4 = "', " 
    insert5 = ", '" 
    insert6 = "'),"
    insert7 = "');"
    
    print(ene)
    print("generating ticket insert statements...")
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(number_of_tickets):
            seat_price = gen_seat_number()
            pass_id = random.randint(1,num_of_passangers)
            ticket_passangers.append(pass_id)
            ticket_idi = 12345+int(i)
            ticket_id.append(ticket_idi)
            flight_id = random.randint(1,num_of_flights)
            ticket_flights.append(flight_id)
            date = gen_t_date()
            if i == number_of_tickets-1:
                file.write(insert11+str(ticket_idi) + insert12 + str(pass_id)+insert2+str(flight_id)+insert3+str(seat_price[0])+insert4+str(seat_price[1])+insert5+str(date)+insert7+ene)
            else:
                file.write(insert11+str(ticket_idi) + insert12 + str(pass_id)+insert2+str(flight_id)+insert3+str(seat_price[0])+insert4+str(seat_price[1])+insert5+str(date)+insert6+ene)
        
    success = table_name + message
    return success



def reservation_insert():
    table_name = "Reservations"
    file_path = save_path + list_of_inserts[12]
    insert1 = "INSERT INTO Reservations VALUES"
    insert11 = " (''," 
    insert2=", " 
    insert3 = ", " 
    insert4= ", '"
    insert5 = "'),"
    insert6 = "');"
    res_status = ["Booked", "Paid", "Cancelled"]

    print(ene)
    print("generating reservation table insert statements...")   
    with open(file_path, 'w') as file:
        file.write(insert1 + ene)
        for i in range(number_of_tickets):
            pass_id = ticket_passangers[i]
            flight_id = ticket_flights[i]
            res_ticket_id = ticket_id[i]
            num = random.randint(0,2)
            status = res_status[num]
            if i == number_of_tickets - 1:
                file.write(insert11 + str(pass_id) + insert2 + str(flight_id) + insert3 + str(res_ticket_id) + insert4 + str(status) + insert6 + ene)
            else:
                file.write(insert11 + str(pass_id) + insert2 + str(flight_id) + insert3 + str(res_ticket_id) + insert4 + str(status) + insert5 + ene)
                
            
    success = table_name + message
    return success

##########################################################################################
############################ FILE MERGNG SECTION #########################################
##########################################################################################

def first_merge():
    country = [line for line in open(save_path+list_of_inserts[0])]
    city = [line for line in open(save_path+list_of_inserts[1])]
    postcode_air = [line for line in open(save_path+list_of_inserts[2])]

    with open("_1_ insert.sql", "w") as file:
        for i in range(len(country)):
            file.write(country[i])
        for i in range(len(city)):
            file.write(city[i])
        for i in range(len(postcode_air)):
            file.write(postcode_air[i])

    mess = "Merging complete!!!"
    return mess                       

def second_merge():
    postcode = [line for line in open(save_path+list_of_inserts[3])]
    p_model = [line for line in open("program_data\\6 insert statements for plane model table.txt")]
    plane = [line for line in open(save_path+list_of_inserts[5])]
    qualification = [line for line in open("program_data\\8 insert statements for qualifications table.txt")]
    passanger = [line for line in open(save_path+list_of_inserts[4])]
    employee = [line for line in open(save_path+list_of_inserts[6])]
    pilot = [line for line in open(save_path+list_of_inserts[7])]
    route = [line for line in open(save_path+list_of_inserts[8])]
    price = [line for line in open(save_path+list_of_inserts[9])]
    flight = [line for line in open(save_path+list_of_inserts[10])]
    ticket = [line for line in open(save_path+list_of_inserts[11])]
    reservation = [line for line in open(save_path+list_of_inserts[12])]
    
    with open("_2_ insert.sql", "w") as file:
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

    mess = "Merging complete!!!"
    return mess

def gen_readme():
    readme = '''

    1. open phpMyAdmin
    2. import JetAirDB DML Code.sql
    3. go to database JetAirDB
    4. import file __1__insert.sql
    6. before pressing GO to import file, unmark 'DO NOT use AUTO_INCREMENT for zero values"
    7. go to table airports and import 4 airports.csv
    7. go back to database JetAirDB main window
    8. import file __2__insert.sql
    9. before pressing GO to import file, unmark 'DO NOT use AUTO_INCREMENT for zero values"
    10. Enjoy your populated table


    '''

    with open("README.txt","w") as file:
        file.write(readme)

    return "readme file generated"



##########################################################################################
############################## EXECUTION SECTION #########################################
##########################################################################################

while True:

    print(make_country_insert())
    print(make_city_insert())
    print(postcode_airport())
    print(ene)
    num_of_postcodes = int(input("please enter the number of postcodes: "))
    print(postcode_insert())
    p_model_list = []
    print(ene)
    num_of_planes = int(input("how many planes does airline have: "))
    print(plane_insert())
    num_of_pilots = (num_of_planes * 2) + 4
    num_of_flight_att = (num_of_planes * 3) + 6
    num_of_ticket_a = (num_of_planes) + 3
    s_number_of_employees = num_of_pilots + num_of_flight_att + num_of_ticket_a
    if s_number_of_employees // 20 == 0:
        num_of_managers = 1
    else:
        num_of_managers = s_number_of_employees // 20
        
    f_number_of_employees = s_number_of_employees + num_of_managers
    print(employee_insert())
    print(pilot_insert())
    print(ene)
    num_of_routes = int(input("How many routes AirLine has? "))
    print(route_insert())
    print(price_insert())
    print("number of flights is double number of routes")
    num_of_flights = num_of_routes*2
    flight_pass = []
    print(ene)
    print("generating " + str(num_of_flights) + " flights")
    print(flight_insert())
    num_flight_pass = 0
    for i in range(len(flight_pass)):
        num_flight_pass += flight_pass[i]
    num_of_passangers = num_flight_pass // 2
    print(ene)
    print("generating " + str(num_of_passangers) + " passangers")
    print(passanger_insert())
    number_of_tickets = num_flight_pass // (num_of_planes*2)
    ticket_flights = []
    ticket_passangers = []
    ticket_id = []
    print(ticket_insert())
    print(reservation_insert())
    print(ene)
    print("Files merging...")
    print(first_merge())
    print("Files merging...")
    print(second_merge())
    print(ene)
    print("Generating readme file...")
    print(gen_readme())



    print(ene)
    print("##################################################")
    print(ene)        
    print('''
            GENERATING FILES COMPLETE PLEASE FOLLOW
            THE INSTRUCTIONS IN FILE 'README.txt'
    ''')
    print(ene)
    print("##################################################")
    print(ene)

    end_program = input("press enter to exit! ")
    if not end_program:
        break
    else:
        break

##########################################################################################
##########################################################################################
################################# CODE END ###############################################
##########################################################################################
##########################################################################################
