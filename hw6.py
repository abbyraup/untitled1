

name=input("What is your name?")
print("Welcome",name)
print("The goal of this game is to go from American University to HOME with your brother. Good luck.")


def playGame(s):
    d={('start','W'):'s0',('start','w'):'s2',('start','m'):'s1',
       ('start','U'):'s3',('s1','Y'):'s2',('s0','w'):'s2',
       ('s2','U'):'s3',('s3','A'):'s5',('s3','T'):'s4',
       ('s5','T'):'s4',('s5','A'):'start', ('s4','P'):'s6',
       ('s6','w'):'s9',('s6','s'):'start',('s6','d'):'s7',
       ('s6','w'):'s9',('s7','H'):'s10',('s9','H'):'s10',
       ('s9','b'):'s12',('s7','b'):'s12',('s6','b'):'s12',
       ('s12','H'):'s10', ('s10','H'):'s15'   }
    start_location='American University'
    

        
    






 if __name__ == '__main__':   
       playGame() 
