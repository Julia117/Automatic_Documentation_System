# Language (class)

**Code:**
```python
class Language(str, Enum):
    German: str = 'de'
    Greek: str = 'el'
    English: str = 'en'
    Spanish: str = 'es'
    French: str = 'fr'
    Italian: str = 'it'
    Hebrew: str = 'he'
    Japanese: str = 'ja'
    Korean: str = 'ko'
    Portuguese: str = 'pt'
    Russian: str = 'ru'
    Ukrainian: str = 'uk'
    Chinese: str = 'zh'
    Arabic: str = 'ar'
    Latin: str = 'la'
    Turkish: str = 'tr'
    Afrikaans: str = 'af'
    TwiAkan: str = 'ak'
    Amharic: str = 'am'
    Assamese: str = 'as'
    Aymara: str = 'ay'
    Azerbaijani: str = 'az'
    Belarusian: str = 'be'
    Bulgarian: str = 'bg'
    Bhojpuri: str = 'bho'
    Bambara: str = 'bm'
    Bengali: str = 'bn'
    Bosnian: str = 'bs'
    Catalan: str = 'ca'
    Cebuano: str = 'ceb'
    KurdishSorani: str = 'ckb'
    Corsican: str = 'co'
    Czech: str = 'cs'
    Welsh: str = 'cy'
    Danish: str = 'da'
    Dogri: str = 'doi'
    Dhivehi: str = 'dv'
    Ewe: str = 'ee'
    Esperanto: str = 'eo'
    Estonian: str = 'et'
    Basque: str = 'eu'
    Persian: str = 'fa'
    Finnish: str = 'fi'
    FilipinoTagalog: str = 'fil'
    Frisian: str = 'fy'
    Irish: str = 'ga'
    ScotsGaelic: str = 'gd'
    Galician: str = 'gl'
    Guarani: str = 'gn'
    Konkani: str = 'gom'
    Gujarati: str = 'gu'
    Hausa: str = 'ha'
    Hawaiian: str = 'haw'
    Hindi: str = 'hi'
    Hmong: str = 'hmn'
    Croatian: str = 'hr'
    HaitianCreole: str = 'ht'
    Hungarian: str = 'hu'
    Armenian: str = 'hy'
    Indonesian: str = 'id'
    Igbo: str = 'ig'
    Ilocano: str = 'ilo'
    Icelandic: str = 'is'
    Javanese: str = 'jv'
    Georgian: str = 'ka'
    Kazakh: str = 'kk'
    Khmer: str = 'km'
    Kannada: str = 'kn'
    Krio: str = 'kri'
    Kurdish: str = 'ku'
    Kyrgyz: str = 'ky'
    Luxembourgish: str = 'lb'
    Luganda: str = 'lg'
    Lingala: str = 'ln'
    Lao: str = 'lo'
    Lithuanian: str = 'lt'
    Mizo: str = 'lus'
    Latvian: str = 'lv'
    Maithili: str = 'mai'
    Malagasy: str = 'mg'
    Maori: str = 'mi'
    Macedonian: str = 'mk'
    Malayalam: str = 'ml'
    Mongolian: str = 'mn'
    MeiteilonManipuri: str = 'mni-mtei'
    Marathi: str = 'mr'
    Malay: str = 'ms'
    Maltese: str = 'mt'
    MyanmarBurmese: str = 'my'
    Nepali: str = 'ne'
    Dutch: str = 'nl'
    Norwegian: str = 'no'
    Sepedi: str = 'nso'
    NyanjaChichewa: str = 'ny'
    Oromo: str = 'om'
    OdiaOriya: str = 'or'
    Punjabi: str = 'pa'
    Polish: str = 'pl'
    Pashto: str = 'ps'
    Quechua: str = 'qu'
    Romanian: str = 'ro'
    Kinyarwanda: str = 'rw'
    Sanskrit: str = 'sa'
    Sindhi: str = 'sd'
    SinhalaSinhalese: str = 'si'
    Slovak: str = 'sk'
    Slovenian: str = 'sl'
    Samoan: str = 'sm'
    Shona: str = 'sn'
    Somali: str = 'so'
    Albanian: str = 'sq'
    Serbian: str = 'sr'
    Sesotho: str = 'st'
    Sundanese: str = 'su'
    Swedish: str = 'sv'
    Swahili: str = 'sw'
    Tamil: str = 'ta'
    Telugu: str = 'te'
    Tajik: str = 'tg'
    Thai: str = 'th'
    Tigrinya: str = 'ti'
    Turkmen: str = 'tk'
    TagalogFilipino: str = 'tl'
    Tsonga: str = 'ts'
    Tatar: str = 'tt'
    Uyghur: str = 'ug'
    Urdu: str = 'ur'
    Uzbek: str = 'uz'
    Vietnamese: str = 'vi'
    Xhosa: str = 'xh'
    Yiddish: str = 'yi'
    Yoruba: str = 'yo'
    ChineseTraditional: str = 'zh-tw'
    Zulu: str = 'zu'
    Cantonese: str = 'yue'
```

**Explanation:**
**`Language` – a string‑based enum of language codes**

- `class Language(str, Enum)`  
  * Inherits from both `str` and `Enum`.  
  * Each member is a language name (e.g., `English`) whose value is the ISO‑639‑1 two‑letter code (`'en'`).  
  * Because it subclasses `str`, you can use a member wherever a plain string is expected (e.g., `Language.English == 'en'`).

**Why use it?**

- Keeps language codes in one place, avoiding hard‑coded strings scattered through the codebase.  
- Provides type safety: functions that expect a language can declare `lang: Language`.  
- Supports iteration, lookup, and serialization out of the box.

**Typical usage**

```python
def translate(text: str, lang: Language) -> str:
    # lang is a Language enum member, e.g., Language.English
    code = lang.value   # 'en'
    # … call translation API with code …
```

**Key points**

- Every language listed (German, Greek, English, …, Cantonese) is a member.  
- The value is the standard two‑letter code, except for a few special cases (`zh-tw` for Traditional Chinese, `yue` for Cantonese).  
- Because it’s a `str` subclass, you can compare it directly to strings or use it in string formatting.

**Imports:**
```
from enum import Enum
```
