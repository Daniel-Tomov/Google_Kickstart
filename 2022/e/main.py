from time import sleep


def bot():
    global game_Board
    global bot_Score
    if game_Board[0] == 'white':
        game_Board[0] = 'Bot'
        if len(game_Board) == 1:
            return 1
        return 0

    #print(game_Board)

    for i in range(1, len(game_Board) - 1):
        #print(f'{i}   {game_Board[i - 1]}   {game_Board[i]}   {game_Board[i + 1]}  should equal {game_Board}')
        if game_Board[i - 1] == 'white' and game_Board[i] == 'white' and game_Board[i + 1] == 'white':
            game_Board[i] = 'Bot'
            #print(game_Board)

            bot_Score+=1
            return 0
    if game_Board[len(game_Board) - 1] == 'white' and game_Board[len(game_Board) - 2] == 'white':
        game_Board[len(game_Board) - 1] = 'Bot'
        bot_Score+=1
        return 0
    return 1



def john():
    global game_Board
    global john_Score

    for i in range(1, len(game_Board) - 1):
        if game_Board[i - 2] == 'white' and game_Board[i - 1] == 'white' and game_Board[i] == 'white' and game_Board[i + 1] == 'white':
            game_Board[i] = 'John'
            john_Score+=1
            #print(game_Board)
            return 0

    for i in range(1, len(game_Board) - 1):
        if game_Board[i - 1] == 'white' and game_Board[i] == 'white' and game_Board[i + 1] == 'white':
            game_Board[i] = 'John'
            john_Score+=1
            #print(game_Board)
            return 0
    if game_Board[len(game_Board) - 1] == 'white' and game_Board[len(game_Board) - 2] == 'white':
        game_Board[len(game_Board) - 1] = 'John'
        john_Score+=1
        return 0
    return 1


def main():
    global game_Board, bot_Score, john_Score

    #test_Cases = int(input())

    test_Cases = open('test_set_2/ts2_input.txt', 'r').read()
    test_Cases = test_Cases.split('\n')
    print(test_Cases)
    

    for i in range(int(test_Cases[0])):
        bot_Score = 1
        john_Score = 0
        
        #cells = int(input())
        cells = int(test_Cases[i + 1])

        game_Board = ['white'] * cells
        #print(game_Board)
        for g in range(len(game_Board)):
            print(g, end='\r')
            #print(game_Board)
            if bot() == 1:     
                print(f'Case #{i + 1}: {bot_Score}')
                break
            #print(game_Board)
            if john() == 1:
                print(f'Case #{i + 1}: {bot_Score}')
                break

if __name__ == "__main__":
    main()