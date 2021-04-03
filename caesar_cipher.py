###シーザー暗号
#https://www.nostarch.com/crackingcodes/

import pyperclip

#シーザー暗号a~z,A~Z,1~!?.
def ceasar_cipher(message,key,seq):#文章、鍵、暗号か復号か(trueで暗号、falseで複合)
    SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
    translated=""
    
    for symbol in messeage:
        #シンボル内での文字列であるか
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)

            if seq==True:#暗号
                translatedIndex=symbolIndex+key

            elif seq==False:#復号
                translatedIndex=symbolIndex-key
            
            #繰り返しを行うときの処理
            if translatedIndex>=len(SYMBOLS):
                translatedIndex=translatedIndex-len(SYMBOLS)
            
            elif translatedIndex<0
                translatedIndex=translatedIndex+len(SYMBOLS)

            translated=translated+SYMBOLS[translatedIndex]        

        else:
            translated=translated+symbols
    
    return translated

'''tesecode
m="This is my secret messege"
re=ceasar_cipher(m,13,False)
print(re)
'''


