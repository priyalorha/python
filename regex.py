'''Python's regulax expression'''


import re

fil=open("dark.txt")

#search either dark or earth
for line in fil:
        if re.search("dark|earth",line):
            print(line,end='')

fil.close()


def tryo(filename):
    with open(filename)as temp:
        for t in temp:
            findmatch=re.search("dark|earth|friend",t)
            if findmatch:
                print(findmatch.group())




#find the word and replace it with something
def replacegame(filename):
    with open(filename) as temp:
        for t in temp:
            print(re.sub("earth","ho hala",t),end='')

#find the word and replace it with something and print only those case

def replacegame2(filename):
    with open(filename) as temp:
        for t in temp:
            findmatch=re.search("earth",t)
            if findmatch:
                print(t.replace(findmatch.group(),"HAla bol"),end=' ')

def replacegame3(filename):
    pattern=re.compile("earth")

    with open(filename) as temp:
        for t in temp:
            findmatch=re.search(pattern,t)
            if findmatch:
                print(t.replace(findmatch.group(),"HAla bol"),end=' ')

gu='''Tell me not, in mournful numbers,
Life is but an empty dream! -
For the soul is dead that slumbers,
And things are not what they seem. 


Life is real! Life is earnest!
And the grave is not its goal;
Dust thou art, to dust returnest,
Was not spoken of the soul. 


Not enjoyment, and not sorrow,
Is our destined end or way;
But to act, that each tomorrow
Find us farther than today. 


Art is long, and Time is fleeting,
And our hearts, though stout and brave,
Still, like muffled drums, are beating
Funeral marches to the grave. 


In the world’s broad field of battle,
In the bivouac of Life,
Be not like dumb, driven cattle!
Be a hero in the strife! 


Trust no Future, how’er pleasant!
Let the dead Past bury its dead!
Act, - act in the living Present!
Heart within, and God o’erhead! 


Lives of great men all remind us
We can make our lives sublime,
And, departing, leave behind us
Footprints on the sands of time; 


Footprints, that perhaps another,
Sailing o’er life’s solemn main,
A forlorn and shipwrecked brother,
Seeing, shall take heart again. 


Let us, then, be up and doing,
With a heart for any fate;
Still achieving, still pursuing
Learn to labor and to walk. '''
emAIL="abcd@gmail.com"
num='958-594-511'
numm=re.compile(r'\d\d\d-\d\d\d-\d\d\d')
m=numm.finditer(num)
for k in m:
    print(k)

pat=re.compile(r'[a-z,A-Z,0-9]@;.\w+',re.IGNORECASE)
mat=pat.finditer(emAIL)
print(mar for mar in mat)

print(x for match in mat)








replacegame3("dark.txt")


#replacegame2("dark.txt")

#replacegame("dark.txt")


pattern=re.compile(r'a/{1,3}b')
match=pattern.findall('a///b')
print(match)
pattern2=re.compile(r'\d+')
match2=pattern2.findall("James Bond 007i happiness 1/0")
print(match2)


print(re.findall(r'\d+','1232 dferf 1232'))







#tryo("dark.txt")