#include <SFML/Graphics.hpp>
#include <iostream>


void keyboard_move(sf::CircleShape* k){
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)){
        k->move(1.f, 0.f);
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)){
        k->move(-1.f, 0.f);
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)){
        k->move(0.f, -1.f);
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)){
        k->move(0.f, 1.f);
    }
}


int main(){

    sf::RenderWindow window(sf::VideoMode(800, 600), "My window");
    sf::Texture texture;
    if (!texture.loadFromFile("texture.jpg")){
        std::cout << "Не могу загрузить текстуру" << std::endl;
        return 0;
    }

    sf::CircleShape shape(50.f);
    shape.setTexture(&texture);
    shape.setPosition(sf::Vector2f(100,100));
    shape.setTextureRect(sf::IntRect(10, 10, 100, 100));


    while (window.isOpen()){
        sf::Event event;
        while (window.pollEvent(event)){
            if (event.type == sf::Event::Closed)
                window.close();
            
        }
        keyboard_move(&shape);
    

        window.clear(sf::Color::Black);
        window.draw(shape);
        window.display();
    }

    return 0;
}