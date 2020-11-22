//#include <stdio.h>
#include "game.h"
#include <vector>
#include <string>
#include <iostream>
#include <sstream>

const std::string rounds[4] = {"ПреФлоп","Флоп","Терн","Ривер"};

template <typename T>
void print(T smth){
    std::cout << smth << std::endl;
}

void show_making_bets_process(Table obj){
    std::cout << "Ставку делает:" << obj.get_players()[obj.p_cursor(false)].name() << std::endl;
    std::cout << "Последняя ставка: " << obj.get_lastbet() << std::endl;
    std::cout << "Стек: " << obj.get_players()[obj.p_cursor(false)].get_stack() << std::endl;
    if (obj.get_bets()[obj.p_cursor(false)] != 0){
        std::cout << "Личный банк: " << obj.get_bets()[obj.p_cursor(false)] << std::endl;
    }
}

int main(){
    print("PokerFold (v. 0.1)");
    Table myTable(5);
    std::cout << "Блайнды: " << myTable.get_blinds().first << " / " << myTable.get_blinds().second << std::endl;
    print("Сколько сегодня играет?");
    short nplayers=0;
    std::cin >> nplayers;
    for (short i=0; i < nplayers; i++){
        print("Введите имя игрока");
        std::string temp_nick="";
        std::cin >> temp_nick;
        int temp_stack=0;
        while (myTable.get_blinds().second > temp_stack){
            print("Введите стек");            
            std::cin >> temp_stack;
            if (myTable.get_blinds().second > temp_stack){
                print("Ваш стек слишком маленький");
            }
        };
        myTable.join_the_game(temp_nick,temp_stack);
    }
    print("=======Регистрация закончена======");
    myTable.make_dealer();
    myTable.make_zero_bets();
    std::cout << "Button: " << myTable.get_dealer().name() << std::endl;

    for (short round=0; round < myTable.get_players().size(); round++){
        if (round == 0){
            std::pair<int,int> players_blinds = myTable.bet_blinds();
            std::cout << "Малый блайнд поставил: " << myTable.get_players()[players_blinds.first].name() << std::endl;
            std::cout << "Большой блайнд поставил: " << myTable.get_players()[players_blinds.second].name() << std::endl;
            //myTable.p_cursor(true);
            myTable.p_cursor(true);
            //myTable.p_cursor(true);
        }
        std::cout << "======" << rounds[round] << "======" << std::endl;
        show_making_bets_process(myTable);
        print("Введите новую ставку (0 - фолд)");
        int new_bet=0;
        std::cin >> new_bet;
        if (new_bet != 0){
            while (myTable.get_valid_bet(new_bet).first == 0 ){
                print( myTable.get_valid_bet(new_bet).second );
                std::cin >> new_bet;
            }
            myTable.tableBet(myTable.p_cursor(false), myTable.previous());
            myTable.p_cursor(true);
            print("Ставка сделана. Следующий!! ======");
        } else {
            myTable.someone_fold(myTable.p_cursor(false));
            if (myTable.p_cursor(false) >= myTable.get_players().size()){
                myTable.player_cursor = 0;
            };
            print("Упс... Кто то покину игру... =======");
        } // if fold
        std::cout << std::endl;
        while (myTable.bets_are_equal() != true){
            show_making_bets_process(myTable);
            if (myTable.all_ined){
                print("Предыдущий игрок сделал олл ин. Вам остается только коллить или фолдить. call / fold?");
                std::string answ="";
                std::cin >> answ;
                bool player_bool_answer = myTable.call_fold(answ);
                if (player_bool_answer){ // call
                    myTable.tableBet(myTable.p_cursor(false),myTable.get_bets()[ (myTable.p_cursor(false) - 1) % myTable.get_players().size() ]);
                    myTable.p_cursor(true);
                    print("Вы пошли олл-ин! ========");
                } else { // fold
                    myTable.someone_fold(myTable.p_cursor(false));
                    if (myTable.p_cursor(false) >= myTable.get_players().size()){
                        myTable.player_cursor = 0;
                    };
                    print("Упс... Он не согласился ставить олл-ин... ======");
                };
            } else { //allined
                print("Введите новую ставку (0 - fold)");
                int new_bet=0;
                std::cin >> new_bet;
                if (new_bet != 0){
                    while (myTable.get_valid_bet(new_bet).first == 0 ){
                        print( myTable.get_valid_bet(new_bet).second );
                        std::cin >> new_bet;
                    }
                    myTable.tableBet(myTable.p_cursor(false),myTable.previous());
                    myTable.p_cursor(true);
                    print("Ставка сделана. Следующий!! ======");
                } else {
                    myTable.someone_fold(myTable.p_cursor(false));
                    if (myTable.p_cursor(false) >= myTable.get_players().size()){
                        myTable.player_cursor = 0;
                    }
                    print("Упс... Кто то покинул игру... =======");
                } //new_bet != 0
            } // allined
        }//bets_are_equal
        if (myTable.get_players().size() == 1){
            std::cout << "Победил " << myTable.get_players()[0].name() << ", все остальные фолднули" << std::endl;
        }
        std::cout << "Конец раунда. Общий банк:" << myTable.calc_bank() << std::endl;
        myTable.end_bet_round();
    } // rounds for
    return 0;
}
