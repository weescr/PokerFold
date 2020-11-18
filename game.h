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
        Card() = default;
        Card(char dsuit,char dval){
            this->value = dval;
            this->suit = dsuit;
        };
};

class Player{
    private:
        Card hand_cards[2];
        unsigned int stack{};
        std::string nickname{};
    public:
        void bet(int newbet){
            this->stack = this->stack - newbet;
        }
        Player(std::string newnickname, char newstack){
            this->stack = newstack;
            this->nickname = newnickname;
        };
};

class Table{
    private:
        std::vector<int> bets{};
        std::vector<Player> players{};
        unsigned int lastBet=0;
        int sb=0;
        int bb = sb * 2;
        char player_cursor=0;
        unsigned int folded_score=0;
        unsigned int all_game_money=0;
        int player_bet=0;
        bool all_ined=false;
        Player dealer;
    public:
        void join_the_game(std::string argnick, int argstack ){
            Player NewPlayer(argnick,argstack);
            this->players.push_back(NewPlayer); 
        }
        void make_dealer(){
            char index = 0 + rand() % this->players.size();
            this->dealer = this->players[index];
        }
        void make_zero_bets(){
            for (char i=0; i < this->players.size(); i++){
                this->bets.push_back(0);
            };
        }
        //void bet_blinds(){
         //   char n = this->players.index(self.dealer)
        //}
};