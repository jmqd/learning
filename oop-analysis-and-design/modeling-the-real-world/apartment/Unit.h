// Floor.h
#ifndef Floor_H
#define Floor_H

class Floor
{

public:
    std::vector<Unit> get_units();
    std::vector<int> get_unit_numbers();
    float get_ceiling_height();
    // floor number relative to ground (floor number 0)
    int get_number();
private:
    std::vector<Unit> units;
    std::vector<int> unit_numbers;
    int floor_number;
    float ceiling_height;
}
