# put your code here.
def count_words(filename):
    #open file
    file = open(filename)

    word_counts = {}

    # loop through lines
    for line in file:
        line.rstrip()
        words = line.split()
        # loop through words in lines
        for word in words:
            word_counts[word] = word_counts.get(word,0)+1

    return word_counts


# use get function to count words 
print(count_words('twain.txt'))