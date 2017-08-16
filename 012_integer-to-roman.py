class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_num = ""
        roman_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        dec_roman_list = [1000, 500, 100, 50, 10, 5, 1]
        roman_index = 0
        max_roman = dec_roman_list[roman_index]

        while num:
            if num >= max_roman:
                roman_num += roman_dict[max_roman]
                num = num - max_roman
            else:
                roman_index += 1
                max_roman = dec_roman_list[roman_index]
        roman_num = roman_num.replace("DCCCC", "CM") # 900
        roman_num = roman_num.replace("CCCC", "CD") # 400
        roman_num = roman_num.replace("LXXXX", "XC") # 90
        roman_num = roman_num.replace("XXXX", "XL") # 40
        roman_num = roman_num.replace("VIIII", "IX") # 9
        roman_num = roman_num.replace("IIII", "IV") # 4
        return roman_num

print(Solution().intToRoman(149))