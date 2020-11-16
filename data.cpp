#include <iostream>
#include "gameclassnew.h"
#include <string>
using namespace std;

const string rounds[4] = {"ПреФлоп","Флоп","Терн","Ривер"};
const string commands[4] = {"bet","raise","fold","ALL IN"};


string dealer_omg(bool a){
	if (a){
		return "|| Д и Л л Е р";
	}
	return "";
};

bool isfold(string movement){
	std::string::size_type n;
	n = movement.find("fold");
	if (n == std::string::npos){
		return false;
	} else {
		return true;
	}
}

int main(int argc, char*argv[]){
    setlocale(LC_ALL, "rus");
    srand(time(0));
	std::cout << "Poker!Fold v0.1" << std::endl;
	std::cout << "Сколько игроков будет играть сегодня? ";
	int n_players=0;
	cin >> n_players;
	
	std::cout << std::endl;
	
	Table myTable;
	int temp_stack=0;
	myTable.new_blinds(1);
	string temp_nick="";
	for (int i; i < n_players; i++){
		std::cout<< i+1 << " Игрок,"  << " имя: ";
		cin >> temp_nick;
		while (myTable.blinds(1) >= temp_stack){
			std::cout << temp_nick << " будет иметь стек: ";
			cin >> temp_stack;
			if (myTable.blinds(1) >= temp_stack){
				std::cout << "Ваш стек должен быть больше, чем Большой Блайнд" << std::endl;
			};
		}
		myTable.join_the_game(temp_nick,temp_stack);
		std::cout << temp_nick << " получил стек в " << temp_stack << std::endl;
		temp_stack=0;
		std::cout << std::endl;
	};
	string dealer_nick = myTable.make_dealer();
    std::cout << "Button: " << dealer_nick << std::endl;
	
	std::cout << "Начинаем!" << std::endl;
	
	myTable.deal_hand_cards();
	for (short i=0; i < 5; i++){
		// Счётчик раундов
		
		std::cout << "Раунд: " << rounds[i] << std::endl;
		myTable.round = i;
		if (myTable.round == 0){
			std::cout << "Делаем первые ставки! " << std::endl;
			myTable.bet_blinds();
			for (int k=myTable.player_cursor(); i < myTable.get_players().size(); i++){
				// Счётчик игроков
				if (k+1 == myTable.get_players().size()){
					k = 0;
				}
				std::cout << "Ход игрока " <<  myTable.get_players()[k].nick << std::endl;
				std::cout << "Последняя ставка: " << myTable.get_last_bet() << std::endl;
				std::cout << "Ваш ход: (bet или fold)" << std::endl;
				string move;
				cin >> move;
			
				if (isfold(move)){
					myTable.someone_fold(k);
				} else {
					int newbet=0;
					while (newbet < myTable.get_last_bet() && newbet <= myTable.get_players()[k].get_stack()){
						std::cout << "Введите новый бет: ";
						cin >> newbet;
						if (newbet > myTable.get_players()[k].get_stack() ){
							std::cout << "У вас недостаточно фишек для такого бета. Ваш стек: " << myTable.get_players()[k].get_stack() << std::endl;
						} else {
							myTable.someone_bet(k, std::stoi(move));
							std::cout << "Ставка успешно приянта. Ваш банк:" << myTable.get_bank()[k] << std::endl;
						}	
				}	
			}
		}
	}
	
	
	
	
	
	std::cout << std::endl;
	
	std::cout << "Стол с картами: " << std::endl;
	for (short i=0; i < myTable.cardsondesk().size(); i++){
        std::cout << myTable.cardsondesk()[i].display() << std::endl;
    }
	std::cout << std::endl;
    return 0;
}
