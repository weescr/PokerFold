//#include <stdio.h>
#include "game.h"
#include <vector>
#include <string>
#include <iostream>
#include <sstream>

const std::string rounds[4] = {"ПреФлоп","Флоп","Терн","Ривер"};
const std::string rounds_eng[4] = {"Preflop","Flop","Turn","River"}; 

void show_making_bets_process(Table obj){
    printf( "Player: %s\n", obj.get_players()[obj.player_cursor].name().c_str());
    
    if (obj.get_players()[obj.player_cursor].with_cards){ // Если у него есть карманные карты
        std::pair<Card,Card> player_cards = obj.get_players()[obj.player_cursor].get_hand_cards();
        printf( "Your cards: %s && %s\n",player_cards.first.display().c_str(), player_cards.second.display().c_str());
    }
    printf( "Last Bet: %d\n", obj.get_lastbet());
    printf("Stack: %d\n", obj.get_players()[obj.player_cursor].get_stack());
    if (obj.get_bets()[obj.p_cursor(false)] != 0){
        printf("Personal bank: %d\n", obj.get_bets()[obj.player_cursor]) ;
    }
}

void show_desk(Table obj){
    if (obj.get_desk().size() != 0){
        for (Card v : obj.get_desk()){
           printf("%s | ", v.display().c_str());
        } printf("\n");
    }
}

Table players_register(Table obj){
    short nplayers=0;
    printf("How many players are playing today? "); std::cin >> nplayers;
    for (short i=0; i < nplayers; i++){
        std::string temp_nick="";
        printf("New player name: "); std::cin >> temp_nick;
        int temp_stack=0;
        while (obj.get_blinds().second > temp_stack){
            printf("New player stack: "); std::cin >> temp_stack;
            if (obj.get_blinds().second > temp_stack){ printf("Your stack is too small"); }
        };
        printf("Registered!\n");
        obj.join_the_game(temp_nick,temp_stack);
    }
    return obj;
}

int main(){
    printf("PokerFold (v. 0.1)\n");
    Table preTable(5);
    //printf("==========Registration of new players=========");
   // printf("Blinds are: %s / %s\n", preTable.get_blinds().first, preTable.get_blinds().second);
    Table myTable =  players_register(preTable);
    printf("=======Registration of new players is over======\n");
    myTable.make_dealer();
    myTable.make_zero_bets();
    myTable.deal_hand_cards();

    printf("Button: %s\n", myTable.get_dealer().name().c_str());
    
    for (short round=0; round < myTable.get_players().size(); round++){
        myTable.put_cards_on_desk(round);
        if (round == 0){
            std::pair<int,int> players_blinds = myTable.bet_blinds();
            printf("SB / BB: %s & %s\n", myTable.get_players()[players_blinds.first].name().c_str(), myTable.get_players()[players_blinds.second].name().c_str());
            myTable.p_cursor(true); // Следующий после блайндов
        }
       
        printf("====== %s ======\n",  rounds_eng[round].c_str());
        show_making_bets_process(myTable);
        int new_bet=0;
        printf("Введите новую ставку (0 - фолд): ");  std::cin >> new_bet;
        show_desk(myTable);
        if (new_bet != 0){
            while (myTable.get_valid_bet(new_bet).first == 0 ){
                printf( "%s: ", myTable.get_valid_bet(new_bet).second.c_str()); std::cin >> new_bet;
            }
            myTable.tableBet(myTable.p_cursor(false), myTable.previous());
            myTable.p_cursor(true);
            printf("====== Ставка сделана. Следующий!! ======\n");
        } else {
            myTable.someone_fold(myTable.p_cursor(false));
            if (myTable.p_cursor(false) >= myTable.get_players().size()){
                myTable.player_cursor = 0;
            };
            printf("Упс... Кто то покину игру... =======\n");
            // ticket 1: Если в новом раунде первую ставку сделать нулевой, то игра завершится 
        } // if fold
        while (myTable.bets_are_equal() != true){
            show_making_bets_process(myTable);
            if (myTable.all_ined){
                std::string answ="";
                printf("Предыдущий игрок сделал олл ин. Вам остается только коллить или фолдить. call / fold? "); std::cin >> answ;
                bool player_bool_answer = myTable.call_fold(answ);
                if (player_bool_answer){ // call
                    myTable.tableBet(myTable.player_cursor,myTable.get_bets()[ (myTable.player_cursor - 1) % myTable.get_players().size() ]);
                    myTable.p_cursor(true);
                    printf("Вы пошли олл-ин! ========\n");
                } else { // fold
                    myTable.someone_fold(myTable.player_cursor);
                    if (myTable.player_cursor >= myTable.get_players().size()){
                        myTable.player_cursor = 0;
                    };
                    printf("Упс... Он не согласился ставить олл-ин... ======\n");
                };
            } else { //allined
                int new_bet=0;
                printf("Введите новую ставку (0 - fold): "); std::cin >> new_bet;
                if (new_bet != 0){
                    while (myTable.get_valid_bet(new_bet).first == 0 ){
                        printf("%s:", myTable.get_valid_bet(new_bet).second.c_str()); std::cin >> new_bet;
                    }
                    myTable.tableBet(myTable.p_cursor(false),myTable.previous());
                    myTable.p_cursor(true);
                    printf("Ставка сделана. Следующий!! ======\n");
                } else {
                    myTable.someone_fold(myTable.p_cursor(false));
                    if (myTable.p_cursor(false) >= myTable.get_players().size()){
                        myTable.player_cursor = 0;
                    }
                    printf("=======Упс... Кто то покинул игру... =======\n");
                } //new_bet != 0
            } // allined
        }//bets_are_equal
        if (myTable.get_players().size() == 1){
            printf("Победил %s, все остальные фолднули\n", myTable.get_players()[0].name() .c_str());
        }
        printf("Конец раунда. Общий банк: %d\n", myTable.calc_bank());
        myTable.end_bet_round();
    } // rounds for
    return 0;
}
