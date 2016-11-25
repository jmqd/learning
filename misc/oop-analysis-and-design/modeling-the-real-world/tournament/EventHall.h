// EventHall.h
#ifndef EventHall_H
#define EventHall_H

class EventHall: public AbstractRoom
{

public:
    float get_square_footage();
    int get_maximum_person_capacity();
    Venue get_venue();
private:
    float square_footage();
    int maximum_person_capacity;
    Venue venue;
