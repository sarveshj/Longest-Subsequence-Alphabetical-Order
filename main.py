

def longest_seq(s):
    
    
    
    """
    i/p : string
    o/p : list of alphabetical substring
    
    """
    seq_list =[]
    alphabet_list = 'abcdefghijklmnopqrstuvwxyz'

    
    #print(s)
    if s == '' or len(s) < 2:
        return []
        
    else:
        seq = ''
        for i in range(len(s)):
            if i+1 == len(s):
                #print(s[:i])
                #break
                #whole string is in order -- No need to call further recursion
                return seq_list + s[:i+1].split() 
            
            if ord(s[i+1]) >= ord(s[i]):
                continue
                
            else:
                return seq_list + s[:i+1].split() + longest_seq(s[i+1:])
            
        #print(s[:i].split())

def main():
        
    from random import randint
    from random import choice
    from string import ascii_lowercase

    s = ''.join(choice(ascii_lowercase) for i in range(25))    
        
    out = longest_seq(s)
    out_sorted = sorted(out, key =len)
    for l in out:
        if len(l) == len(out_sorted[-1]):
            break

    print( "Longest substring in alphabetical order is:" + l)
        
    
main()

