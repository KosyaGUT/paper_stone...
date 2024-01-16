from random import *
from time import sleep


class Game:
    """
    Класс игры "Камень, ножницы, бумага"
    """
    winner: str  # Победитель
    generator_words: str  # Загаданное слово
    elements: dict = {
        'Бумага': 'Камень',
        'Камень': 'Ножницы',
        'Ножницы': 'Бумага'
    }

    def start(self) -> None:
        """
        Метод, начинающий игру
        """

        while True:
            # Загаданное слово генерируется компьютером
            self.generator_words = choice(list(self.elements.values()))
            # догадка вводится с клавиатуры
            user_word = input('Введите вашу догадку: ').capitalize()
            # проверка формата
            if user_word in self.elements:
                pass
            elif not user_word.isdigit() or user_word.isdigit():
                print("Введите либо Камень, либо Ножницы, либо Бумага")
                continue
            sleep(1)
            print('Камень, ножницы, бумага')
            sleep(1)
            print('Раз!')
            sleep(1)
            print('Два!')
            sleep(1)
            print('Триии!')
            sleep(1)

            # определение победителя
            if self.elements[user_word] == self.generator_words:
                print(f'{user_word} против {self.generator_words}, побеждает... {user_word}')
                self.winner = input('Как тебя зовут, победитель?\n')
                self.final()
                break
            elif user_word == self.generator_words:
                print('хех, ничья')
                continue
            else:
                print('Увы, ты проиграл...')
                break

    def final(self) -> None:
        """
        Метод, выводящий на экран консоли поздравление победителя.
        """

        print(f'Поздравляем, {self.winner} победил в игре!')


def main():
    game = Game()
    game.start()


if __name__ == '__main__':
    main()

