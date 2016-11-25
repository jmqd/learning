// AbstractPerson.h
#ifndef AbstractPerson_H
#define AbstractPerson_H

class AbstractPerson
{

public:
    int get_age();
    std::string get_first_name();
    std::string get_last_name();
    std::string get_email()
    std::string get_birthdate();
    std::string get_next_birthday();
private:
    date birthday;
    std::string email;
    std::string first_name;
    std::string last_name;
    std::string gender;
    Address address;
}
