# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import arrow
import dateparser
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



class ActionGetNearestStation(Action):

    def name(self) -> Text:
        return "Action_Get_Nearest_Station"  

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I am fetching the nearest station information.")
        dispatcher.utter_message(text=".")
        dispatcher.utter_message(text=".")
        dispatcher.utter_message(text="done.")
        return []
    

class ActionToStation(Action):

    def name(self) -> Text:
        return "Action_To_Charging_Station" 
    

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        station = list(tracker.get_latest_entity_values("place"))

        if station:
            
            station_name = station[0]  
            dispatcher.utter_message(text=f"I understand. Taking you to the {station_name} charging station.")
        else:
            
            dispatcher.utter_message(text="i did not extract a location")
        
        return []