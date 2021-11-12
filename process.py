log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)
#1 the first line of code is to accesss the information in  file because we already opened it on line 1
#2 the .strip is deleting all the white space from the information we are accessing in um-server-01-txt
#3 the day is to get the day you want and for that day we want to grab information from the 0 index to the 3rd
#4 if the day is tuesdday then grab the information from inndex 0 to 3 and store all that data
#5 print is to see the data you want back in the console.