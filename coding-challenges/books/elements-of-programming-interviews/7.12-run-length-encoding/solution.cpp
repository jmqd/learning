#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

string RunLengthEncode(const string &bytes_to_encode) {
  std::string::const_iterator iterator = bytes_to_encode.cbegin();
  string encoded_string = "";

  while (iterator != bytes_to_encode.end()) {
    char prev_c = *iterator;
    int running_count = 0;

    while (prev_c == *iterator) {
      ++running_count;
      ++iterator;
    }

    encoded_string += std::to_string(running_count) + prev_c;
    }
  return encoded_string;
}

string RunLengthDecode(const string &rle_encoded_string) {
  std::string::const_iterator iterator = rle_encoded_string.cbegin();
  string decoded_string = "";

  while (iterator != rle_encoded_string.end()) {
    string digit_component = "";

    while (isdigit(*iterator)) {
      digit_component += *iterator++;
    }

    char character_component = *iterator++;

    for (int i = std::stoi(digit_component); i > 0; --i) {
      decoded_string += character_component;
    }
  }
  return decoded_string;
}

int main() {
  string input_string = "saaadda";
  cout << "Testing " << input_string << '\n';
  cout << "Encoding result is " << RunLengthEncode(input_string) << '\n';
  cout << "Decoding back result is " << RunLengthDecode(RunLengthEncode(input_string)) << '\n';
  return 0;
}

