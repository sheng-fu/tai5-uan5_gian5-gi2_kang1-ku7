# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.正規.阿拉伯數字 import 阿拉伯數字


class 數量單元試驗(TestCase):
    def tearDown(self):
        self.assertEqual(阿拉伯數字().轉數量('空', self.題目), self.答案)

    def test_10(self):
        self.題目 = '10'
        self.答案 = '十'

    def test_15(self):
        self.題目 = '15'
        self.答案 = '十五'

    def test_單位詞kah數量(self):
        self.題目 = '120'
        self.答案 = '百二'

    def test_數量kah單位詞kah數量(self):
        self.題目 = '2300'
        self.答案 = '兩千三'

    def test_一萬以下無0(self):
        self.題目 = '4512'
        self.答案 = '四千五百一十二'

    def test_百空(self):
        self.題目 = '602'
        self.答案 = '六百空二'

    def test_大數字(self):
        self.題目 = '1230567890980654'
        self.答案 = '一千兩百三十兆五千六百七十八億九千空九十八萬空六百五十四'

    def test_2ê(self):
        self.題目 = '2'
        self.答案 = '兩'

    def test_20ê(self):
        self.題目 = '20'
        self.答案 = '二十'

    def test_大單位(self):
        self.題目 = '2000000000000'
        self.答案 = '兩兆'

    def st_xx(self):
        問答 = [
            ('23', '二十三'),
            ('1001', '一千空一'),
            ('1020', '一千空二十'),
            ('1300', '一千三百'),  # 千三 一千三
            ('4512', '四千五百一十二'),
            ('5004', '五千空四'),
            ('6070', '六千空七十'),
            ('9800', '九千八百'),  # 九千八
            ('10800', '一萬空八百'),
            ('400000800', '四億空八百'),
            ('1230567890980654', '一千兩百三十兆五千六百七十八億九千空九十八萬空六百五十四'),
            ('1300130013', '十三億空一十三萬空一十三'),
            ('2000000022222', '兩兆空二萬兩千兩百二十二'),
            ('7900000000', '七十九億'),
            ('10000000000000000', None),
            ('0830', None),
        ]

class 阿拉伯數字單元試驗():
    def setUp(self):
        self.數字 = 阿拉伯數字()
        pass

    def tearDown(self):
        pass

    def test_轉數量(self):
        問答 = [
            ('2', '兩'),
            ('10', '十'),
            ('23', '二十三'),
            ('15', '十五'),
            ('120', '一百二十'),  # 百二 一百二
            ('230', '兩百三十'),  # 兩百三
            ('602', '六百空二'),
            ('1001', '一千空一'),
            ('1020', '一千空二十'),
            ('1200', '一千兩百'),
            ('1300', '一千三百'),  # 千三 一千三
            ('4512', '四千五百一十二'),
            ('5004', '五千空四'),
            ('6070', '六千空七十'),
            ('9800', '九千八百'),  # 九千八
            ('10800', '一萬空八百'),
            ('400000800', '四億空八百'),
            ('1230567890980654', '一千兩百三十兆五千六百七十八億九千空九十八萬空六百五十四'),
            ('1300130013', '十三億空一十三萬空一十三'),
            ('2000000022222', '兩兆空二萬兩千兩百二十二'),
            ('2000000000000', '兩兆'),
            ('7900000000', '七十九億'),
            ('10000000000000000', None),
            ('0830', None),
        ]
        self.檢查數量(問答)

    def test_轉兩佮二的數量(self):
        問答 = [
            ('12', '十二'),
            ('120', '一百二十'),
            ('3200', '三千兩百'),
            ('42000', '四萬兩千'),
            ('920000', '九十二萬'),
            ('1200000', '一百二十萬'),
            ('12000000', '一千兩百萬'),
            ('32000000', '三千兩百萬'),
            ('200000000', '兩億'),
            ('820000000', '八億兩千萬'),
        ]
        self.檢查數量(問答)

    def test_轉閩南語數量省一佮單位(self):
        問答 = [
            ('兩百三十', '兩百三'),
            ('六百空二', None),
            ('一千空一', None),
            ('一千空一十', '一千空十'),
            ('一千空二十', None),
            ('一千一百一十', '一千一百一'),
            ('一千兩百', '千二'),
            ('一千三百', '千三'),
            ('一千三百一十三', '一千三百十三'),
            ('四千五百一十二', '四千五百十二'),
            ('五千空四', None),
            ('六千空七十', None),
            ('九千八百', '九千八'),
            ('十三萬空一十三', '十三萬空十三'),
            ('一兆空一十六萬七千', '一兆空十六萬七'),
            ('七十九億', None),
        ]
        self.檢查閩南語數量(問答)

    def test_轉閩南語兩佮二數量(self):
        問答 = [
            ('十二', None),
            ('一百二十', '百二'),
            ('一千兩百', '千二'),
            ('三千兩百', '三千二'),
            ('四萬兩千', '四萬二'),
            ('九十二萬', None),
            ('八億兩千萬', None),
            ('一百二十萬', '百二萬'),
            ('一千兩百萬', '千二萬'),
            ('三千兩百萬', None),
            ('兩億', None),
            ('一千兩百億', '千二億'),
            ('三千兩百億', None),
        ]
        self.檢查閩南語數量(問答)

    def test_轉客家話數量省單位(self):
        問答 = [
            ('一百二十', '百二'),
            ('兩百三十', '兩百三'),
            ('六百零二', None),
            ('一千零一', None),
            ('一千零一十', None),
            ('一千零二十', None),
            ('一千一百一十', '一千一百一'),
            ('一千兩百', '千二'),
            ('一千三百', '千三'),
            ('一千三百一十三', None),
            ('四千五百一十二', None),
            ('五千零四', None),
            ('六千零七十', None),
            ('九千八百', '九千八'),
            ('十三億零一十三萬零一十三', None),
            ('一兆零一十六萬七千', '一兆零一十六萬七'),
            ('七十九億', None),
        ]
        self.檢查客家話數量(問答)

    def test_轉官話數量省上尾單位(self):
        問答 = [
            ('一百二十', '一百二'),
            ('兩百三十', '兩百三'),
            ('六百零二', None),
            ('一千零一', None),
            ('一千零一十', None),
            ('一千零二十', None),
            ('一千一百一十', '一千一百一'),
            ('一千兩百', '一千二'),
            ('一千三百', '一千三'),
            ('一千三百一十三', None),
            ('四千五百一十二', None),
            ('五千零四', None),
            ('六千零七十', None),
            ('九千八百', '九千八'),
            ('十三億零一十三萬零一十三', None),
            ('一兆零一十六萬七千', '一兆零一十六萬七'),
            ('七十九億', None),
        ]
        self.檢查官話數量(問答)

    def test_轉官話兩佮二數量(self):
        問答 = [
            ('十二', None),
            ('一百二十', '一百二'),
            ('一千兩百', '一千二'),
            ('三千兩百', '三千二'),
            ('四萬兩千', '四萬二'),
            ('九十二萬', None),
            ('八億兩千萬', None),
            ('一百二十萬', None),
            ('一千兩百萬', None),
            ('三千兩百萬', None),
            ('兩億', None),
        ]
        self.檢查官話數量(問答)

    def 檢查數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.是數量無(問), False, 問)
                self.assertEqual(self.數字.轉數量('空', 問), 問)
            else:
                self.assertEqual(self.數字.是數量無(問), True)
                self.assertEqual(self.數字.轉數量('空', 問), 答, 問)
                self.assertEqual(self.數字.轉數量('零', 問),
                                 答.replace('空', '零'), 問)

    def 檢查閩南語數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.轉閩南語數量無(問), False, 問)
                self.assertEqual(self.數字.轉閩南語數量(問), 問)
            else:
                self.assertEqual(self.數字.轉閩南語數量無(問), True, 問)
                self.assertEqual(self.數字.轉閩南語數量(問), 答, 問)

    def 檢查客家話數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.轉客家話數量無(問), False, 問)
                self.assertEqual(self.數字.轉客家話數量(問), 問)
            else:
                self.assertEqual(self.數字.轉客家話數量無(問), True, 問)
                self.assertEqual(self.數字.轉客家話數量(問), 答, 問)

    def 檢查官話數量(self, 問答):
        for 問, 答 in 問答:
            if 答 is None:
                self.assertEqual(self.數字.轉官話數量無(問), False, 問)
                self.assertEqual(self.數字.轉官話數量(問), 問)
            else:
                self.assertEqual(self.數字.轉官話數量無(問), True, 問)
                self.assertEqual(self.數字.轉官話數量(問), 答, 問)
