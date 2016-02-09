# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔


class 詞物件網仔單元試驗(unittest.TestCase):

    @patch('臺灣言語工具.基本物件.句.句.網出詞物件')
    def test_篩出字物件(self, 網出詞物件mock):
        物件 = 拆文分析器.分詞句物件('頭-家｜thau5-ke1 員-工｜uan5-kang1')
        詞物件網仔.網出詞物件(物件)
        網出詞物件mock.assert_called_once_with()

    def test_網字(self):
        型 = '媠'
        字物件 = 拆文分析器.建立字物件(型)
        self.assertEqual(詞物件網仔.網出詞物件(字物件), 拆文分析器.建立詞物件(型))

    def test_網詞(self):
        型 = '媠'
        詞物件 = 拆文分析器.建立詞物件(型)
        self.assertEqual(詞物件網仔.網出詞物件(詞物件), [詞物件])

    def test_網詞無字(self):
        型 = ''
        詞物件 = 拆文分析器.建立詞物件(型)
        self.assertEqual(詞物件網仔.網出詞物件(詞物件), [詞物件])

    def test_網詞濟字漢字(self):
        語句 = '椅仔！'
        self.assertEqual(
            詞物件網仔.網出詞物件(拆文分析器.建立詞物件(語句)),
            [拆文分析器.建立詞物件(語句)])

    def test_網詞濟字音標(self):
        語句 = 'tsit8-tiunn1 !'
        self.assertEqual(
            詞物件網仔.網出詞物件(拆文分析器.建立詞物件(語句)),
            [拆文分析器.建立詞物件(語句)])

    def test_網詞濟字漢羅(self):
        語句 = 'tsit8-張!'
        self.assertEqual(
            詞物件網仔.網出詞物件(拆文分析器.建立詞物件(語句)),
            [拆文分析器.建立詞物件(語句)])

    def test_網組孤字(self):
        語句 = '媠'
        切好語句 = ['媠']
        self.網組集句章看覓(語句, 切好語句)

    def test_網無字(self):
        語句 = ''
        切好語句 = []
        self.網組集句章看覓(語句, 切好語句)

    def test_網濟音標(self):
        語句 = 'gua2 u7 tsit8-tiunn1 i2-a2'
        切好語句 = ['gua2', 'u7', 'tsit8-tiunn1', 'i2-a2']
        self.網組集句章看覓(語句, 切好語句)

    def test_網濟漢羅(self):
        語句 = 'gua2 有 tsit8-tiunn1 椅-仔'
        切好語句 = ['gua2', '有', 'tsit8-tiunn1', '椅仔']
        self.網組集句章看覓(語句, 切好語句)

    def test_網濟字輕聲(self):
        語句 = 'mi2-kiann7 boo5-0ki3 ah ! '
        切好語句 = ['mi2-kiann7', 'boo5-0ki3', 'ah', '!']
        self.網組集句章看覓(語句, 切好語句)

    def test_網濟連字佮符號(self):
        語句 = '枋-寮漁-港「大-條-巷」。上-闊兩-公-尺'
        切好語句 = ['枋寮', '漁港', '「', '大條巷', '」', '。', '上闊', '兩公尺']
        self.網組集句章看覓(語句, 切好語句)

    def 網組集句章看覓(self, 語句, 切好語句):
        切好詞陣列 = []
        for 語詞 in 切好語句:
            切好詞陣列.append(拆文分析器.建立詞物件(語詞))
        self.assertEqual(
            詞物件網仔.網出詞物件(拆文分析器.建立組物件(語句)),
            切好詞陣列)
        self.assertEqual(
            詞物件網仔.網出詞物件(拆文分析器.建立集物件(語句)),
            切好詞陣列)
        self.assertEqual(
            詞物件網仔.網出詞物件(拆文分析器.建立句物件(語句)),
            切好詞陣列)
        self.assertEqual(
            詞物件網仔.網出詞物件(拆文分析器.建立章物件(語句)),
            切好詞陣列)

    def test_網集濟組(self):
        原來語句 = '我有一張椅仔！'
        組陣列 = [拆文分析器.建立組物件(原來語句),
               拆文分析器.建立組物件(原來語句), ]
        self.assertRaises(解析錯誤, 詞物件網仔.網出詞物件, 集(組陣列))

    def test_網章濟句(self):
        原來語句 = '我有一張椅仔！'
        句陣列 = [拆文分析器.建立句物件(原來語句)] * 2
        self.assertEqual(詞物件網仔.網出詞物件(章(句陣列)),
                         詞物件網仔.網出詞物件(拆文分析器.建立句物件(原來語句)) * 2)

    def test_烏白擲物件(self):
        self.assertRaises(型態錯誤, 詞物件網仔.網出詞物件, 2123)
        self.assertRaises(型態錯誤, 詞物件網仔.網出詞物件, '詞物件網仔')
        self.assertRaises(型態錯誤, 詞物件網仔.網出詞物件, None)
