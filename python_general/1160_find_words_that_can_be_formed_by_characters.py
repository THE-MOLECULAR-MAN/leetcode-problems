#!/usr/bin/python3
# Tim H 2023
# UNFINISHED
# https://leetcode.com/problems/two-sum/description/
"""docstring"""
# Need to use the Counter class instead of multiset
# Leetcode doesn't allow you to install additional python modules beyond
# what they have
# ./.venv/bin/python -m pip install -r requirements.txt
# https://multiset.readthedocs.io/en/stable/
# https://docs.python.org/3.10/library/collections.html#collections.Counter


from multiset import Multiset
     
# def sortString2(string_to_sort):
#     return ''.join(sorted(string_to_sort))

# Leetcode doesn't allow system calls:
# import subprocess
# import sys
# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# import pip
# def install(package):
#     if hasattr(pip, 'main'):
#         pip.main(['install', package])
#     else:
#         pip._internal.main(['install', package])
# install('multiset')
# from multiset import Multiset


def multiset_is_subset_of(l_str, r_str):
    return Multiset(l_str).issubset(Multiset(r_str))
    
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        goodsum = 0
        l_chars = len(chars)
        for i, iter_word in enumerate(words):
            # iter_word = sortString2(iter_word)
            # if there are not enough characters to form the word, don't bother
            if len(iter_word) > l_chars:
                continue
            if Multiset(iter_word).issubset(Multiset(chars)):
                goodsum += len(iter_word)
        return goodsum

###############################################################################
#       MAIN
###############################################################################

test_words = ["cat", "bt", "hat", "tree", "cathyz"]
test_chars = "atach"
correct_ans = 6
ans = Solution().countCharacters(test_words, test_chars)
print('INPUT words: ' + str(test_words) + '   chars: ' + test_chars)
print('OUTPUT: ' + str(ans) + ' Correct: ' + str(correct_ans))
assert ans == correct_ans


test_words = ["hello","world","leetcode","impossiblylongword"]
test_chars = "welldonehoneyr"
correct_ans = 10
ans = Solution().countCharacters(test_words, test_chars)
print('INPUT words: ' + str(test_words) + '   chars: ' + test_chars)
print('OUTPUT: ' + str(ans) + ' Correct: ' + str(correct_ans))
assert ans == correct_ans


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
assert ans == correct_ans
