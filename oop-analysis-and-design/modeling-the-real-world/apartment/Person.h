// Person.h
#ifndef Person_H
#define Person_H

class AbstractPerson
{

public:
    int get_age();
    string get_first_name();
    string get_last_name();
    string get_email()
private:
    int birth_year;
    int birth_day;
    int birth_month;
    string email;
    string first_name;
    string last_name;
    string gender;
    Address address;
}
