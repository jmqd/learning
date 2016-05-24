#include <iostream>
#include <string>
using std::cout;
using std::endl;

int main()
{
    std::string name;
    std::cout << "What is your name, weary traveler?\n> ";
    std::getline (std::cin, name); 
    std::cout << "\nhello, " << name << "!" << endl;
    return 0;
}
