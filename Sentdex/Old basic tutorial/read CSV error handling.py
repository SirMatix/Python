import csv

#csv - comma separated variables

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    dates = []
    colors = []

    for row in readCSV:
        color = row[7]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input('What color do you want to know the date from? ')

        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of', whatColor, 'is', theDate, sep=' ')
        else:
            print('Color not found, or is not a color')

    # except Exception, e: - python 2.7 
    except Exception as e:
        print(e)

    print('continuing')
        
