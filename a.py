def editorMiss(text):

    count=0

    for ch in text:

        if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):

            pass

        elif(ch >= '0' and ch <= '9'):

            pass

        else:

            if(ch==" "):

                pass

            else:

                count=count+1

    return count