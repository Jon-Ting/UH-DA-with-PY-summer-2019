#!/usr/bin/env python3

def word_frequencies(filename):
    freq_dict = {}
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            split_line = line.strip("""!"#$%&'()*,-./:;?@[]_""").split()
            for j, word in enumerate(split_line):
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word not in freq_dict.keys():
                    freq_dict[word] = 1
                else:
                    freq_dict[word] += 1
    print(freq_dict)
    return freq_dict

def main():
    word_frequencies("src/alice.txt")

if __name__ == "__main__":
    main()
