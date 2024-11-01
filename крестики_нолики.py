def check_winner():
    if area[0][0] == 'x' and area[0][1] == 'x' and area[0][2] == 'x':
        return 'x'
    if area[1][0] == 'x' and area[1][1] == 'x' and area[1][2] == 'x':
        return 'x'
    if area[2][0] == 'x' and area[2][1] == 'x' and area[2][2] == 'x':
        return 'x'
    if area[0][0] == 'x' and area[1][0] == 'x' and area[2][0] == 'x':
        return 'x'
    if area[0][1] == 'x' and area[1][1] == 'x' and area[2][1] == 'x':
        return 'x'
    if area[0][2] == 'x' and area[1][2] == 'x' and area[2][2] == 'x':
        return 'x'
    if area[0][0] == 'x' and area[1][1] == 'x' and area[2][2] == 'x':
        return 'x'
    if area[2][0] == 'x' and area[1][1] == 'x' and area[0][2] == 'x':
        return 'x'
    if area[0][0] == 'x' and area[0][1] == 'x' and area[0][2] == 'x':
        return 'x'
    if area[1][0] == 'x' and area[1][1] == 'x' and area[1][2] == 'x':
        return 'x'

    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
        return '0'
    if area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
        return '0'
    if area[2][0] == '0' and area[1][1] == '0' and area[0][2] == '0':
        return '0'
    return '*'
def draw_area():
    for i in area:
        print(*i)
    print()
area = [['*','*','*'], ['*','*','*'], ['*','*','*']]
print('Добро пожаловать в игру "Крестики-нолики"')
print('---------------------------------------')
print('٩(｡•́‿•̀｡)۶')
print()
draw_area()
for turn in range (1,10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'x'
        print('Ходят крестики')
    row = int(input('Введите номер строки (1,2,3) ')) - 1
    column = int(input('Введите номер столбца (1,2,3) ')) - 1
    if area [row][column] == '*':
        area [row][column] = turn_char
    else:
        print('Ячейка уже занята, вы пропускаете ход :(')
        draw_area()
        continue
    draw_area()
    if check_winner() == 'x':
        print('Победа крестиков :)')
        break
    if check_winner() == '0':
        print('Победа ноликов :)')
        break
    if check_winner() == '*' and turn == 9:
        print('Ничья!!!')


