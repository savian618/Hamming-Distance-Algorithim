def hamming_dist(word1, word2):
    val = 0.0
    if len(word1) == len(word2):
        for x in range(len(word1)):
            w1 = word1[x]
            w2 = word2[x]
            if w1 == ' ' and w2 == ' ':
                continue
            if (w1.lower() == 's' and w2.lower() == 'z') or (w1.lower() == 'z' and w2.lower() == 's'):
                if (w1 == w1.lower() and w2.upper() == w2) or (
                        w1 == w1.upper() and w2.lower() == w2):
                    val += .5
            elif (w1 == w1.lower() and w2.upper() == w2) or (
                    w1 == w1.upper() and w2.lower() == w2):
                val += .5
                if w1.lower() != w2.lower():
                    val += 1
            elif w1.lower() != w2.lower():
                val += 1

    return val


if __name__ == "__main__":
    print(hamming_dist("make", "mage"))
    print(hamming_dist("MaiSY", "MaiZy"))
    print(hamming_dist("Eagle", "Eager"))
    print(hamming_dist("Sentences work too", "Sentences wAke too"))
    print(hamming_dist("data Science", "Data Sciency"))
    print(hamming_dist("organizing", "orGanising"))
    print(hamming_dist("AGPRklafsdyweIllIIgEnXuTggzF", "AgpRkliFZdiweIllIIgENXUTygSF"))
