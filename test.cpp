#include <SFML/Graphics.hpp>

int main(){
    sf::RenderWindow window(sf::VideoMode(200, 200), "SFML works!"); //инициализация окна
    sf::CircleShape shape(100.f); //нарисовать круг
    shape.setFillColor(sf::Color::Green); //сменить цвет

    while (window.isOpen()){
        sf::Event event; // обработчик ивентов
        while (window.pollEvent(event)){ //пока получаем события от окна
            if (event.type == sf::Event::Closed) //если событие "закрыть"
                window.close(); //закрыть
        }
        window.clear(); //очистить окно
        window.draw(shape); //нарисовать круг
        window.display(); //отобразит
    }

    return 0;
}