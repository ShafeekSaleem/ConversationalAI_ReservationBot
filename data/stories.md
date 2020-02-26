## reservation_happy_path
* greet
  - utter_greet
* mood_great
  - utter_ask_happy_help
* book_reservation
  - reservation_form
  - form{"name":"reservation_form"}
  - form{"name":null}
  - utter_ask_correctness
* affirm
  - action_reset_slot
  - utter_happy
  - utter_goodbye

## reservation_happy_path_2
* book_reservation
  - reservation_form
  - form{"name":"reservation_form"}
  - form{"name":null}
  - utter_ask_correctness
* affirm
  - action_reset_slot
  - utter_happy
* goodbye
  - utter_goodbye

## greeting_happy
* greet
  - utter_greet
* mood_great
  - utter_ask_happy_help


## greeting_sad
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_sad_help

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* chitchat
    - utter_ask_for_relevent
* ask_purpose
    - utter_purpose
* bot_challenge
    - utter_iamabot
* stop

## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_ask_happy_help
* ask_purpose
    - utter_purpose
* book_reservation{"restaurant_type": "bakery"}
    - slot{"restaurant_type": "bakery"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "bakery"}
    - slot{"restaurant_type": "bakery"}
    - slot{"requested_slot": "party_size_number"}
* form: inform{"party_size_number": "7"}
    - slot{"party_size_number": "7"}
    - form: reservation_form
    - slot{"party_size_number": "7"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "Kolannawa"}
    - slot{"city": "Kolannawa"}
    - form: reservation_form
    - slot{"city": "Kolannawa"}
    - slot{"requested_slot": "timeRange"}
* form: inform{"timeRange": "6 O'clock"}
    - slot{"timeRange": "6 O'clock"}
    - form: reservation_form
    - slot{"timeRange": "6 O'clock"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_correctness
* affirm
    - action_reset_slot
    - slot{"restaurant_type": null}
    - slot{"party_size_number": null}
    - slot{"city": null}
    - slot{"timeRange": null}
    - utter_did_that_help
* affirm
    - utter_goodbye
* goodbye
