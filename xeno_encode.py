#xeno_encode.py
#Zaine Wilson
#a simple poem enciphering script
import string
available_pairs = ['A','C','G','U']
encode_dict = {}
pairslist = []
poem_alphabet = list(string.ascii_letters+string.punctuation+" ")
index = 0
for a in available_pairs:
	for b in available_pairs:
		for c in available_pairs:
			for d in available_pairs:
				pairslist.append(a+b+c+d)
				index+=1
				if index == len(poem_alphabet):
					break;
encode_dict=dict(zip(poem_alphabet,pairslist))
print "Poem encoding dictionary cooked: \n"
print encode_dict
print "\n\n"
print "Enter lines from your poem, then enter #$QUIT$# to stop entry"
flag = False
message_list = []
while(flag != True):
	message = raw_input(">")
	if message == "#$QUIT$#":
		flag =  True
	else:
		message_list+=list(message)
ciphertext_list = []
for i in message_list:
	ciphertext_list.append(encode_dict[i])
print "_".join(ciphertext_list)
