#include <iostream>
#include "gameclassnew.h"
#include <string>
//using namespace std;

const string rounds[4] = {"ПреФлоп","Флоп","Терн","Ривер"};

bool isfold(string movement){
    std::string::size_type n;
	n = movement.find("fold");
	if (n == std::string::npos){
		return false;
	} else {
		return true;
	}
}



int main(){
    setlocale(LC_ALL, "rus");
    srand(time(0));
    std::cout << "Poker!Fold" << std::endl;
    std::cout << "Сколько игроков играет сегодня? ";
    int amount_players=0;
    std::cin >> amount_players;
    std::cout << std::endl;

    Table myTable;
    myTable.new_blinds(1);

    //Регистрация игроков
    for (int i=0; i < amount_players; i++){
        std::cout << "Игрок №" << i+1 << std::endl;
        std::cout << "Блайнд / Биг Балайнд: " << myTable.table_blinds(0) << " : " << myTable.table_blinds(1) << std::endl;
        std::cout << "Имя: ";
        string player_name="";
        cin >> player_name;
        int player_stack=0;
        while (myTable.table_blinds(1) > player_stack){
            std::cout << player_name << " будет иметь стек: ";
            std::cin >> player_stack;
            if (player_stack < myTable.table_blinds(1)){
                std::cout << "Стек должен быть больше, чем размер большого блайнда!" << std::endl;
            };
        }
        myTable.join_the_game(player_name,player_stack);
        std::cout << std::endl;
    }
    string dealer_nick = myTable.make_dealer();
    int player_cursor = myTable.get_player_by_nick(dealer_nick)+1;
    if (player_cursor == myTable.get_players().size()){
        player_cursor = 0;
    }
    std::cout << "Button: " << dealer_nick << std::endl;
    std::cout << "Игра начинается..." << std::endl;
    myTable.deal_hand_cards();
    myTable.make_zero_bets();

    for (int round=0; round < 4; round++){
        std::cout << "Раунд: " << rounds[round] << std::endl;
        std::cout << std::endl;
        if (round == 0){
            std::cout << "Малый блайнд делает: " << myTable.get_players()[myTable.whose_blind(0)].nick << std::endl;
            std::cout << "Большой блайнд делает: " << myTable.get_players()[myTable.whose_blind(1)].nick << std::endl;
            myTable.bet_blinds();
            player_cursor = myTable.whose_blind(1) + 1; // Следующий игрок
            if (player_cursor >= myTable.get_players().size()){
                player_cursor = 0;
            }
            
        }
        
        while (myTable.bets_are_equal() != true){
            std::cout << "Ходит игрок: " << myTable.get_players()[player_cursor].nick << std::endl;
            //std::cout << "Ваши карты:" << std::endl;
            //std::cout << myTable.get_players()[player_cursor].get_hand_cards()[0].display() << std::endl;
            //std::cout << myTable.get_players()[player_cursor].get_hand_cards()[1].display() << std::endl;
            std::cout << "Банк: " << myTable.get_bank() << std::endl;
            std::cout << "Ваш стек: " << myTable.get_players()[player_cursor].get_stack() << std::endl;
            std::cout << "Последняя ставка: " << myTable.get_last_bet() << std::endl;
            std::cout << "Введите ставку: (0 - fold)" << std::endl; 
            int new_bet=0;
            std::cin >> new_bet;
            std::cout << new_bet << std::endl;
            if (new_bet = 0){
                std::cout << "DA. FOLD" << std::endl;
                myTable.someone_fold(player_cursor);
                if (player_cursor+1 == myTable.get_players().size()){
                    player_cursor = 0;
                };

                std::cout << "Bets:" << std::endl;
                for (int i : myTable.get_bets()){
                    std::cout << i << " ";
                }
                std::cout << std::endl;
                std::cout << "player cursor " << player_cursor << std::endl;

            } else {
                while (new_bet <= myTable.get_last_bet() && new_bet <= myTable.get_players()[player_cursor].get_stack()){
                    std::cin >> new_bet;
                    if (myTable.get_last_bet() > new_bet){
                        std::cout << "Слишком маленькая ставка. Может вы фолд?" << std::endl;
                    }
                    if (myTable.get_players()[player_cursor].get_stack() < new_bet){
                        std::cout << "У вас слишком маленькой стек для такой ставки!";
                    }
                }
                myTable.someone_bet(player_cursor,new_bet);
                player_cursor++;
                if (player_cursor == myTable.get_players().size()){
                    player_cursor = 0;
                }
            }
        }
    }
    return 0;
}