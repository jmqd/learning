// Participant.h
#ifndef Participant_H
#define Participant_H

class Participant: public AbstractPerson
{

public:
    Event get_current_event();
    int get_player_id();
    std::vector<Event> get_enrolled_events();
    EventRecord get_event_record();


private:
    Event current_event;
    std::vector<Event> enrolled_events;
    int player_id;

}
