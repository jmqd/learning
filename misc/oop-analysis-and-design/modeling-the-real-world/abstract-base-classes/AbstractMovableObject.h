// AbstractMovableObject.h
#ifndef AbstractMovableObject_H
#define AbstractMovableObject_H

class AbstractMovableObject: public AbstractPhysicalObject
{

Public:
    std::vector<float> get_acceleration();
    // return three component vector, [Vx, Vy, Vz]
    std::vector<float> get_velocity();
    // return three component force vector, [Fx, Fy, Fz]
    std::vectory<float> get_forces();
    float get_drag_coefficient();
    float get_rolling_resistance_coefficient();
    float get_friction_coefficient();
Private:
    std::vector<float> velocity;
    std::vector<float> aceleration;
    std::vector<float> force;
    float drag_coefficient;
    float power;
    float rolling_resistance_coefficient;
    float friction_coefficient;
}
