// AbstractPhysicalObject.h
#ifndef AbstractPhysicalObject_H
#define AbstractPhysicalObject_H

class AbstractPhysicalObject
{

Public:
    float get_mass();
    float get_height();
    float get_width();
    float get_length();
    float get_volume();
    std::vector<float> get_position();
Private:
    float mass;
    float height;
    float width;
    float length;
    float volume;
    std::vector<float> position;
}
