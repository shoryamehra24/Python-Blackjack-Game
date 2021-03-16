import random
from os import system
cls = lambda: system('cls')
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 


def blackjack_start():

    start = input("Do you wish to play a game of Blackjack? Type 'y' or 'n'. ")

    user_cards = random.sample(cards, 2)


    dealer_cards = random.sample(cards,1)

        

    if start == "y":
        game_start = True
        print(logo)

        while game_start:

           

            #User Code
            user_score = 0

            

            for card in user_cards:
                user_score += card


            #Ace Code
            if user_score > 11:
                cards[0] = 1

        

            #Dealer Code
            dealer_score = 0

            if dealer_score > 11:
                cards[0] = 1

            
            for card in dealer_cards:
                dealer_score += card
            
            if dealer_score < 17:
                new_card = random.choice(cards)
                dealer_cards.append(new_card)
                dealer_score += new_card
               

              
            print(f"Your cards: {user_cards}, and current score: {user_score}")
            print(f"Computer's first card: {dealer_cards[0]}")

            def score_display(player_cards,player_score,computer_cards,computer_score):
                print(f"Your final hand: {player_cards}, final score: {player_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")      
           
            if user_score > 21 and dealer_score > 21:
                game_start = False
                cls()
                print("Draw! You both went over.😁")
                score_display(player_cards=user_cards,player_score=user_score,computer_cards=dealer_cards,computer_score=dealer_score)
                blackjack_start()
            if user_score > 21:
                game_start = False
                cls()
                print("You lose! You went over.🤦‍♀️")
                score_display(player_cards=user_cards,player_score=user_score,computer_cards=dealer_cards,computer_score=dealer_score)
                blackjack_start()
                    
            


            user_choice = input("Type 'y' to get another card and type 'n' to pass. ")

            
            if user_choice == "y":
                    new_card = random.choice(cards)
                    user_cards.append(new_card)
                    dealer_new_card = random.choice(cards)
                    dealer_cards.append(dealer_new_card)
                    
            elif user_choice == "n":
                if dealer_score < 17:
                    new_card = random.choice(cards)
                    dealer_cards.append(new_card)
                    dealer_score += new_card
                    score_display(player_cards=user_cards,player_score=user_score,computer_cards=dealer_cards,computer_score=dealer_score)    
                game_start = False
        

        if dealer_score > 21:
            game_start = False 
            cls()
            print("You win! Dealer went over.😂")
            score_display(player_cards=user_cards,player_score=user_score,computer_cards=dealer_cards,computer_score=dealer_score)
            blackjack_start()
        if dealer_score < user_score <= 21:
            game_start = False 
            cls()
            print("You win!👌")
            score_display(player_cards=user_cards,player_score=user_score,computer_cards=dealer_cards,computer_score=dealer_score)
            blackjack_start()
        elif user_score < dealer_score <= 21:
            game_start = False 
            cls()
            print("You lose!😢")
            score_display(player_cards=user_cards,player_score=user_score,computer_cards=dealer_cards,computer_score=dealer_score)
            blackjack_start()
        elif user_score == dealer_score:
            game_start = False 
            cls()
            print("Draw!😜")
            score_display(player_cards=user_cards,player_score=user_score,computer_cards=dealer_cards,computer_score=dealer_score)
            blackjack_start()

blackjack_start()
       



        


