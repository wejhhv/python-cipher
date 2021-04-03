
##指定シンボルにおけるすべてのカギについて復号の結果を表示する

SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

#暗号文を引数として入力
def caesarhack(message):
    
    candidate=[]#元の文章の候補

    for key in range(len(SYMBOLS)):
        translated=""

        for symbol in message:
            #シンボル内での文字列であるか
            if symbol in SYMBOLS:
                symbolIndex=SYMBOLS.find(symbol)
                translatedIndex=symbolIndex-key
                
                if translatedIndex<0:
                    translatedIndex=translatedIndex+len(SYMBOLS)

                translated=translated+SYMBOLS[translatedIndex]        

            else:
                translated=translated+symbol
        
        if translated[-1]==".": 
            candidate.append(translated)

        print("key #%s: %s" % (key,translated))
    
    return candidate

#暗号文
message="guv6Jv6Jz!J6rp5r7Jzr66ntrM"
caesarhack(message)
