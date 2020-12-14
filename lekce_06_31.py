# Napiš skript, který spočítá kolik samohlásek a souhlásek obsahuje následující string s anglickou větou:
# output:
# No. consonants: 43 | No. vowels: 30

sentence = 'A speech sound! that is produced, by comparatively open configuration of the vocal tract.'
sentence_list_raw = sentence.split()
final_dict = {'consonants': 0, 'vowels': 0}
for word in sentence_list_raw:
    word = word.strip(' ,.!?;:')
    for string in word:
        if string.lower() in 'aeiouy':
            final_dict['vowels'] += 1
        else:
            final_dict['consonants'] += 1
print(final_dict)
