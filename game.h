#include <vector>
#include <string>
#include <random>
#include <algorithm>
#include <ctime>
#include <set>

const short NVAL=13;
const short NSUIT=4;

const std::string cardsuit[4] = {"черви","вини","буби","крести"};
const std::string cardvalue[13] = {"2","3","4","5","6","7","8","9","10","Валет","Дама","Король","Туз"};

class Card{
    private: //char - 1 bytes; short int - 2 bytes
        char value;
        char suit;
    public:
        char get_card_value(){
            return this->value;
        }
        char get_card_suit(){
            return this->suit;
        }
        std::string display(){
            return cardvalue[this->value] + " " + cardsuit[this->suit];
        }
        
        Card(char dsuit,char dval){
            this->value = dval;
            this->suit = dsuit;
        };
};

class Player{
    private:
        bool dealer=false;
        Card hand_cards[2];
        unsigned int stack{};
        std::string nickname{};
    public:
        int bet(int newbet){
            this->stack = this->stack - newbet;
        }
        Player(char newnickname, char newstack){
            this->stack = newstack;
            this->nickname = newnickname;
        }
};

