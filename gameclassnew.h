#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <algorithm>
#include <ctime>
#include <set>

using namespace std;

const short NVAL=13;
const short NSUIT=4;

//const string cardvalue[13] = {"2","3","4","5","6","7","8","9","10","Jack","Queen","King","A"};
//const string cardsuit[4] = {"hearts","sprades","diamonds","clubs"};
const string cardsuit[4] = {"черви","вини","буби","крести"};
const string cardvalue[13] = {"2","3","4","5","6","7","8","9","10","Валет","Дама","Король","Туз"};


class Card{
    private:
        short value;
        short suit;
        bool on_heands=false;
        struct valuest{
            short value;
        };
    public:
        valuest mystruct;
        short getvalue(){
            mystruct.value = this->value;
            return this->value;
        };
        short getsuit(){
            return this->suit;
        };
        string display(){
            return cardvalue[this->value] + " " + cardsuit[this->suit];
        };
        Card(short dsuit,short dval){
            this->value = dval;
            this->suit = dsuit;
        };
};


class Dude{
    private:
        bool dealer=false;
        std::vector<Card> hand_cards = {};
		string cardcombination="";
        int player_stack=0;
		int player_bank=0;
        //short now; // 0 - idle 1 - играет и т.д

    public:
        string nick="";
		
        //Взять две карты для пользователя
        void take2cards(Card card1, Card card2){
             this->hand_cards.push_back(card1);
             this->hand_cards.push_back(card2);
        }
		
		void push_stack(int argstack){
			this->player_stack = argstack;
		}

        void become_dealer(){ 
            this->dealer = true;
        }

        auto get_hand_cards(){
            return this->hand_cards;
        }
        
        bool isdealer(){ 
            return this->dealer;
        }
		
		int get_stack(){
			return this->player_stack;
		}

		//MOVES
		void raise(int raise_bet){
			this->player_bank = player_bank + raise_bet;
			this->player_stack = this->player_stack - raise_bet;
		}

        int get_player_bank(){
            return this->player_bank;
        }
		void check(){
			bool a;
		}
		void fold(){
			this->hand_cards = {};
			this->cardcombination = "";
			this->dealer = false;
		}
		
};
class Combo{
    private:
		string pre_combo="None";
        std::vector<Card> cardsondesk_combo{};
        bool flush=false;
		short current=0;
        struct cmp{
            bool operator() ( Card a,  Card b){return a.getvalue() <  b.getvalue();}
        };
        struct cmp2{
            bool operator() ( Card a,  Card b){return a.getsuit() <  b.getsuit();}
        };
        auto range(short a,short b){
            std::vector<int> x(b);
            std::iota(std::begin(x), std::end(x), a);
            return x;
        };
        auto values(std::vector<Card> a){
            std:vector<int> n{};
            for (short i=0; i < a.size(); i++){
                n.push_back(a[i].getvalue());
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
			if (slice_int(values(a),from,to) == range(a[0].getvalue(),to)){
                return true;
            } else {
				return false;
			};
		}
        
    public:
        string answer(){
			//std::cout << "ВОТ НАЧАЛСЯ ПРОЦЕСС ПРОВЕРКА КАРТ!!!" << std::endl;
			//for (Card i : cardsondesk_combo){
			//	std::cout << i.display() << std::endl;
			//};
            std::sort(this->cardsondesk_combo.begin(),this->cardsondesk_combo.end(), [](Card  & a, Card  & b) -> bool{
                return a.getvalue() < b.getvalue(); 
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
        Combo(std::vector<Card> a, Dude Man){
            this->cardsondesk_combo = a;
			std::vector<Card> man_cards=Man.get_hand_cards();
            this->cardsondesk_combo.push_back(man_cards[0]);
            this->cardsondesk_combo.push_back(man_cards[1]);
			
			if (man_cards[0].getvalue() == man_cards[1].getvalue()){
				this->pre_combo = "One Pair (pre)";
			}
        }
};
class Table{
    private:
        //0 - ПРЕФЛОП; 1 - ФЛОП; 2 - ТЕРН; 3 - РИВЕР
        int sb;
		int last_bet;
        long int bank=0;
        std::vector<int> bets{}; //Чтобы хранить дл конкретного игрока его ставку
        std::vector<int> folded_bank{};
        std::vector<Card> desk = {};
        std::vector<Dude> players = {};
        std::vector<Card> deck = {};
        Dude dealer={};
        
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
		
    public:
		short round=0;

		void new_blinds(int blind){
            this->sb = blind;
        }

		int table_blinds(bool w){ // 0 - small blind; 1 - big blind
			if (w){
				return this->sb*2;
			} else {
				return this->sb;
			}
		}

        void make_zero_bets(){
            for (int i=0; i < this->players.size(); i++){
                this->bets.push_back(0);
            };
        }
        
        int whose_blind(bool wichblind){ // значит большой блайд // 0 - small blind // 1 - big blind
			int ival = get_player_by_nick(this->dealer.nick);
			if (ival+1 == this->players.size()){
				if (wichblind){
					return 1;
				} else {
					return 0;
				}
			} else {
				if (wichblind){
					if (ival+2 == this->players.size()){
						return 0;	
					} else {
						return ival+2;
					}
				} else {
					return ival+1;
				}
			}
		};

		void bet_blinds(){ 
            int smallb_player_i = whose_blind(0);
			this->players[smallb_player_i].raise(this->sb);
			this->bets[smallb_player_i] = this->sb;

            int bigb_player_i = whose_blind(1);
			this->players[bigb_player_i].raise(this->sb*2);
		    this->bets[bigb_player_i] = this->sb*2;

            //this->bank = this->bank + this->sb*2;
            this->last_bet = sb*2;
        }
       
        int get_bank(){
            int sum;
            for (int i=0; i < this->bets.size(); i++){
                sum = sum + this->bets[i];
            }
            for (int i=0; i < this->folded_bank.size(); i++){
                sum = sum + this->folded_bank[i];
            }
            return sum;
        }
        
        bool bets_are_equal(){
            std::set<int> setted_bets(this->bets.begin(), this->bets.end());
            std::cout << "BETS ARE EQUAL ";
            for (int i: this->bets){
                std::cout << i << " ";
            }
            std::cout << std::endl;
            if (setted_bets.size() == 1){
                return true;
            } else {
                return false;
            }
        }

        auto get_bets(){
            return this->bets;
        }
        
        auto get_players(){
            return this->players;
        }

        int get_player_by_nick(string argnick){
			for (short i=0; i < this->players.size(); i++){
				if (this->players[i].nick == argnick){
					return i;
				}
			}
			return 0;
		}

        void join_the_game(string argnick, int stack){
            Dude newdude;
			newdude.push_stack(stack);
			newdude.nick = argnick;
            this->players.push_back(newdude);
        }
		
		void deal_hand_cards(){
            for (short i=0; i < this->players.size(); i++){
                Card card1 = this->deck.back();
                this->deck.pop_back();
                Card card2 = this->deck.back();
                this->deck.pop_back();
                this->players[i].take2cards(card1,card2);  
            };
        }
        
		void someone_fold(int player_i){
           // std::cout << "PLAYER I " << player_i << std::endl;
            
            this->folded_bank.push_back(this->bets[player_i]);
            this->bets.erase(this->bets.begin() + player_i);
            this->players.erase(this->players.begin() + player_i);
            //this->folded_bets[player_i] = this->bets[player_i];
            //this->bets.erase(this->bets.begin() + player_i);
        }

        int get_last_bet(){
            return this->last_bet;
        }

        bool someone_can_bet(int player_i, int argbet){
            if (this->last_bet <= argbet && argbet != 0 && this->players[player_i].get_stack() >= argbet){
                return true;
            } else {
                return false;
            }
        }

        void someone_bet(int player_i, int argbet){
            this->players[player_i].raise(argbet);
            this->bets[player_i] = this->bets[player_i] + argbet;
            this->last_bet = argbet;
        }

        auto try_combo(Dude player){
			Combo MyCombo(this->desk,player);
			return MyCombo.answer();
		}
		
        string make_dealer(){
            short index = 0 + rand() % this->players.size();
            this->players[index].become_dealer();
            this->dealer = this->players[index];
			return this->dealer.nick;
        }
		
       
		
        auto cardsondesk(){
            return this->desk;
        }

        void put_cards_on_desk(){
            if (this->round == 1){
                this->desk.push_back(this->deck.back());
                this->deck.pop_back();
                this->desk.push_back(this->deck.back());
                this->deck.pop_back();
                this->desk.push_back(this->deck.back());
                this->deck.pop_back();
            }
            else{
                this->desk.push_back(this->deck.back());
                this->deck.pop_back();
            }
        }

        Table(){
            generate_deck();
            shuffle_the_deck();
        }


};



