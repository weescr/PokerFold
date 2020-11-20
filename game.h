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
        std::string nickname="";
    public:
        void bet(int newbet){
            this->stack = this->stack - newbet;
        }
        std::string name(){
            return this->nickname;
        }
        void bet(int argbet){
            this->stack = this->stack - argbet;
        }
        int get_stack(){
            return this->stack;
        }
        Player(std::string newnickname, int newstack){
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
        char index(std::vector<Player> mas, Player arg){
            char answ{};
            for (char i=0; i < mas.size(); i++){
                if (mas[i].name() == arg.name()){
                    return i;
                }
            }
            return -1;
        }

    public:
        char player_cursor=0;
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
        auto bet_blinds(){
            char n = index(this->players,this->dealer);
            char sbp = (player_cursor + 1) % this->players.size();
            char bbp = (player_cursor + 2) % this->players.size();
            this->players[sbp].bet(this->sb);
            this->players[bbp].bet(this->bb);
            this->bets[sbp] = this->sb;
            this->bets[bbp] = this->bb;
            this->lastBet = this->bb;
            std::pair<int,int> data{sbp,bbp};
            return data;
        }
        long int calc_bank(){
            long int sum=0;
            for (char i=0; i < this->bets.size(); i++){
                sum = sum + this->bets[i];
            };
            sum = sum + this->folded_score;
            return sum;
        }
        bool bets_are_equal(){
            std::set<int> setted_bets(this->bets.begin(), this->bets.end());
            if (setted_bets.size() == 1){
                return true;
            } else {
                return false;
            }
        }
        void tableBet(char player_i, int player_bet){
            this->players[player_i].bet(player_bet);
            this->bets[player_i] = this->bets[player_i] + player_bet;
            this->lastBet = this->bets[player_i];
            if (this->players[player_i].get_stack() == 0){
                this->all_ined = true;
            };
        }
        void someone_fold(char player_i){
            this->folded_score = this->folded_score + this->bets[player_i];
            this->bets.erase(this->bets.begin() + player_i);
            this->players.erase(this->players.begin() + player_i);
        }
        char p_cursor(bool find){
            if (find){
                this->player_cursor = (this->player_cursor + 1) % this->players.size();
            } else {
                return this->player_cursor;
            }
        }
        bool call_fold(std::string p_answer){
            std::string::size_type n;
            n = p_answer.find("fold");
            if (n == std::string::npos){
                return false;
            } else {
                return true;
            }
        }
        void end_bet_round(){
            this->all_game_money = this->all_game_money + ( this->bets[0] * this->players.size() );
            this->all_game_money = this->all_game_money + this->folded_score;
            this->bets = {};
            this->folded_score = 0;
            this->lastBet = 0;
            this->all_ined = false;
            this->make_zero_bets();
        }
        auto get_valid_bet(int pred_bet){
            if (pred_bet > this->players[this->player_cursor].get_stack() ){
                std::pair<bool,std::string> data{0,"Вы делаете ставку больше вашего стека. Введите новую ставку:\n"};
                return data;
            }
            if (pred_bet + this->bets[this->player_cursor] < this->lastBet){
                std::pair<bool,std::string> data{0,"Вы делаете ставку меньше последнего бета. Введите новую ставку:\n"};
            }
            this->player_bet = pred_bet;
        }
};