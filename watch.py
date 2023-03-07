

# Problem set

import re


 # r represents raw string.
def main():
    Q = parse(input("HTML: "))
    print(Q)

def parse(s):
    A = "https://www.youtu.be/xvFZjo5PgG0"
    B = "http://youtu.be/xvFZjo5PgG0"
    C = "https://youtu.be/xvFZjo5PgG0"
    
    if re.search(r'<iframe .*?\bsrc="(https?://www\.youtube\.com/embed/xvFZjo5PgG0)"\><\/iframe>',s) :
    # https://www.youtube.com/embed/xvFZjo5PgG0

        #print(A)
        return C     #ch
    
    elif re.search(r'<iframe .*?\bsrc="(http?://youtube\.com/embed/xvFZjo5PgG0)"\><\/iframe>',s) :
    # http://youtube.com/embed/xvFZjo5PgG0

        #print(B)
        return C   # CH
    elif re.search(r'<iframe .*?\bsrc="(https?://youtube\.com/embed/xvFZjo5PgG0)"\><\/iframe>',s) :
    # https://youtube.com/embed/xvFZjo5PgG0

        #print(C)
        return C

    elif re.search(r'<iframe .*?\bwidth="(560)" .*?\bheight="(315)" .*?\bsrc="(https?://www.youtube.com/embed/xvFZjo5PgG0)" .*?\btitle="(YouTube video player)" .*?\bframeborder="(0)" .*?\ballow="(accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture)" .*?\ballowfullscreen\></iframe>',s) :
        #print(A)
        #return A
        return C
    elif re.search(r'<iframe .*?\bwidth="(560)" .*?\bheight="(315)" .*?\bsrc="(http?://youtube.com/embed/xvFZjo5PgG0)" .*?\btitle="(YouTube video player)" .*?\bframeborder="(0)" .*?\ballow="(accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture)" .*?\ballowfullscreen\></iframe>',s) :
        #print(B)
        return B

    elif re.search(r'<iframe .*?\bwidth="(560)" .*?\bheight="(315)" .*?\bsrc="(https?://youtube.com/embed/xvFZjo5PgG0)" .*?\btitle="(YouTube video player)" .*?\bframeborder="(0)" .*?\ballow="(accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture)" .*?\ballowfullscreen\></iframe>',s) :
        #print(C)
        return C

    else :
        #print("None")
        return None



if __name__ == "__main__":
    main()









