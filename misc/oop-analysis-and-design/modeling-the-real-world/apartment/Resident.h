// Resident.h
#ifndef Resident_H
#define Resident_H

class Resident: public AbstractPerson
{

public:
    std::vector<Unit> get_unit_number();
    int get_remaining_lease_duration();
    int get_length_of_residency();
    std::vector<array> get_payment_history();
    std::vector<Resident> get_roommates();
    std::vector<Pet> get_pets();
    Unit get_unit();
    Contact get_emergency_contact();
    float get_balance_owed();
    float get_ceiling_height();
    // floor number relative to ground (floor number 0)
    int get_number();
private:
    std::vector<Unit> units;
    std::vector<int> unit_numbers;
    int floor_number;
    float ceiling_height;
}
