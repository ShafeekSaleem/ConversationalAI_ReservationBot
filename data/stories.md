## reservation_happy_path
* greet
    - utter_greet
* mood_great
    - utter_ask_name
* inform{"name": "Peter"}
    - slot{"name": "Peter"}
    - action_set_name_obtained_slot
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


## greeting_name
* greet
    - utter_greet
* mood_great
    - utter_ask_name


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

## interactive_story_2
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

## interactive_story_3
* greet
    - utter_greet
* mood_great
    - utter_ask_happy_help
* ask_purpose
    - utter_purpose
* ask_howold
    - utter_howold
* ask_whatismyname
    - slot{"is_name_obtained": "not_recieved"}
    - utter_not_knowing_name
    - utter_ask_name
* inform{"name": "Shafeek"}
    - slot{"name": "Shafeek"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* ask_whatismyname
    - slot{"is_name_obtained": "name_recieved"}
    - utter_whatismyname
* book_reservation{"restaurant_type": "restaurant"}
    - slot{"restaurant_type": "restaurant"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"requested_slot": "party_size_number"}
* form: inform{"party_size_number": "7"}
    - slot{"party_size_number": "7"}
    - form: reservation_form
    - slot{"party_size_number": "7"}
    - slot{"requested_slot": "city"}
* form: inform{"spatial_relation": "near", "city": "Dehiwala"}
    - slot{"city": "Dehiwala"}
    - form: reservation_form
    - slot{"city": "Dehiwala"}
    - slot{"requested_slot": "timeRange"}
* form: inform{"timeRange": "March 7th"}
    - slot{"timeRange": "March 7th"}
    - form: reservation_form
    - slot{"timeRange": "March 7th"}
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


## interactive_story_4
* greet
    - utter_greet
* mood_great
    - utter_ask_name
* inform{"name": "Shafeek"}
    - slot{"name": "Shafeek"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* ask_whatismyname
    - slot{"is_name_obtained": "name_recieved"}
    - utter_whatismyname
* book_reservation{"restaurant_type": "restaurant"}
    - slot{"restaurant_type": "restaurant"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"requested_slot": "party_size_number"}
* form: inform{"party_size_number": "7"}
    - slot{"party_size_number": "7"}
    - form: reservation_form
    - slot{"party_size_number": "7"}
    - slot{"requested_slot": "city"}
* form: inform{"spatial_relation": "near", "city": "Dehiwala"}
    - slot{"city": "Dehiwala"}
    - form: reservation_form
    - slot{"city": "Dehiwala"}
    - slot{"requested_slot": "timeRange"}
* form: inform{"timeRange": "March 7th"}
    - slot{"timeRange": "March 7th"}
    - form: reservation_form
    - slot{"timeRange": "March 7th"}
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


## interactive_story_5
* greet
    - utter_greet
* mood_great
    - utter_ask_name
* affirm{"name": "John"}
    - slot{"name": "John"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* book_reservation{"restaurant_type": "pub", "city": "Kandy", "party_size_number": "3"}
    - slot{"city": "Kandy"}
    - slot{"party_size_number": "3"}
    - slot{"restaurant_type": "pub"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "pub"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Kandy"}
    - slot{"restaurant_type": "pub"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Kandy"}
    - slot{"requested_slot": "timeRange"}
* form: inform{"timeRange": "midnight"}
    - slot{"timeRange": "midnight"}
    - form: reservation_form
    - slot{"timeRange": "midnight"}
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

## interactive_story_6
* greet
    - utter_greet
* mood_great
    - utter_ask_happy_help
* ask_whatismyname
    - slot{"is_name_obtained": "not_recieved"}
    - utter_not_knowing_name
    - utter_ask_name
* inform{"name": "Shafeek"}
    - slot{"name": "Shafeek"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* book_reservation{"restaurant_type": "restaurant", "city": "Colombo", "party_size_number": "3", "timeRange": "midnight"}
    - slot{"city": "Colombo"}
    - slot{"party_size_number": "3"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"timeRange": "midnight"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Colombo"}
    - slot{"timeRange": "midnight"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Colombo"}
    - slot{"timeRange": "midnight"}
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

## interactive_story_7
* book_reservation{"restaurant_type": "restaurant", "party_size_number": "3", "city": "Allison", "timeRange": "midday"}
    - slot{"city": "Allison"}
    - slot{"party_size_number": "3"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"timeRange": "midday"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Allison"}
    - slot{"timeRange": "midday"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Allison"}
    - slot{"timeRange": "midday"}
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
    - utter_happy
* ask_whatismyname
    - slot{"is_name_obtained": "not_recieved"}
    - utter_not_knowing_name
    - utter_ask_name
* inform{"name": "Ken"}
    - slot{"name": "Ken"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* ask_whatismyname
    - slot{"is_name_obtained": "name_recieved"}
    - utter_whatismyname
* affirm
    - utter_ask_happy_help
* deny
    - utter_happy
    - utter_goodbye
* goodbye

## interactive_story_8_name
* greet
    - utter_greet
* mood_great
    - utter_ask_happy_help
* ask_whatismyname
    - slot{"is_name_obtained": "not_recieved"}
    - utter_not_knowing_name
    - utter_ask_name
* inform{"name": "Shafeek"}
    - slot{"name": "Shafeek"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* book_reservation{"restaurant_type": "restaurant", "party_size_number": "3", "city": "Kandy", "timeRange": "midday"}
    - slot{"city": "Kandy"}
    - slot{"party_size_number": "3"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"timeRange": "midday"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Kandy"}
    - slot{"timeRange": "midday"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "3"}
    - slot{"city": "Kandy"}
    - slot{"timeRange": "midday"}
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
    - utter_happy
* ask_whatismyname
    - slot{"is_name_obtained": "name_recieved"}
    - utter_whatismyname
* affirm
    - utter_ask_happy_help
* deny
    - utter_happy
    - utter_goodbye
* goodbye


## whatismyname_path
* ask_whatismyname
    - slot{"name": "not_recieved"}
    - utter_not_knowing_name
    - utter_ask_name
* inform{"name": "John"}
    - slot{"name": "John"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help

## inform_name_path
* greet
    - utter_greet
* mood_great
    - utter_ask_name
* inform{"name": "Billa"}
    - slot{"name": "Billa"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help

## inform_name_path2
* greet
    - utter_greet
* mood_great
    - utter_ask_name
* inform{"name": "Morgan"}
    - slot{"name": "Morgan"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* ask_whatismyname
    - slot{"is_name_obtained": "name_recieved"}
    - utter_whatismyname
* affirm
    - utter_ask_happy_help
## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_ask_name
* inform{"name": "Hendry"}
    - slot{"name": "Hendry"}
    - action_set_name_obtained_slot
    - utter_ask_happy_help
* book_reservation{"restaurant_type": "restaurant", "city": "Kandy", "party_size_number": "6"}
    - slot{"city": "Kandy"}
    - slot{"party_size_number": "6"}
    - slot{"restaurant_type": "restaurant"}
    - reservation_form
    - form{"name": "reservation_form"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "6"}
    - slot{"city": "Kandy"}
    - slot{"restaurant_type": "restaurant"}
    - slot{"party_size_number": "6"}
    - slot{"city": "Kandy"}
    - slot{"requested_slot": "timeRange"}
* form: inform{"timeRange": "4 O'clock"}
    - slot{"timeRange": "4 O'clock"}
    - form: reservation_form
    - slot{"timeRange": "4 O'clock"}
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
    - utter_happy
* ask_whatismyname
    - slot{"is_name_obtained": "name_recieved"}
    - utter_whatismyname
* affirm
    - utter_ask_happy_help
