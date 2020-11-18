#include <stdio.h>
#include "game.h"
#include <vector>


bool comp( Card& rhs,  Card& lhs){
    return (rhs.get_card_value() == lhs.get_card_value());
}

int main(){
    
    //
    Card Card1(1,1);
    Card Card2(2,1);
    Card Card3(3,1);
    std::vector<Card> cards{Card1,Card2,Card3};
    Card it = Card3;
   // int index = std::find_if(cards.begin(),cards.end(), it.get_card_value(), comp);
    //int index = std::find(cards.begin(),cards.end(), it);
    auto index = std::find(cards.begin(),cards.end(), [](const Card& s))}{return s.value == } )
    printf("%d\n",index);
    return 0;
}
