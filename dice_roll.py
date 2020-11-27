import random

print('==========================================')
print('Dice Rolling Simulator Application and Die Prediction')
print('==========================================')

def main():
    
    is_arranged = True
    while is_arranged:
        global min_value,max_value
        min_value = int(input('Enter minimum die value: '))
        max_value = int(input('Enter maximum die value:'))
        
        if max_value < min_value:
            print('Max value must be greater than min value')
            
        else :
                #To ensure min and max values are 4>= x <= 6
            diff = max_value - min_value
            if diff >=4 and diff <= 6:
                break
            else : 
                print('Ensure the difference between your max and min values are less than 6 and greater than 4')
                

    die1 = random.randint(min_value,max_value)
    die2 = random.randint(min_value,max_value)

    roll_val = [die1, die2]
    
    tot_pred_chances = 0
    current_no_attempt = 0
    
    #Introduce game difficulty
    game_difficulty = {
        'easy' : 8,
        'medium' : 6,
        'hard' : 4
    }
    
    
    print('Enter game difficulty[easy,medium,or hard]')
    
    is_set = True
    while is_set:
        difficulty = input('> ').lower()
        if difficulty in game_difficulty:
            tot_pred_chances = game_difficulty.get(difficulty)
            is_set = False
        else:
            print('Please enter a valid game difficulty!!🔨')
            tot_pred_chances = 0

    exhausted_chances = False
    while not exhausted_chances:
        print(f'Predict die values from {min_value} to {max_value}')
        
        proper_prediction = False
        prediction = []
        while not proper_prediction:
            try:
                pred1 = int(input('First Value: '))
                pred2 = int(input('Second Value: '))
            
                if pred1 >= min_value and pred2 <= max_value:
                    prediction = [pred1,pred2]
                    proper_prediction = True
                else:
                    print('Predictions should be within the min and max value ranges')
            except ValueError:
                print('Ensure you enter a valid prediction')
           
        print(roll_val)
        
        if roll_val == prediction:
            print(f'Congratulations You predicted right in {current_no_attempt+1} attempts!! 🎉🎉')
            current_no_attempt = 0
            break
        else :
            print('Guessed wrong. Please try again')
            current_no_attempt += 1
            print('==========================================')
            
        
        if tot_pred_chances == current_no_attempt:
            exhausted_chances = True
        
    else :
        print('Out of Prediction Chances.😢😢 ')
      
main()

def game_prompt():
    print('Do you wanna start again?????')

    while True:
        restart = input('Y/y or N/n 🖊: ')

        if restart.lower() == 'y':
            print('==========================================')
            print('Loading........')
            print('==========================================')
            main()
        elif restart.lower() == 'n':
            print('Thank you for playing!!!!!!!. See you some other time. 😎😎')
            break
        else :
            print('Invalid Input!!😣')

game_prompt()


