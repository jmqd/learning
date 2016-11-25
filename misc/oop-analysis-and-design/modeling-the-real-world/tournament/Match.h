// Match.h
#ifndef Match_H
#define Match_H

class Match
{

public:
    Round get_round();
    std::vector<Participant> get_participants();
    int get_table_number();
    int get_wins();
    int get_draws();
    Participant get_winner();
    bool is_featured();
private:
