from datetime import date
from typing import Any, Text, Dict, List
import sqlite3
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormAction


class ActionConfirmShowOneTechno(FormAction):
    
    def name(self) -> Text:
        return "action_confirm_show_one_techno"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["techno_type"]


    def submit(self,
               dispatcher: "CollectingDispatcher",
               tracker: "Tracker",
               domain: "DomainDict",
        ) -> List[Dict]:
        
        techno_type = tracker.get_slot('techno_type')
        print(techno_type)

        message_to_user = f"Ok Great. Your want to know about {techno_type}. Can you please confirm ?"

        dispatcher.utter_message(text=message_to_user)
        return []


class ActionShowtechnos(Action):

    def name(self) -> Text:
        return "action_show_technos"

    def run(self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        conn = sqlite3.connect('developpers.db')
        query = "select * from technos;"
        df = pd.read_sql(query, conn)

        str((tracker.latest_message)['text'])
        dispatcher.utter_message(response="utter_list_technos")

        for index, row in df.iterrows():
            content = f"{row['name']} which is of type {row['type']}."
            dispatcher.utter_message(text=content)

        return []


class ActionShowDeveloppers(Action):

    def name(self) -> Text:
        return "action_show_developpers"

    def run(self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        conn = sqlite3.connect('developpers.db')
        query = "select * from developpers;"
        df = pd.read_sql(query, conn)

        str((tracker.latest_message)['text'])
        dispatcher.utter_message(response="utter_list_developpers")

        for index, row in df.iterrows():
            content = f"{row['first_name']} {row['last_name']} works on {row['techno']} and has {row['experience']} years of experience."
            dispatcher.utter_message(text=content)

        return []





















