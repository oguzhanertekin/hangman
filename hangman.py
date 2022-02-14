import random

HANGMAN=(
    """
 ------
|     |
|
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|
|
|
|
|
----------
"""
   ,
"""
 ------
|     |
|     0
|     +
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    |
|    |
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    | |
|    | |
----------
"""
)

def findLetter(letter,word):
    indexList=[]
    for indx in range(0,len(word)):
        if letter==word[indx]:
            indexList.append(indx)
    return indexList

word="DENEME"        

right=14
private="_"*len(word)
privateList=list(private)
wrong=0

while True:
    
    if word==private:
        print("""
    ------------------
    | CORRECT GUESS! |
    ------------------
    WORD IS: {}
    """.format(word))
    
    guess=input("ENTER YOUR GUESS: ")
    guess=guess.upper()

    if right==0 or wrong==11:
        print("YOU HAVE NO RIGHTS LEFT")
        break

    
    
    if len(guess)>1:
        if guess!=word:
            print("""
            ----------------
            | WRONG GUESS! |
            ----------------
            
            """)
            print(HANGMAN[wrong])
            wrong+=1
            right-=1
            print("YOUR RIGHT: {}".format(right))
        elif guess==word:
            print("""
            ------------------
            | CORRECT GUESS! |
            ------------------
            WORD IS: {}
            """.format(word))
            break
    
    elif len(guess)==1:
        if findLetter(guess,word):
            for char in findLetter(guess,word):
                char=int(char)
                privateList[char]=guess
                private="".join(privateList)
            print(HANGMAN[wrong])
            print(*private)

            right-=1
            print("YOUR RIGHT: {}".format(right))
        else:
            print("""
            ----------------
            | WRONG GUESS! |
            ----------------
            """)
            print(HANGMAN[wrong])
            wrong+=1
            right-=1
            print("YOUR RIGHT: {}".format(right))

            







