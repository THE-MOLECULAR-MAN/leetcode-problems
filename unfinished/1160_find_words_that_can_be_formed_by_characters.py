#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/two-sum/description/
"""docstring"""

# from collections import Counter

# def sortString(string_to_sort):
#     from functools import reduce
#     return reduce(lambda a, b : a + b, sorted(string_to_sort))
     
def sortString2(string_to_sort):
    return ''.join(sorted(string_to_sort))

# def find_intersection_excluding_duplicates(lstr,rstr):
#     return set(lstr).intersection(rstr)

#def is_subset_of(lstr,rstr):
#    return set(lstr).issubset(set(rstr))

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        goodsum = 0
        l_chars = len(chars)
        for i, iter_word in enumerate(words):
            # if there are not enough characters to form the word, don't bother
            if len(iter_word) > l_chars:
                # print('word requires more characters than chars has, impossible')
                continue
            # may need to start subtracting letters?
            if set(iter_word).issubset(set(chars)):                
                print(sortString2(iter_word) + ' is subset of ' + sortString2(chars))
                goodsum += len(iter_word)                
        return goodsum

###############################################################################
#       MAIN
###############################################################################

# test_words = ["cat", "bt", "hat", "tree", "cathyz"]
# test_chars = "atach"
# correct_ans = 6
# ans = Solution().countCharacters(test_words, test_chars)
# print('INPUT words: ' + str(test_words) + '   chars: ' + test_chars)
# print('OUTPUT: ' + str(ans) + ' Correct: ' + str(correct_ans))
# assert ans == correct_ans


# test_words = ["hello","world","leetcode","impossiblylongword"]
# test_chars = "welldonehoneyr"
# correct_ans = 10
# ans = Solution().countCharacters(test_words, test_chars)
# print('INPUT words: ' + str(test_words) + '   chars: ' + test_chars)
# print('OUTPUT: ' + str(ans) + ' Correct: ' + str(correct_ans))
# assert ans == correct_ans


test_words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
    "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
    "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
    "boygirdlggnh",
    "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
    "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
    "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
    "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
    "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
    "oxgaskztzroxuntiwlfyufddl",
    "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
    "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
    "eeilfdaookieawrrbvtnqfzcricvhpiv",
    "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
    "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
    "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
    "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo",
    "teyygdmmyadppuopvqdodaczob",
    "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
    "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]

test_chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
correct_ans = 0
ans = Solution().countCharacters(test_words, test_chars)
# print('INPUT words: ' + str(test_words) + '   chars: ' + test_chars)
# print('OUTPUT: ' + str(ans) + ' Correct: ' + str(correct_ans))
# assert ans == correct_ans
