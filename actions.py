# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []

class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("restaurant_type", None), SlotSet("party_size_number", None), SlotSet("city", None), SlotSet("timeRange", None)]

class ReservationForm(FormAction):

    def name(self) -> Text:
        return "reservation_form"
    @staticmethod
    def required_slots(tracker : Tracker) -> List[Text]:
        return ["restaurant_type", "party_size_number", "city", "timeRange"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "restaurant_type" : self.from_entity(
                entity="restaurant_type",
                intent=["book_reservation", "inform"]
            ),
            "party_size_number" : self.from_entity(
                entity="party_size_number",
                intent=["book_reservation", "inform"]
            ),
             "city" : self.from_entity(
                entity="city",
                intent=["book_reservation", "inform"]
            ),
            "timeRange" : self.from_entity(
                entity="timeRange",
                intent=["book_reservation", "inform"]
            )}
            
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        _restuarant_type = tracker.get_slot("restaurant_type")
        _party_size_number = tracker.get_slot("party_size_number")
        _city = tracker.get_slot("city")
        _timeRange = tracker.get_slot("timeRange")
        # utter confirmation
        dispatcher.utter_message("I have booked you a {} in {} for {} people at {}.".format(_restuarant_type, _city, _party_size_number , _timeRange))
        return []