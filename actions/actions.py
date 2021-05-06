from datetime import date
from typing import Any, Text, Dict, List
import sqlite3
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionShowOneTechno(Action):
    
    def name(self) -> Text:
        return "action_show_one_techno"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["techno_type"]


    def run(self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        techno_type = tracker.get_slot('techno_type')

        message_to_user = f"Voici la liste des developpeurs qui travaillent sur {techno_type}."
        dispatcher.utter_message(text=message_to_user)

        conn = sqlite3.connect('developpers.db')
        query = f"select * from developpers where techno= '{techno_type}';"
        df = pd.read_sql(query, conn)

        for index, row in df.iterrows():
            content = f"{row['first_name']} {row['last_name']} a {row['experience']} années d'experience."
            dispatcher.utter_message(text=content)
        
        return []


class ActionConfirmShowOneTechno(Action):
    
    def name(self) -> Text:
        return "action_confirm_show_one_techno"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["techno_type"]


    def run(self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        techno_type = tracker.get_slot('techno_type')
        print(techno_type)

        message_to_user = f"Ok super. Vous souhaitez en savoir plus sur {techno_type}. Pouvez-vous confirmer svp ?"

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
            content = f"{row['name']} qui est une technologie {row['type']}."
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
            content = f"{row['first_name']} {row['last_name']} travaille sur {row['techno']} et a {row['experience']} années d'experience."
            dispatcher.utter_message(text=content)

        return []





















