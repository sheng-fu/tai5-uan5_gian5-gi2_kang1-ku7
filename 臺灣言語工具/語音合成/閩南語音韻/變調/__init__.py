from 臺灣言語工具.語音合成.閩南語音韻.變調.類型 import 變調規則表
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤


規則變調 = 變調規則表(
    名='規則變調',
    喉入聲變調規則={'4': '2', '8': '3'},
    入聲變調規則={'4': '8', '8': '10'},
    變調規則={'1': '7', '2': '1', '3': '2', '5': '7', '7': '3', '9': '9'},
)

三連音變調 = 變調規則表(
    名='三連音變調',
    喉入聲變調規則={'4': '2', '8': '9'},
    入聲變調規則={'4': '8', '8': '9'},
    變調規則={'1': '9', '2': '1', '3': '2', '5': '9', '7': '9'},
)

仔前變調 = 變調規則表(
    名='仔前變調',
    喉入聲變調規則={'4': '1', '8': '7'},
    入聲變調規則={'4': '8', '8': '4'},
    變調規則={'1': '7', '2': '1', '3': '1', '5': '7', '7': '7'},
)
輕聲 = 變調規則表(
    名='輕聲',
    喉入聲變調規則={'4': '3', '8': '3', '0': '3'},
    入聲變調規則={'4': '10', '8': '10', '0': '10'},
    變調規則={'1': '3', '2': '3', '3': '3', '5': '3', '7': '3', '0': '3'},
)


class 再變調:

    @classmethod
    def 變調(cls, 音):
        return 規則變調.變調(規則變調.變調(音))


class 無調符號:

    @classmethod
    def 變調(cls, 音):
        return 音


class 維持本調:

    @classmethod
    def 變調(cls, 音):
        return 音


class 隨前變調:
    對應表 = {
        '1': '1', '2': '3', '3': '3', '4': '3',
        '5': '7', '7': '7', '8': '3'
    }

    def __init__(self, 頂一个調):
        self._變調後輕聲音 = self.對應表[頂一个調]

    def __eq__(self, 別的):
        try:
            return self._變調後輕聲音 == 別的._變調後輕聲音
        except AttributeError:
            return False

    def 變調(self, 音):
        聲, 韻, 調 = 音
        if 韻.endswith('p') or 韻.endswith('t') or 韻.endswith('k'):
            raise 解析錯誤('入聲毋知愛按怎隨前變調！！{0}'.format((聲, 韻, 調)))
        return (聲, 韻.rstrip('hʔ'), self._變調後輕聲音)
