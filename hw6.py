

name=input("What is your name?")
print("Welcome",name)
print("The goal of this game is to go from American University to home. Good luck.")


def playGame(s):
    d={('American University','W'):'s0',('American University','w'):'s2',('American University','m'):'s1',
       ('American University','U'):'s3',('s1','Y'):'s2',('s0','w'):'s2',
       ('s2','U'):'s3',('s3','A'):'s5',('s3','T'):'s4',
       ('s5','T'):'s4',('s5','A'):'American University', ('s4','P'):'s6',
       ('s6','w'):'s9',('s6','s'):'American University',('s6','d'):'s7',
       ('s6','w'):'s9',('s7','H'):'s10',('s9','H'):'s10',
       ('s9','b'):'s12',('s7','b'):'s12',('s6','b'):'s12',
       ('s12','H'):'s10', ('s10','H'):'s15',('s4','N'):'s16',
       ('s16','N'):'s16',('s16','T'):'s4',('s12','d'):'s7',('s1','N'):'American University',
       ('s15','N'):'s15',('s15','Y'):'American University'
       }
    prompt={('American University'):'''You are at American University /nPress:/n W to take the Wonk Bus to Tenleytown. /nw to walk to Tenleytown.
    /nm to take the M4 bus to Tenleytown. /nU to take an Uber to Union Station.''',
        ('s0'):'''You got on the Wonk Bus, but the Wonk Bus broke down. /nPress: /nm to take the M4 bus /nw to walk''',
        ('s1'):'''You decided to try to take the M4 bus. /nPress:/nY if you brought your UPass /nN if you did not bring your Upass''',
        ('s2'):'''Press:/nU to take the metro to Union station''',
        ('s3'):'''Press:/nA to go to Auntie Anne's to get a soft pretzel /nT to go right to the train''',
        ('s5'):'''Press:/nA to go to Auntie Anne's to get a cinnamon and sugar pretzel /na to get a regular soft pretzel /nT to go to the train''',
        ('s4'):'''Press:/nN to take the train to NYC /nP to take the train to Philadelphia''',
        ('s16'):'''Press/nT to take the train back to Union Station /nN to stay in NYC''',
        ('s6'):'''Press: /nb to go to the bathroom /nw to wait for your next train /nd to go to Dunkin' Donuts /ns to go to Starbucks''',
        ('s7'):'''You got Dunkin /nPress: /nb to go to the bathroom /nH to take the train to Harrisburg''',
        ('s9'):'''You are waiting for your train./nPress:/nb to use the bathroom /nH to board the train to Harrisburg''',
        ('s12'):'''You are at the bathroom. /nPress:/nH to board the train to Harrisburg/nd to go to Dunkin' Donuts''',
        ('s10'):'''You are in Harrisburg/nPress:/nH to get in the car to go home''',
        ('s15'):'''You made it home!/nPress:/nY to play again/nN to stay at home'''
        }

#need to add variation to s5 to include cinnamon v plain pretzel. plain you go back to start. cinnamon stay at auntie annes



    start_location='American University'
    current_location=''

    reply=input("> ")
    while not ((current_location,reply) in d.keys()):
        print("That is not a valid. Try again!")
        reply=input("> ")
    current_location=d(current_location,reply)
    print("You are currently at "+current_location)

    

        
    






    if __name__ == '__main__':
       playGame() 
