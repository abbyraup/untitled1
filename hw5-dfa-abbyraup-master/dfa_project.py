def my_dfa(s):
    L=list(s)
    if len(L) < 1:
        return ('q0', False)
    hist=['q0']
    while len(L)>0:
        current_node=hist[-1]
        current_character = L[0]
        if current_node=='q0' and current_character=='0':
            hist.append('q1')
        elif current_node=='q0' and current_character=='1':
            hist.append('q2')
        elif current_node == 'q1' and current_character == '0':
            hist.append('q3')
        elif current_node == 'q1' and current_character == '1':
            hist.append('q2')
        elif current_node == 'q2' and current_character == '0':
            hist.append('q1')
        elif current_node == 'q2' and current_character == '1':
            hist.append('q4')
        elif current_node == 'q3' and current_character == '0':
            hist.append('q3')
        elif current_node == 'q3' and current_character == '1':
            hist.append('q2')
        elif current_node == 'q4' and current_character == '0':
            hist.append('q1')
        elif current_node == 'q4' and current_character == '1':
            hist.append('q4')
        L.pop(0)
    return(hist, boo(hist))

def boo(hist):
    if hist[-1] in {'q3','q4'}:
        return True
    else:
        return False




