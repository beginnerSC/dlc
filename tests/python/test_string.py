"""Unit tests for string functions."""
from dlc.string import (
    reverseWords, isAnagram, isAnagram1, 
    longestPalindrome, countSubstrings, isValid
)


class TestReverseWords:
    def test_basic_case(self):
        """Test reversing words in a basic string."""
        assert reverseWords("the sky is blue") == "blue is sky the"
    
    def test_extra_spaces(self):
        """Test with extra spaces."""
        assert reverseWords("  hello world  ") == "world hello"
    
    def test_multiple_spaces(self):
        """Test with multiple spaces between words."""
        assert reverseWords("a good   example") == "example good a"


class TestIsAnagram:
    def test_valid_anagram(self):
        """Test valid anagram."""
        assert isAnagram("anagram", "nagaram") == True
        assert isAnagram1("anagram", "nagaram") == True
    
    def test_not_anagram(self):
        """Test invalid anagram."""
        assert isAnagram("rat", "car") == False
        assert isAnagram1("rat", "car") == False
    
    def test_different_lengths(self):
        """Test strings of different lengths."""
        assert isAnagram("a", "ab") == False


class TestLongestPalindrome:
    def test_odd_length_palindrome(self):
        """Test odd-length palindrome."""
        result = longestPalindrome("babad")
        assert result in ["bab", "aba"]
    
    def test_even_length_palindrome(self):
        """Test even-length palindrome."""
        assert longestPalindrome("cbbd") == "bb"
    
    def test_single_char(self):
        """Test single character."""
        assert longestPalindrome("a") == "a"


class TestCountSubstrings:
    def test_basic_case(self):
        """Test counting palindromic substrings."""
        assert countSubstrings("abc") == 3  # a, b, c
    
    def test_multiple_palindromes(self):
        """Test with multiple palindromes."""
        assert countSubstrings("aaa") == 6  # a, a, a, aa, aa, aaa


class TestIsValid:
    def test_valid_parentheses(self):
        """Test valid parentheses."""
        assert isValid("()") == True
        assert isValid("()[]{}") == True
        assert isValid("{[]}") == True
    
    def test_invalid_parentheses(self):
        """Test invalid parentheses."""
        assert isValid("(]") == False
        assert isValid("([)]") == False
        assert isValid("]") == False
    
    def test_empty_string(self):
        """Test empty string."""
        assert isValid("") == True
