# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本元素.公用變數 import 分型音符號
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
'''
完整
欠詞
欠字
	農民 運動 在 當年 的 520 達到 最高潮 ， 但是 結果 農民 的 困境 從 沒 被 解決 。
欠字典
'''
class 斷詞斷字翻譯:
# 	辭典揣詞,語句連詞
	_分析器 = 拆文分析器()
	_譀鏡 = 物件譀鏡()
	def 譯(self, 斷詞用戶端, 斷字用戶端, 編碼器, 物件):
		if isinstance(物件, 章):
			return self.譯章(斷詞用戶端, 斷字用戶端, 編碼器, 物件)
		if isinstance(物件, 句):
			return self.譯句(斷詞用戶端, 斷字用戶端, 編碼器, 物件, 揀幾个上好=0)
		raise 型態錯誤('翻譯愛句物件抑是章物件！傳入來的是{0}，{1}'
				.format(type(物件),物件))
	def 譯章(self, 斷詞用戶端, 斷字用戶端, 編碼器, 章物件):
		'''直接選翻上好的，免逐句生幾仔句'''
		結果章物件 = self._分析器.建立章物件('')
		for 句物件 in 章物件.內底句:
			結果章物件.append(
				self.譯句(斷詞用戶端, 斷字用戶端, 編碼器, 句物件, 揀幾个上好 = 0))
		return 結果章物件
	def 譯句(self, 斷詞用戶端, 斷字用戶端, 編碼器, 句物件, 揀幾个上好 = 0):
		一句 = self._譀鏡.看斷詞(句物件)
		翻譯結果 = 斷詞用戶端.翻譯(
			一句, 編碼器, 另外參數 = {'nbest':揀幾个上好})
		if 揀幾个上好 < 1:
			return self._整理斷詞翻譯的結果(
				斷詞用戶端, 斷字用戶端, 編碼器,
				翻譯結果['text'])
		全部句 = []
		for 上好句 in 翻譯結果['nbest']:
			結果句物件 = self._整理斷詞翻譯的結果(
				斷詞用戶端, 斷字用戶端, 編碼器,
				上好句['hyp'])
			全部句.append(結果句物件)
		return 全部句
	def _整理斷詞翻譯的結果(self, 斷詞用戶端, 斷字用戶端, 編碼器,
			斷詞翻譯結果):
		句物件 = self._分析器.建立句物件('')
# 		print('上好句', 斷詞翻譯結果)
		for 一个詞 in 斷詞翻譯結果.split():
			集物件 = self._分析器.建立集物件('')
			if 斷詞用戶端.是未知詞(一个詞):
				愛翻詞 = 斷詞用戶端.提掉後壁未知詞記號(一个詞)
# 				print(愛翻詞)
				詞物件 = self._斷字翻譯一詞(斷字用戶端, 編碼器, 愛翻詞)
				組物件 = self._分析器.建立組物件('')
				組物件.內底詞.append(詞物件)
				集物件 = self._分析器.建立集物件('')
				集物件.內底組.append(組物件)
				句物件.內底集.append(集物件)
			else:
# 				print('一个詞', 一个詞)
				集物件 = self._分析器.轉做集物件(一个詞)
				句物件.內底集.append(集物件)
		return 句物件
	def _斷字翻譯一詞(self, 斷字用戶端, 編碼器, 愛翻詞):
		詞物件 = self._分析器.建立詞物件('')
		翻譯結果 = 斷字用戶端.翻譯(
				' '.join(愛翻詞), 編碼器,)
		for 斷詞 in 翻譯結果['text'].split():
			if 斷字用戶端.是未知詞(斷詞):
				漢字 = 斷字用戶端.提掉後壁未知詞記號(斷詞).split(分型音符號)[0]
				字物件 = self._分析器.產生對齊字(
					漢字, 漢字
					)
				詞物件.內底字.append(字物件)
			else:
				字物件 = self._分析器.轉做字物件(斷詞)
				詞物件.內底字.append(字物件)
		return 詞物件
