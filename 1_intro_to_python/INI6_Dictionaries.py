#!/usr/bin/env python3
"""
Given:  A string s of length at most 10000 letters.
Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.
"""
s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
result = {}

for word in s.split(" "):
    if word in result.keys():
        result[word] += 1
    else:
        result[word] = 1

for key, value in result.items():
    print(key, value)

# Note: this doesn't acount for upper/lower case letters, eg) 'We' and 'we' are seen as different words
