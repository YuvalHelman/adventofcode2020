#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <functional>

bool in_array(const std::string& value, const std::vector<std::string>& array)
{
    return std::find(array.begin(), array.end(), value) != array.end();
}

std::unordered_map<std::string, std::function<bool(std::string)>> rules {
    {
        "byr", [](auto const& s) {
            auto res = std::stoi(s);
            if (res < 1920 || res > 2002)
                return false;
            return true;
        }
    },
    {
        "iyr", [](auto const& s) {
            auto res = std::stoi(s);
            if (res < 2010 || res > 2020)
                return false;
            return true;
        }
    },
    {
        "eyr", [](auto const& s) {
            auto res = std::stoi(s);
            if (res < 2020 || res > 2030)
                return false;
            return true;
        }
    },
    {
        "hgt", [](auto const& s) {
            std::istringstream iss(s);
            std::string_view cm_or_in(s.end() - 2, s.end());
            std::string num(s.begin(), s.end() - 2);
            try {
                auto res = std::stoi(num);

                if (cm_or_in.compare("in")) {
                    if (res < 150 || res > 193)
                        return false;
                    return true;
                }
                else if (cm_or_in.compare("cm")) {
                    if (res < 59 || res > 76)
                        return false;
                    return true;
                }
                return false;
                }
            catch (const std::invalid_argument& e) {
                return false;
            }
        }
    },
    {
        "hcl", [](auto const& s) {
            std::string valid_chars("abcdef0123456789");
            constexpr int VALID_NUM_OF_CHARS = 6;
            int count = 0;
            char c;
            std::istringstream iss(s);

            if (s.find('#') != 0)
                return false;
            iss.get(); // read the #
            while (iss >> c) {
                if (valid_chars.find_first_of(c) == std::string::npos) {
                        return false;
                }
                ++count;
            }
            if (count != VALID_NUM_OF_CHARS)
                return false;
            return true;
        }
    },
    {
        "ecl", [](auto const& s) {
            std::vector<std::string> valid_items {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
            if (in_array(s, valid_items))
                return true;
            return false;
        }
    },
    {
        "pid", [](auto const& s) {
            std::string valid_chars("0123456789");
            constexpr int VALID_NUM_OF_CHARS = 9;
            if (s.size() != VALID_NUM_OF_CHARS) {
                return false;
            }
            for (char const& c : s) {
                if (valid_chars.find_first_of(c) == std::string::npos) {
                        return false;
                }
            }
            return true;
        }
    },
    {
        "cid", [](auto const& s) {
                return true;
        }
    },

};

std::istream& proccess_key_val_from_string(std::istringstream& iss, std::string& key, std::string& val) {
    return  std::getline(std::getline(iss, key, ':'), val, ' ');
}

bool is_item_valid(std::string& key, std::string& val) {
    auto key_it = rules.find(key);
    if (key_it != rules.end() && key_it->second(val)) {
        return true;
    }
    return false;
}

int process_lines_in_file(const std::string& input_path, bool add_rules) {
    std::string line, key, val;
    std::ifstream infile(input_path);
    std::unordered_set<std::string> tracked_items;
    auto num_valid_passports = 0;

    while (std::getline(infile, line)) {
        if (line.empty()) {
            if (tracked_items.size() == 8 ||
                (tracked_items.size() == 7 && tracked_items.find("cid") == tracked_items.end()) ) {
                ++num_valid_passports;
            }
            tracked_items.clear();
            continue;
        }else {
            std::istringstream iss(line);
            while (proccess_key_val_from_string(iss, key, val)) {
                if (!add_rules || is_item_valid(key, val)) {
                    tracked_items.insert(key);
                }
            }
        }
    }
    return num_valid_passports;
}


int main()
{
    std::cout << "ex1 res: " << process_lines_in_file("inputs/day4.txt", false) + 1 << std::endl; // checked last one manually because of EOF
    std::cout << "ex2 res: " << process_lines_in_file("inputs/day4.txt", true) + 1 << std::endl;
    return 0;
}
