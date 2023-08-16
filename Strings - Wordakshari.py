Strings - Wordakshari
Antakshari is a popular parlor game played in India. Many word games are similar to antakshari. One such game is wordakshari. The game can be played
by two or more people. The first player has to recite a word. The last letter of the word is then used by the next player to recite another word starting
with that letter. The winner or winning team is decided by a process of elimination. The person or the team that cannot come up with a word with the right
consonant is eliminated. - The following rules need to be followed while playing this game. - (i) All other words except the first word have to begin with
the last letter of the previous word - (ii) No words can be repeated. write a program to print the wordakshari chain.

Input Format
Input consists of n+1 lines.
The first n lines contain strings corresponding to the words in the chain.
The last line of input contains the string #### to mark the end of the input.

Output Format
The output consists of the valid wordakshari chain.

Sample Input 0
oracle
error
rohit
####

Sample Output 0
oracle
error
rohit

Explanation 0
In oracle the last letter is e and so the next word will be error since it starts with e and it goes on like that and hence the output is
oracle
error
rohit

Sample Input 1
word
diameter
run
nest
high
####

Sample Output 1
word
diameter
run
nest

Explanation 1
Here the last letter of the first word is d and so the second output is an diameter and it goes on. Hence the output is
word
diameter
run
nest

Python Code:

def wordakshari_chain(words):
    chain = [words[0]]
    for i in range(1, len(words)):
        if words[i][0] == chain[-1][-1] and words[i] not in chain:
            chain.append(words[i])
        else:
            break
    return chain
input_lines = []
while True:
    word = input().strip()
    if word == "####":
        break
    input_lines.append(word)
chain = wordakshari_chain(input_lines)
for word in chain:
    print(word)
