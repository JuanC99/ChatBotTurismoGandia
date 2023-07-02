# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (EventType)
import random

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        dt = datetime.now()
        print('Datetime is:', dt)
        print('day Name:', dt.strftime('%A'))
        dispatcher.utter_message(text="Hello World!, today is: {}".format(dt.strftime('%A')))

        return []

class ActionRecomendarTurismo(Action):

    def name(self) -> Text:
        return "action_recomendar_turismo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        listaSitiosTuristicosGandia = [
                ("utter_responderExplicacionCastilloBayren","utter_turismo/preguntarPorReservaCastilloBairen"),
                ("utter_responderExplicacionCuevaParapello","utter_turismo/preguntarPorReservaCuevaParpallo"),
                ("utter_responderExplicacionRefugioAntiaeresos","utter_turismo/preguntarPorVisitaRefugiosAntiaereos")
                ]
        nRandom = random.randint(0, len(listaSitiosTuristicosGandia) - 1)
        #dispatcher.utter_message(response="utter_responderRecomendacion") #Aqui tienes mi recomendacion de hoy!
        for elemento in listaSitiosTuristicosGandia[nRandom]:
            dispatcher.utter_message(response=elemento)
        return []