#include <stdio.h>
#include "game.h"
#include <vector>
#include <string>
#include <iostream>

void show_making_bets_process(Table obj){
    printf("Ставку делает");
    std::string nickname = obj.get_players()[obj.p_cursor(false)].nickname;
    //printf("%string", &nickname);
    std::cout << nickname << std::endl;
}

int main(){
    return 0;
}
