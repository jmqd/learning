// AbstractBuilding.h
#ifndef Venue_H
#define Venue_H

class Venue: public AbstractBuilding
{

public:
    std::string get_name();
    std::string get_owner();
    std::string get_address();
    std::string get_city();
    std::string get_state();
    std::string get_zip();
    int get_assessment();
    EventHall get_main_event_space();
    std::vector<Floors> get_floors();
    std::vector<int> get_room_numbers();
private:
    Address address;
    int assessment;
    EventHall main_event_space;
    date built;
    std::vector<Floors> floors;
    std::vector<Resident> residents;
    std::string name;
    std::string owner;
    Staff staff;
}
