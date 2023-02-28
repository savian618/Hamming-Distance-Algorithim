# Hamming-Distance-Algorithim

A program to calculate a variant of the Hamming distance with two key modifications to the standard algorithm. 
In information theory, the Hamming distance is a measure of the distance between two text strings. 
This is calculated by adding one to the Hamming distance for each character that is different between the two strings. 
For example, “kitten" and “mitten" have a Hamming distance of 1. See https://en.wikipedia.org/wiki/Hamming_distance for more information. 
Modifications to the standard Hamming distance algorithm for the purposes of this exercise include: 
Add .5 to the Hamming distance if a capital letter is switched for a lower case letter unless it is in the first position.  Examples include: 
"Kitten" and "kitten" have a distance of 0 
"kitten" and "KiTten" have a Hamming distance of .5.
"Puppy" and "POppy" have a distance of 1.5 (1 for the different letter, additional .5 for the different capitalization). 
Consider S and Z (and s and z) to be the same letter. For example, "analyze" has a distance of 0 from "analyse".




