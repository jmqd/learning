// Building.h
#ifndef Building_H
#define Building_H

class Building
{

public:
    string get_name();
    string get_owner();
    string get_address();
    string get_city();
    string get_state();
    string get_zip();
    string has_roof();
    std::vector<Floors> get_floors();
    std::vector<int> get_room_numbers();
    std::vector<Staff> get_staff();
private:
    Staff staff;
    Address address;
    Policy policy;
    std::vector<Floors> floors;
    std::vector<Resident> residents;
    string name;
    string owner;
    Staff staff;
}
