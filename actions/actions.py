from datetime import date
from typing import Any, Text, Dict, List
import sqlite3
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionFinalizeAppDetail(Action):

    def name(self) -> Text:
        return "action_finalize_app_details"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["application_type"]

    def run(self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        application_type = tracker.get_slot('application_type')
        techno_type = tracker.get_slot('techno_type')

        message_to_user = f"Vous souhaitez donc une application {application_type} réalisée en {techno_type}. "
        
        message_to_user += f"Nous serons plus que ravis de réaliser ce site web pour vous!!"
        dispatcher.utter_message(text=message_to_user)

        return []



class ActionConfirmWebSite(Action):
    
    def name(self) -> Text:
        return "action_confirm_web_sites"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["application_type"]


    def run(self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        application_type = tracker.get_slot('application_type')
        search = 'mobile'
        message_to_user = f"Ok super. "
        message_to_user += f"Vous souhaitez réaliser une application {application_type}. "
        message_to_user += f"Voici les technos permettant de le faire :"
        dispatcher.utter_message(text=message_to_user)

        query = f"""
            SELECT * FROM technos
            WHERE type = '{application_type}';
        """
        conn = sqlite3.connect('developpers.db')
        df = pd.read_sql(query, conn)

        for index, row in df.iterrows():
            content = f"{row['name']}"
            dispatcher.utter_message(text=content)

        dispatcher.utter_message(text="Sur laquelle de ces technos souhaitez-vous voir votre site réalisée?")

        return []



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
        query = f"""
            SELECT * FROM developpers 
            JOIN technos ON developpers.id_techno = technos.id_techno 
            WHERE name = '{techno_type}';
        """
        df = pd.read_sql(query, conn)

        for index, row in df.iterrows():
            content = f"{row['first_name']} {row['last_name']} a {row['experience']} années d'experience."
            dispatcher.utter_message(text=content)
        
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

        query = f"""
            SELECT * FROM developpers 
            JOIN technos ON developpers.id_techno = technos.id_techno;
        """


        df = pd.read_sql(query, conn)

        str((tracker.latest_message)['text'])
        dispatcher.utter_message(response="utter_list_developpers")

        for index, row in df.iterrows():
            content = f"{row['first_name']} {row['last_name']} travaille sur {row['name']} et a {row['experience']} années d'experience."
            dispatcher.utter_message(text=content)

        return []





















