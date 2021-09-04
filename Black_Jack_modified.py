# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:44:23 2021

@author: wajee
"""

import random

Cards={'Hearts':{'King':10,'Queen':10,'Jack':10,'Ace':[1,11],'2':2,'3':3,'4':4,'5':5,
                 '6':6,'7':7,'8':8,'9':9,'10':10},
       
       'Clubs':{'King':10,'Queen':10,'Jack':10,'Ace':[1,11],'2':2,'3':3,'4':4,'5':5,
                 '6':6,'7':7,'8':8,'9':9,'10':10},
       
       'Spades':{'King':10,'Queen':10,'Jack':10,'Ace':[1,11],'2':2,'3':3,'4':4,'5':5,
                 '6':6,'7':7,'8':8,'9':9,'10':10},
       
       'Diamond':{'King':10,'Queen':10,'Jack':10,'Ace':[1,11],'2':2,'3':3,'4':4,'5':5,
                 '6':6,'7':7,'8':8,'9':9,'10':10} }


def shuffle_cards():
    

    card_list=[]
    
    for card_type,cards in Cards.items():
        for card,score in cards.items():
           
            card_list.append([card_type,card])
 
  
    random.shuffle(card_list)
    
    return(card_list)

def deal():
   
    deck=shuffle_cards()
    
    player=random.sample(deck, 2)
    deck.remove(player[0])
    deck.remove(player[1])
       
    dealer=random.sample(deck, 2)
    deck.remove(dealer[0])
    deck.remove(dealer[1])
    
    return(player,dealer,deck)
              
               
def get_score(card_hand,score):
    
    for cards in card_hand:
    
            card_type=cards[0]
            card=cards[1]
            
            if(card =='Ace'):
                
                if(score < 11):
                    Ace_score=(Cards[card_type][card][1])
                    score+=Ace_score
                    
                if(score > 11 or score==11):
                    Ace_score=(Cards[card_type][card][0])
                    score+=Ace_score
    
            else:
                Value=Cards[card_type][card]   
                score += Value      
    return(score)


 
def Win_Condition(player_score,dealer_score,player_hand,dealer_hand,player_bank,player_bet):
    
      if((player_hand[0][1]=='Ace' and player_hand[1][1]=='King') or
       (player_hand[0][1]=='Ace' and player_hand[1][1]=='Queen') or
       (player_hand[0][1]=='Ace' and player_hand[1][1]=='Jack') or
       (player_hand[0][1]=='King' and player_hand[1][1]=='Ace') or
       (player_hand[0][1]=='Queen' and player_hand[1][1]=='Ace') or
       (player_hand[0][1]=='Jack' and player_hand[1][1]=='Ace')):
        
        print("Black Jack")
        print("Player wins")
        print(player_hand)
        Win=2*player_bet
        player_bank=player_bank + Win
        return(player_bank)
    
      if((dealer_hand[0][1]=='Ace' and dealer_hand[1][1]=='King') or
       (dealer_hand[0][1]=='Ace' and dealer_hand[1][1]=='Queen') or
       (dealer_hand[0][1]=='Ace' and dealer_hand[1][1]=='Jack') or
       (dealer_hand[0][1]=='King' and dealer_hand[1][1]=='Ace') or
       (dealer_hand[0][1]=='Queen' and dealer_hand[1][1]=='Ace') or
       (dealer_hand[0][1]=='Jack' and dealer_hand[1][1]=='Ace')):
        
        print("Black Jack")
        print("Dealer Wins")
        print(player_hand)
        print(dealer_hand)
        return(player_bank)
    
      if(player_score==21):
            
        print('Player Wins')
        print(player_hand)
        print(player_score)
        print(dealer_hand)
        print(dealer_score)
        player_bank+=2*player_bet
        return(player_bank)      
    
      if(dealer_score>21):
                
        print('Player Wins')
        print(player_hand)
        print(player_score)
        print(dealer_hand)
        print(dealer_score)
        player_bank+=2*player_bet
        
        return(player_bank)
        
        
      if(player_score==dealer_score):
         
        print(player_hand)
        print(player_score)
        print(dealer_hand)
        print(dealer_score)
        print("Push")
        
        return(player_bank)
     
    
      if(player_score>dealer_score):
         
         print("Player Wins")
         print(player_hand)
         print(player_score)
         print(dealer_hand)
         print(dealer_score)
         player_bank=player_bank + 2*player_bet
         
         return(player_bank)
        
      if(player_score<dealer_score):
         
         print("Player Loses")
         print(player_hand)
         print(player_score)
         print(dealer_hand)
         print(dealer_score)
         
         return(player_bank)

def Black_Jack(player_hand,dealer_hand,player_bet,player_bank,deck):
    
     player_score=0
     dealer_score=0
    
     print("Do you want to Hit or Stay")
     choice=input("Press H for Hit or S for Stay:")
     
     if(choice=='S' or choice=='s'):
         
  
         player_score=get_score(player_hand,player_score)
         dealer_score=get_score(dealer_hand,dealer_score)
         print(dealer_score)
    
     while choice=='H' or choice=='h':
         
        new_card=deck.pop()
        player_hand.append(new_card)
        print(player_hand)
     
        player_score=get_score(player_hand,player_score)
        dealer_score=get_score(dealer_hand,dealer_score)
       
        
        if(player_score >21):
            
         print('Bust')
         print("Player Loses")
         print(player_score)
         print(dealer_hand)
         print(dealer_score)
         return(player_bank)
         
        print("Do you want to Hit or Stay")
        choice=input("Press H for Hit or S for Stay:")
    
    
     while dealer_score < 18 :
            
         test_score=0
         
         dealer_card=deck.pop()
         dealer_hand.append(dealer_card)
         dealer_score=get_score(dealer_hand, test_score)
 
     player_bank=Win_Condition(player_score, dealer_score, player_hand, dealer_hand, player_bank, player_bet)
     return(player_bank)

def main():
    
    player_bank=2500
    play='Y'
    
    while play=='Y' or play=='y':
        
        player_bet=int(input("How much bet do you want to place:"))
        
        if(player_bet>player_bank):
            
            print("The amount of bet exceeds your Bank Amount")
            print("Please choose again")
            
        else:
            
            player_bank=player_bank-player_bet
            
            player_hand,dealer_hand,remaining_cards=deal()
            print("Your Hand Contains")
            print(player_hand)
            print("Dealers hand Contains")
            print(dealer_hand[0])
            player_bank=Black_Jack(player_hand,dealer_hand,player_bet,player_bank,remaining_cards)
            print(f"The Amount you currently have is {player_bank}")
            print("Do you want to continue playing")
            
            play=input("Press Y for yes or N for No:")
   


if __name__=='__main__':
    main()

         
         
         
    
  
