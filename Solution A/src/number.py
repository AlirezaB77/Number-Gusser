import random

def valid_data(a):
    if not a.isdigit():
        print('Invalid number. Please input number')
        return False
    a = int(a)
    if a < 1 or a > 100 :
        print('choose number between 1 to 100')
        return False
    return True

def strat_game():
    answer = random.randint(1,100)
    score = 100
    
    while True:
        user_gesse = (input("Enter number 1 to 100 / quit(q) : "))
        
        if user_gesse == 'q' :
            print('quit the game')
            break
        
        if not valid_data(user_gesse):
            continue
        
        user_gesse = int(user_gesse)
        if user_gesse < answer:
            print("your answer is lower than real answer")
            score -=10

        elif user_gesse > answer:
            print("your answer is higher than real answer")
            score -=10
        
        elif user_gesse == answer:
            print(f"your answer {answer} is correct")
            score = max(score, 0)
            print(f'You guessed correctly! Your score is: {score}')
            wanna_play = input('Do you want to play again? (y/n) ')
            if wanna_play == 'y':
                answer = random.randint(1, 100)
                score = 100
                continue
            else:
                print('Goodbye!')
                break


if __name__ == '__main__' :
    strat_game()



