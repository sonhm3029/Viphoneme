from __init__ import vi2IPA_split, syms
'''
cou=0
M=[]
with open("Popular.txt",encoding="utf-8") as f:
    content=f.read().splitlines()
    for line in content:
        vi=vi2IPA_split(line,"/").split("/")
        print(vi)
        for v in vi:
            if v=="" or v=="." or v==" ":
                continue
            if v not in syms:
                print(v)
                cou+=1
                M.append(v)
print("Number of phoneme not in dict need to be modified",cou)
M=list(set(M))
print(M)
Modifi=['jw', 'ŋw', 'bw', 'vw', 'dw', 'eo', 'ʈw', 'mw', 'zw', 'fw', 'tw', 'tʰw', 'ɲw', 'cw', 'ʂw', 'ɣw', 'ʐw', 'xw', 'lw', 'hw', 'nw', 'sw', 'c']
listParse=['ʷiə', 'uəj', 'iəw', 'k͡p', 'ʷɤ̆', 'ɤ̆j', 'ŋ͡m', 'kwi', 'ɤ̆w', 'ɯəj', 'ʷen', 'ʷiu', 'ʷet', 'ɯəw', 'ʷɛ', 'ʷɤ', 'ɯj', 'oj', 'ăw', 'zi',
 'kw', 'aɪ', 'iɛ', 'ɤ̆', 'ɔ:', 'ăj', 'ʷa', 'eə', 'u:', 'uj', 'aʊ', 'uə', 'aj', 'iə', 'iw', 'əʊ', 'ɑ:', 'tʃ', 'ʷe', 'ɛu', 'ɔɪ', 'ʷi', 'eɪ', 'ɤj',
  'ɯw', 'ɛj', 'ɔj', 'i:', 't∫', 'ɪə', 'ʷă', 'ɜ:', 'tʰ', 'dʒ', 'ew', 'ʊə', 'ɯə', 'aw', '3', 'θ', 'v', 'ʊ', 'ʤ', 'ɔ', '1', 'ʧ', 'ʈ', ' ', 'd', 'i',
   'ɣ', 'ɲ', 'ɤ', '?', 'ɪ', 'l', '.', 'j', ':', 't', 'ʒ', 'ə', 'ʌ', 'm', '!', '∫', 'ð', 'u', 'e', 'w', 'p', 'ʃ', 'æ', "'", 'h', 'o', 'k', '5',
    'g', '4', 'n', ';', 'r', 'b', 'ɯ', 'a', 's', 'ʐ', 'η', 'ŋ', 'ɒ', 'ʂ', '_', 'f', ',', 'ɛ', 'z', '6', '2', 'x', 'ă']

'''
a=vi2IPA_split("Được viết vào 6/4/2020, có thể xử lí những trường hợp chứa English","/")
print(a)
#