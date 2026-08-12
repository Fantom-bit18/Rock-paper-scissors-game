import random

CHOICES = {'К': "Камень", 'Н': "Ножницы", 'Б': "Бумага"}

WINNING_COMBINATIONS = {
    'К': 'Н',
    'Н': 'Б',
    'Б': 'К'
}

def get_user_choice():
    while True:
        try:
            user_input = input("\nВаш выбор (К/Н/Б): ").strip().upper()
        except (KeyboardInterrupt, EOFError):
            raise

        if not user_input:
            print("Пустой ввод. Пожалуйста, введите К, Н или Б.")
            continue

        user_input = user_input[0]

        if user_input in CHOICES:
            return user_input

        print("Неверный ввод. Пожалуйста, введите К, Н или Б.")

def get_computer_choice():
    return random.choice(list(CHOICES.keys()))

def determine_winner(user, comp):
    if user == comp:
        return 'tie'
    if WINNING_COMBINATIONS[user] == comp:
        return 'user'
    return 'comp'

def play_game(games):
    user_count = 0
    comp_count = 0
    ties = 0
    rounds = 0

    while rounds < games:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()

        print("Выбор компьютера: ", CHOICES[comp_choice])

        result = determine_winner(user_choice, comp_choice)

        if result == 'user':
            user_count += 1
            print("Вы выиграли этот раунд!")
        elif result == 'comp':
            comp_count += 1
            print("Компьютер выиграл этот раунд!")
        else:
            ties += 1
            print("Ничья")

        rounds += 1

        print("\n\t\t\tСЧЁТ")
        print(f"Вы: {user_count}\tКомпьютер: {comp_count}\tНичьи: {ties}\n")

    return user_count, comp_count, ties

def print_final_score(user_count, comp_count, ties):
    print("\n\t\tИТОГОВЫЙ СЧЁТ")
    print(f"Вы: {user_count}\tКомпьютер: {comp_count}\tНичьи: {ties}\n")

    if user_count > comp_count:
        print("\n\tПоздравляем! Вы победили!")
    elif user_count < comp_count:
        print("\n\tСожалеем! Вы проиграли!")
    else:
        print("\n\tОй! У вас ничья!")

def play_again():
    try:
        answer = input("\nСыграть ещё раз? (да/нет): ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        raise
        
    return answer in ("да", "д", "yes", "y", "1")

def main():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Нажмите Ctrl+C в любой момент для выхода.\n")

    try:
        while True:
            try:
                games_input = input("\nВведите количество раундов, которые хотите сыграть: ").strip()
                
                if not games_input:
                    print("Вы ничего не ввели. Попробуйте снова.")
                    continue
                    
                games = int(games_input)
                if games <= 0:
                    print("Количество раундов должно быть положительным числом.")
                    continue
                    
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите целое число.")
                continue

            user_count, comp_count, ties = play_game(games)
            print_final_score(user_count, comp_count, ties)

            if not play_again():
                break

    except KeyboardInterrupt:
        print("\n\nВы прервали выполнение программы. До свидания!")
    except EOFError:
        print("\n\nПоток ввода закрыт. До свидания!")
    except Exception as e:
        print(f"\nПроизошла непредвиденная критическая ошибка: {e}")
    finally:
        print("\nСпасибо за игру! Возвращайтесь снова!")


if __name__ == '__main__':
    main()
