// Round.h
#ifndef Round_H
#define Round_H

class Round
{

public:
    Event get_event();
    int get_round_number();
    int get_participant_count();
    std::vector<Match> get_matches();
    std::vector<Participant> get_participants();
private:
