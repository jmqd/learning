// Unit.h
#ifndef Unit_H
#define Unit_H

class Unit: public Dwelling
{

public:
    std::vector<Resident> get_residents();
    Policy get_policy();
    bool is_smoking;
    bool is_pet_friendly;
    Floor get_floor();
    ApartmentBuilding get_building();
    int max_capacity();
    int get_room_count();
    bool is_furnished;
private:
    std::vector<Resident> residents;
    Policy policy;
    Floor floor;
    ApartmentBuilding building;
    int max_capacity;
    int room_count;
}
