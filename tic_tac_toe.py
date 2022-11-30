def field_init(n):
    field = []
    for i in range(n):
        s = []
        for j in range(n):
            s.append('--')
        field.append(s)
        s = []
    return field

def field_string(field):
    field_string = ''
    for i in range(len(field)):
        if i != 0:
            field_string += '\n'
        for j in range(len(field)):
            field_string += field[i][j] + '  '
    return field_string


def check_win(field):
    combinations = []
    
    # Запись в массив всех имеющихся на поле комбинаций по строкам, столбцам
    n = len(field)
    for i in range(n):
        string_comb = []
        column_comb = []
        for j in range(n):
            string_comb.append(field[i][j])
            column_comb.append(field[j][i])
        combinations.append(string_comb)
        combinations.append(column_comb)
        
    # Запись в массив всех имеющихся на поле комбинаций по диагоналям, если применимо
    if n%2 == 1:
        diag1_comb = []
        diag2_comb = []
        for i in range(n):
            diag1_comb.append(field[i][i])
            diag2_comb.append(field[n-i-1][i])
        combinations.append(diag1_comb)
        combinations.append(diag2_comb)
    
    # Проверка выигрыша
    win_combination_1 = []
    win_combination_2 = []
    for i in range(n):
        win_combination_1.append('X')
        win_combination_2.append('O')
    if win_combination_1 in combinations:
        return 1
    elif win_combination_2 in combinations:
        return 2
    else:
        return 0