from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from booking import make_a_booking
import mysql.connector



class ActionRoom(Action):

    def name(self):
        return 'action_room'

    def run(self, dispatcher, tracker, domain):
        
        name_room = tracker.get_slot('name_room')
        day = tracker.get_slot('day')
        hour_start = tracker.get_slot('hour_start')
        duration = tracker.get_slot('duration')
        
        booking_answer = make_a_booking(name_room, day, hour_start, duration)
        
        if booking_answer:
            booking_answer = 'The reservation has been made'
        else:
            booking_answer = 'The room is taken at this hour'
        
        response = """You want to book the {} room is booked on {} at {} for {}. Is it correct ?""".format(name_room, day, hour_start, duration)
        
        name_room = str(name_room)
        day = str(day)
        hour_start = str(hour_start)
        duration = str(duration)
        
        #SQL queries#
        cnx = mysql.connector.connect(password='root', user="root", database="alex")
             

        dispatch = dispatcher.utter_message(response)
        dispatch = dispatcher.utter_message(str(booking_answer))
        
        return dispatch
    
        
