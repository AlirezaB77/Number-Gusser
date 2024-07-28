from src.utils.input_valid import valid_data
from src.logic.number_gen import number_generator
from src.logic.hint_gen import hint_gen
from src.logic.score import Scorer

def main():
    random_number = number_generator(1,100)
    score = Scorer()
    while True:
        user_input = valid_data(1,100)
        if user_input == random_number:
            print(f"your answer {random_number} is correct")
            print(f"Congratulations! Your final score is: {score.get_score()}")
            break
        else:
            hint = hint_gen(user_input,random_number)
            #print(hint)
            score.decrement_score()



if __name__ == "__main__":
    main()