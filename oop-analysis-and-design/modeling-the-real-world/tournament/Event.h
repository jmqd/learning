// Event.h
#ifndef Event_H
#define Event_H

class Event
{

public:
    std::vector<Paricipant> get_participants();
    std::vector<Arbiter> get_arbiters();
    std::vector<Round> get_rounds();
    std::string get_name();
    Round get_current_round();
    DateTime get_start_time();
private:
