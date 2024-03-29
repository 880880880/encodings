import yaml

mydict = {'key1': ['element_0', 'element_1'], 'key2': 1, 'key3': {}}
for i in range(166, 256):
    mydict['key3'][i]=chr(i)
with open('yamloutput.yaml','w', encoding='utf-8') as file:
    yaml.dump(mydict, file, default_flow_style=False, allow_unicode=True)
with open('yamloutput.yaml','r', encoding='utf-8') as file:
    loader=yaml.load(file, Loader=yaml.SafeLoader)
    if mydict==loader: print('File is equal to source dictionary')

# key1:
# - element_0
# - element_1
# key2: 1
# key3:
#   166: ¦
#   167: §
#   168: ¨
#   169: ©
#   170: ª
#   171: «
#   172: ¬
#   173: ­
#   174: ®
#   175: ¯
#   176: °
#   177: ±
#   178: ²
#   179: ³
#   180: ´
#   181: µ
#   182: ¶
#   183: ·
#   184: ¸
#   185: ¹
#   186: º
#   187: »
#   188: ¼
#   189: ½
#   190: ¾
#   191: ¿
#   192: À
#   193: Á
#   194: Â
#   195: Ã
#   196: Ä
#   197: Å
#   198: Æ
#   199: Ç
#   200: È
#   201: É
#   202: Ê
#   203: Ë
#   204: Ì
#   205: Í
#   206: Î
#   207: Ï
#   208: Ð
#   209: Ñ
#   210: Ò
#   211: Ó
#   212: Ô
#   213: Õ
#   214: Ö
#   215: ×
#   216: Ø
#   217: Ù
#   218: Ú
#   219: Û
#   220: Ü
#   221: Ý
#   222: Þ
#   223: ß
#   224: à
#   225: á
#   226: â
#   227: ã
#   228: ä
#   229: å
#   230: æ
#   231: ç
#   232: è
#   233: é
#   234: ê
#   235: ë
#   236: ì
#   237: í
#   238: î
#   239: ï
#   240: ð
#   241: ñ
#   242: ò
#   243: ó
#   244: ô
#   245: õ
#   246: ö
#   247: ÷
#   248: ø
#   249: ù
#   250: ú
#   251: û
#   252: ü
#   253: ý
#   254: þ
#   255: ÿ
