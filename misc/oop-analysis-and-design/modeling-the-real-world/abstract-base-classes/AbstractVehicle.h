// AbstractVehicle.h
#ifndef AbstractVehicle_H
#define AbstractVehicle_H

class AbstractVehicle: public AbstractMovableObject
{

Public:
    std::string get_energy_type();
    int get_person_capacity();
    float get_power();
    float get_rolling_resistance_coefficient();
    float get_friction_coefficient();
Private:
    // e.g. hybrid, petrol, electric, nuclear, hydrogen, etc.
    std:string energy_type;
    int person_capacity;
    float power;
    float rolling_resistance_coefficient;
    float friction_coefficient;
}
