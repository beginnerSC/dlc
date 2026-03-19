"""Unit tests for string functions."""
from dlc.string import (
    reverseWords, isAnagram, isAnagram1,
    longestPalindrome, countSubstrings, isValid,
    isPalindrome,
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


class TestIsPalindrome:
    def test_canonical_true(self):
        """LeetCode 125 example: alphanumeric palindrome with punctuation."""
        assert isPalindrome("A man, a plan, a canal: Panama") == True

    def test_canonical_false(self):
        """LeetCode 125 example: not a palindrome."""
        assert isPalindrome("race a car") == False

    def test_empty_string(self):
        """Empty string is a palindrome."""
        assert isPalindrome("") == True

    def test_only_non_alphanumeric(self):
        """Only punctuation/spaces — treated as empty after stripping."""
        assert isPalindrome(" ") == True
        assert isPalindrome(".,!?") == True

    def test_single_character(self):
        assert isPalindrome("a") == True
        assert isPalindrome("1") == True

    def test_case_insensitive(self):
        """Case should not matter."""
        assert isPalindrome("AbA") == True
        assert isPalindrome("AbBa") == True

    def test_digits(self):
        """Numeric palindrome."""
        assert isPalindrome("12321") == True
        assert isPalindrome("12345") == False

    def test_mixed_alphanumeric(self):
        """Digits and letters together."""
        assert isPalindrome("0P0") == True
        assert isPalindrome("0P1") == False


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
