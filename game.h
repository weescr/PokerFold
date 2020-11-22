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
        std::pair<Card,Card> hand_cards{};
        unsigned int stack{};
        std::string nickname="";    
    public:
        void bet(int newbet){
            this->stack = this->stack - newbet;
        }
        std::string name(){
            return this->nickname;
        }
        void take_2_cards(std::pair<Card,Card> argcards){
            this->hand_cards = argcards;
        }
        int get_stack(){
            return this->stack;
        }
        std::pair<Card,Card> get_hand_cards(){
            return this->hand_cards;
        }
        Player() = default;
        Player(std::string newnickname, int newstack){
            this->stack = newstack;
            this->nickname = newnickname;
        };
};

class Combo{
    private:
		std::string pre_combo="None";
        std::vector<Card> cardsondesk_combo{};
        bool flush=false;
		short current=0;
        struct cmp{
            bool operator() ( Card a,  Card b){return a.get_card_value() <  b.get_card_value();}
        };
        struct cmp2{
            bool operator() ( Card a,  Card b){return a.get_card_suit() <  b.get_card_suit();}
        };
        auto range(short a,short b){
            std::vector<int> x(b);
            std::iota(std::begin(x), std::end(x), a);
            return x;
        };
        auto values(std::vector<Card> a){
            std::vector<int> n{};
            for (short i=0; i < a.size(); i++){
                n.push_back(a[i].get_card_value());
            };
            return n;
        };
        auto slice(std::vector<Card> argvec, short from, short to){
            std::vector<Card>::const_iterator first = argvec.begin() + from;
            std::vector<Card>::const_iterator last = argvec.begin() + to;
            return std::vector<Card>(first, last);
        };
        auto slice_int(std::vector<int> argvec, short from, short to){
            std::vector<int>::const_iterator first = argvec.begin() + from;
            std::vector<int>::const_iterator last = argvec.begin() + to;
            return std::vector<int>(first, last);
        };
        bool thereflush(std::vector<Card> a, int from, int to){
            std::vector<Card> suits=slice(a,from,to);
            std::set<Card, cmp2> setted_suit(suits.begin(),suits.end());
            if (setted_suit.size() == 1){
                return true;
            } else {
                return false;
            };
        };
        bool therestraight(std::vector<Card> a, int from, int to){
			if (slice_int(values(a),from,to) == range(a[0].get_card_value(),to)){
                return true;
            } else {
				return false;
			};
		}
        
    public:
        std::string answer(){
            std::sort(this->cardsondesk_combo.begin(),this->cardsondesk_combo.end(), [](Card  & a, Card  & b) -> bool{
                return a.get_card_value() < b.get_card_value(); 
            });
            Card minimal_card{this->cardsondesk_combo[0]};
            std::set<Card, cmp> setted_cards(this->cardsondesk_combo.begin(), this->cardsondesk_combo.end());
            unsigned long int uniques_length{setted_cards.size()};
            std::vector<Card> temp(setted_cards.begin(),setted_cards.end());
            
			if (uniques_length >= 5){
                std::vector<int> temp2=values(temp);
                int l=temp2.size();
                int l1=temp.size();
                
				if (thereflush(temp,l1-5, l1) && temp2[l-1] == 12 && temp2[l-2] == 11 && temp2[l-3] == 10 && temp2[l-4] == 9 && temp2[l-5] == 8){
					return "Royal Flush";
                };
				
				for (short i=0; i < 3; i++){
					if (therestraight(temp,0+i,5+i) && thereflush(temp,0+i,5+i)){
						return "Straight Flush";
					};
				}	
            }
			
			if (uniques_length == 4 || uniques_length == 3 || uniques_length == 2){
				std::vector<int> temp{values(cardsondesk_combo)};
				if ( std::count(temp.begin(),temp.end(),temp[0]) == 4 || std::count(temp.begin(),temp.end(),temp[1]) == 4 || std::count(temp.begin(),temp.end(),temp[2]) == 4){
					return "Four of a Kind";
				};
					return "Full House";
			};
			
            if (thereflush(temp,0,2) == true || thereflush(temp,1,6) == true || thereflush(temp,2,7) == true){
                return "Flush";
            };
			
			for (short i=0; i < 3; i++){
				if (therestraight(temp,0+i,5+i)){
					return "Straight";
				};
			}
			
            if (uniques_length == 5){
                std::vector<int> temp{values(this->cardsondesk_combo)};
                for(short i=0; i<5; i++){
                    if (std::count(temp.begin(),temp.end(),temp[i]) == 3){
                        return "Three of a kind / SET";
                    };
                };
                return "Two Pairs";
            };
			
            if (uniques_length == 6){
                return "One Pair";
            };
			
			return "nothing";
			
        }
        Combo() = default;
        Combo(std::vector<Card> a, Player Man){
            this->cardsondesk_combo = a;
			std::pair<Card,Card> man_cards = Man.get_hand_cards();
            this->cardsondesk_combo.push_back(man_cards.first);
            this->cardsondesk_combo.push_back(man_cards.second);
			
			if (man_cards.first.get_card_value() == man_cards.second.get_card_value()){
				this->pre_combo = "One Pair (pre)";
			}
        }
};
class Table{
    private:
        std::vector<int> bets{};
        std::vector<Player> players{};
        std::vector<Card> deck{};
        unsigned int lastBet=0;
        int sb=0;
        int bb = sb * 2;
        unsigned int folded_score=0;
        unsigned int all_game_money=0;
        int player_bet=0;
        
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
        bool all_ined=false;
        void generate_deck(){
            short i;
            short k;
            for (i = 0; i < 13; i++){
                for (k = 0; k < 4; k++){
                    this->deck.push_back(Card(k, i));
                } 
            }
        }
        void shuffle_the_deck(){
            std::random_shuffle(std::begin(this->deck), std::end(this->deck));
        }
        void join_the_game(std::string argnick, int argstack ){
            Player NewPlayer(argnick,argstack);
            this->players.push_back(NewPlayer); 
        }
        void deal_hand_cards(){
            for (short i=0; i < this->players.size(); i++){
                std::pair<Card,Card> new_hand_cards{};
                new_hand_cards.first = this->deck.back();
                this->deck.pop_back();
                new_hand_cards.second = this->deck.back();
                this->deck.pop_back();
                this->players[i].take_2_cards(new_hand_cards);  
            }
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
        std::vector<Player> get_players(){
            return this->players;
        }
        auto bet_blinds(){
            char n = index(this->players,this->dealer);
            char sbp = (n + 1) % this->players.size();
            char bbp = (n + 2) % this->players.size();
            this->players[sbp].bet(this->sb);
            this->players[bbp].bet(this->bb);
            this->bets[sbp] = this->sb;
            this->bets[bbp] = this->bb;
            this->lastBet = this->bb;
            this->player_cursor = bbp;
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
            return -1;
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
        std::pair<bool,std::string> get_valid_bet(int pred_bet){
            if (pred_bet > this->players[this->player_cursor].get_stack() ){
                std::pair<bool,std::string> data{0,"Вы делаете ставку больше вашего стека. Введите новую ставку:"};
                return data;
            }
            if (pred_bet + this->bets[this->player_cursor] < this->lastBet){
                std::pair<bool,std::string> data{0,"Вы делаете ставку меньше последнего бета. Введите новую ставку:"};
                return data;
            }
            std::pair<bool,std::string> data{1,"Ставка принята"};
            this->player_bet = pred_bet;
            return data;
        }
        int previous(){
            return this->player_bet;
        }
        std::pair<int,int> get_blinds(){
            std::pair<int,int> r{this->sb,this->sb*2};
            return r;
        }
        int get_lastbet(){
            return this->lastBet;
        }
        std::vector<int> get_bets(){
            return this->bets;
        }
        Player get_dealer(){
            return this->dealer;
        }
        Table(int smallb){
            this->sb = smallb;
            this->bb = this->sb * 2;
            generate_deck();
            shuffle_the_deck();
        };
};