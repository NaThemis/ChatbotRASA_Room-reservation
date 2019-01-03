import mysql.connector
from datetime import datetime, time
import dateparser
import pendulum
import string
import dateutil.parser
from robot.libraries.DateTime import convert_time

# function to return a tuple from the pendulum object type
def from_pendulum_to_tupple(date):
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    return (year, month, day, hour, minute)

# function to check if the room asked is free while looking in the database
def is_the_room_available(name_room, day_only, day_startinghour, day_ending_hour, cnx):

    # variables
    starting_hour_list = []
    ending_hour_list = []
    room_list = []

    #cursor
    cur_select_all = cnx.cursor(buffered=True)
    query_select_all = ("SELECT * FROM reservations")
    cur_select_all.execute(query_select_all)

    # convert the entry starting and ending meeting hour to a tupple
    asked_starting_hour = from_pendulum_to_tupple(day_startinghour)
    asked_ending_hour = from_pendulum_to_tupple(day_ending_hour)

    # select all the name room, starting and ending meeting hour and append them to a list
    for i in cur_select_all:
        room_list.append(i[1])
        starting_hour_list.append(from_pendulum_to_tupple(pendulum.parse(i[2])))
        ending_hour_list.append(from_pendulum_to_tupple(pendulum.parse(i[3])))

    # loop thru a list
    # if the asked room is equal to the room in the list
    # and if the asked_starting_hour and asked_ending_hour
    # are between the lists values return False else return True
    for i in range(len(starting_hour_list)):
        if name_room == room_list[i]:
            #print('is the same room')
            if starting_hour_list[i] <= asked_starting_hour <= ending_hour_list[i]:
                #print('starting hour is between')
                return False
            if starting_hour_list[i] <= asked_ending_hour <= ending_hour_list[i]:
                #print('ending hour is between')
                return False

    return True

# main function
def make_a_booking(name_room, day, hour_start, duration):

    # connect to the localhost database
    cnx = mysql.connector.connect(password='jeb41jeb', user="root", database="alex")

    #day_only : get the parsed date
    day_only = str(dateparser.parse(day).date())

    # parse the hour in string inputed by the user and convert it the a pendulum object
    hour_start_parsed = dateutil.parser.parse(hour_start, fuzzy_with_tokens=True)
    pendulum_combined_day_and_hour_start = pendulum.parse(str(day_only) + " " + hour_start, strict=False)

    # convert the duration in string inputed by the user and to seconds then in minutes
    duration_in_seconds = convert_time(duration)
    duration_in_minutes = duration_in_seconds / 60

    # add the duration_in_minutes to the starting hour to get the hour start pendulum object
    pendulum_combined_day_and_hour_end = pendulum_combined_day_and_hour_start.add(minutes = duration_in_minutes)
    #print(pendulum_combined_day_and_hour_end)

    # check if the room is available
    room_available = is_the_room_available(name_room, day_only, pendulum_combined_day_and_hour_start, pendulum_combined_day_and_hour_end, cnx)


    #if the room isn't available return False
    # else make the insert intro the database and return True
    if room_available == False:
        print('Oh wait ..., I just checked and unfortunately this room is not available :-(')
        return False
    else:
        print('Hey, I just checked and the room is available :-)')
        cur_insert_entry = cnx.cursor(buffered=True)
        query_insert_one = "INSERT INTO reservations (name_room, hour_start, hour_end) VALUES ('%s', '%s', '%s' );" % (name_room, pendulum_combined_day_and_hour_start, pendulum_combined_day_and_hour_end)
        #print(" the query is " + str(query_insert_one))
        cur_insert_entry.execute(query_insert_one)
        cnx.commit()
        cur_insert_entry.close()
        cnx.close()
        return True


# function to clean the database
def clean_the_data_base():
    cnx_delete = mysql.connector.connect(password='jeb41jeb', user="root", database="alex")
    cur_delete = cnx_delete.cursor(buffered=True)
    delete_query = ("DELETE FROM reservations")
    cur_delete.execute(delete_query)
    cnx_delete.commit()
    cur_delete.close()
    cnx_delete.close()

# print all the entries of the database
def print_all():
    cnx_for_select_all = mysql.connector.connect(password='jeb41jeb', user="root", database="alex")
    cur_select_all = cnx_for_select_all.cursor(buffered=True)
    query_select_all = ("SELECT * FROM reservations")
    cur_select_all.execute(query_select_all)
    #for i in cur_select_all:
        #print(i)
    cur_select_all.close()



#clean_the_data_base()


#make_a_booking("green", "today", "14h", "45min")
#make_a_booking("red", "tomorrow", "16h30", "1h45min")


#print('print all the values')
#print_all()
