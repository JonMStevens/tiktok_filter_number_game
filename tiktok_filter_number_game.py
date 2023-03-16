import random

main_game_list = [0] * 20


def print_game_state(game_list: "list[int]"):
    print('\n'.join([f'{i + 1}: {x}' for i, x in enumerate(game_list)]))


def take_turn(game_list: "list[int]"):
    next_num = random.randint(1, 999)
    print(f"Next number: {next_num}")
    if (game_won(game_list, next_num)):
        print("You win 🎖")
        game_list = [0] * 20
        return
    if (game_lost(game_list, next_num)):
        print("You lose 😭")
        game_list = [0] * 20
    user_input = get_user_input(game_list, next_num)
    game_list[user_input] = next_num


def game_won(game_list: "list[int]", next_num: int) -> bool:
    zero_count = sum(1 for num in game_list if num == 0)
    if zero_count > 1:
        return False

    if zero_count == 1:
        zero_i = game_list.index(0)
        game_list[zero_i] = next_num

    return list_is_sorted(game_list)


def game_lost(game_list: "list[int]", next_num: int) -> bool:
    # todo define other loss condition
    turn_num = sum(1 for num in game_list if num > 0) + 1
    return not game_won(game_list, next_num) and turn_num >= 20


def list_is_sorted(game_list: "list[int]"):
    if len(list < 2):
        return True

    return all(num > 0 for num in game_list) and all(
        game_list[i] <= game_list[i+1] for i in range(len(game_list) - 1))


def get_user_input(game_list: "list[int]", next_num: int) -> int:
    while (1):
        try:
            i = int(input("choose your spot ->")) - 1
        except:
            continue

        if not 0 <= i <= 20:
            print("Please enter a number between 1 and 20")
            continue

        if not game_list[i] == 0:
            print("Please place the number in a spot with a zero")
            continue

        # could place the number in a fake list, filter zeroes, check if sorted
        before = list(filter(lambda x: x != 0, game_list[:i]))
        if len(before) > 0 and any(x > next_num for x in before):
            print("number must be placed before all larger numbers")
            continue
        after = list(filter(lambda x: x != 0, game_list[i + 1:]))
        if len(after) > 0 and any(x < next_num for x in after):
            print("number must be placed after all smaller numbers")
            continue

        return i


if __name__ == "__main__":
    while (1):
        print_game_state(main_game_list)
        take_turn(main_game_list)
