# My Linguistics class wants me to look through a dozen Shakespeare sonnets and find rhymes represented in a table
# This is my solution

from sonnets import sonnets


word_bank_raw = "asleep deem keep leap no sea show speed weed \
                breed go know meet plea seem slow steep weep \
                deed grow leaf need reap eaf so sweet"
word_bank = word_bank_raw.split()

# actually finding the pairs
pairs = []
for sonnet_num in sonnets:
    sonnet = sonnets[sonnet_num]
    sonnet_lines = sonnet.split('\n')
    final_words = [line.split()[-1] for line in sonnet_lines]
    num_final_words = len(final_words)
    for i in range(num_final_words):
        final_word = final_words[i]
        if final_word in word_bank: # if one word is in the word bank
            nearby_word_indices = [i+1, i+2] # ignoring negatives to avoid double-counting
            filtered_words = [final_words[i] for i in nearby_word_indices if (i >= 0 and i < num_final_words)]
            for other_word in filtered_words: # check words around it
                if other_word in word_bank:
                    pairs.append([final_word, other_word])

# printing result in copy-paste-friendly fashion
for pair in pairs:
    print(pair[0] + '-' + pair[1])