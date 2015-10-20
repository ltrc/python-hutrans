==============
python-hutrans
==============

Hindi-to-Urdu and Urdu-to-Hidi transliterator.

References
==========

`Dependency Parsing of Hindi and Urdu (Under Review)`_

.. _`Dependency Parsing of Hindi and Urdu (Under Review)`: https://researchweb.iiit.ac.in/~riyaz.bhat/

Installation
============

Dependencies
~~~~~~~~~~~~

`python-hutrans`_ requires `sklearn`_, `cython`_, `SciPy`_ and `python-converter-indic`.

.. _`sklearn`: https://github.com/scikit-learn/scikit-learn

.. _`cython`: http://docs.cython.org/src/quickstart/install.html

.. _`Scipy`: http://www.scipy.org/install.html

.. _`python-converter-indic`: https://github.com/irshadbhat/python-converter-indic

Download
~~~~~~~~

Download **python-hutrans**  from `github`_.

.. _`github`: https://github.com/irshadbhat/python-hutrans

Install
~~~~~~~

::

    cd python-hutrans
    sudo python setup.py install

Examples
~~~~~~~~

1. **Work with Files:**

::

    hutrans --i tests/text/urdu.txt --s urdu --o tests/urdu-dev.txt
    hutrans --i tests/text/hindi.txt --s hindi --o tests/hindi-parab.txt
    hutrans --i tests/ssf-intra/hin-ssf.txt  --s hindi --f ssf --t intra --o hin-ssf-parab.txt

    --i input     <input-file>
    --s source    source script [hindi|urdu]
    --f format    select output format [text|ssf|conll|bio|tnt]
    --t ssf-type  specify ssf-type [inter|intra] in case file format (--f) is ssf
    --o output    <output-file>    

2. **From Python**

2. **Text:**

.. code:: python

    >>> from hutrans import transliterator
    >>> trn = transliterator(format_='text', source='hindi')
    >>> 
    >>> text = """देश के कई हिस्सों में सूखे के आसार उत्पन्न हो गए हैं
    ... अब तक मौसम विभाग सामान्य बारिश होने की अपनी भविष्यवाणी पर अड़ा हुआ था लेकिन अब यह दावा पूरी तरह से खारिज हो गया है
    ... देश भर में अब तक हुई बारिश औसत से छह फीसदी कम है जबकि विभाग का दावा था कि इसमें ५ फीसदी से ज्यादा कमी नहीं होगी
    ... इसके चलते उत्तर प्रदेश पंजाब हरियाणा राजस्थान बिहार झारखंड आदि राज्य लगभग सूखे की चपेट में हैं
    ... लेकिन तकनीकी कारणों से इन्हें अभी सूखाग्रस्त घोषित नहीं किया गया है
    ... मौसम विशेषज्ञों ने माना कि यदि अगला साल भी सूखा रहा तो देश के कई हिस्सों को सूखाग्रस्त घोषित करना पड़ सकता है
    ... इस बीच बारिश नहीं होने के कारण गर्मी ने फिर अपना कहर बरपाना शुरू कर दिया तथा कई स्थानों पर तापमान ४० डिग्री सेल्सियस से ऊपर पहुंच गया है
    ... मौसम विभाग के अनुसार जून से अगस्त के तीन महीनों में देश भर में कुल ६७५ ८ मिलीमीटर बारिश हुई है जबकि इस अवधि के दौरान ७१७ ९ मिलीमीटर औसत बारिश होनी चाहिए
    ... इसमें अब तक कुल छह फीसदी की कमी है
    ... पिछले हफ्ते इसमें तीन फीसदी की कमी थी लेकिन बीते पूरे सप्ताह बारिश न होने के कारण इसमें तीन फीसदी की और बढ़ोत्तरी हुई है
    ... उत्तर प्रदेश हिमाचल राजस्थान उत्तरांचल पंजाब जम्मू कश्मीर बिहार झारखंड छत्तीसगढ़ तथा पूर्वोत्तर के कुछ राज्यों में औसत से कम बारिश हुई है
    ... इससे इन राज्यों में कृषि को भारी क्षति होने की आशंका है
    ... मानसून की सबसे बुरी स्थिति उत्तरी राज्यों में रही
    ... पश्चिमी राजस्थान में महज १४६ मिलीमीटर बारिश हुई"""
    >>> 
    >>> print trn.transform(text)
    دیش کے کئی حصوں میں سوکھے کے آثار اتپن ہو گئے ہیں
    اب تک موسم وبھاگ سامانیہ بارش ہونے کی اپنی بھوشیہوانی پر اڑا ہوا تھا لیکن اب یہ دعوی پوری طرح سے خارج ہو گیا ہے
    دیش بھر میں اب تک ہوئی بارش اوسط سے چھہ فیصدی کم ہے جبکہ وبھاگ کا دعوی تھا کہ اسمیں 5 فیصدی سے زیادہ کمی نہیں ہوگی
    اسکے چلتے اتر پردیش پنجاب ہریانا راجستھان بہار جھارکھنڈ آدی راجیہ لگبھگ سوکھے کی چپیٹ میں ہیں
    لیکن تکنیکی کارنوں سے انھیں ابھی سوکھاگرست گھوشت نہیں کیا گیا ہے
    موسم وشیشگیوں نے مانا کہ یدی اگلا سال بھی سوکھا رہا تو دیش کے کئی حصوں کو سوکھاگرست گھوشت کرنا پڑ سکتا ہے
    اس بیچ بارش نہیں ہونے کے کارن گرمی نے پھر اپنا قہر برپانا شرو کر دیا تتھا کئی ستھانوں پر تاپمان 40 ڈگری سیلسیس سے اوپر پہنچ گیا ہے
    موسم وبھاگ کے انوسار جون سے اگست کے تین مہینوں میں دیش بھر میں کل 675 8 ملیمیٹر بارش ہوئی ہے جبکہ اس اودھی کے دوران 717 9 ملیمیٹر اوسط بارش ہونی چاہئیے
    اسمیں اب تک کل چھہ فیصدی کی کمی ہے
    پچھلے ہفتے اسمیں تین فیصدی کی کمی تھی لیکن بیتے پورے سپتاہ بارش ن ہونے کے کارن اسمیں تین فیصدی کی اور بڑھوتری ہوئی ہے
    اتر پردیش ہماچل راجستھان اترانچل پنجاب جمو کشمیر بہار جھارکھنڈ چھتیسگڑھ تتھا پورووتر کے کچھ راجیوں میں اوسط سے کم بارش ہوئی ہے
    اسسے ان راجیوں میں کرشی کو بھاری شتی ہونے کی آشنکا ہے
    مانسون کی سبسے بری ستھتی اتری راجیوں میں رہی
    پچھمی راجستھان میں محض 146 ملیمیٹر بارش ہوئی
    >>> 


2. **work with conll:**

.. code:: python

    >>> trn = transliterator(format_='conll', source='hindi')
    >>> conll = """
    ...     ... 1       इसकी     यह      pn      PRP     cat-pn|gen-f|num-sg|pers-3|case-o|vib-का|tam-kA|chunkId-NP|chunkType-head|stype-|voicetype-    2     r6      _       _
    ...     ... 2       ऊँचाई     ऊँचाई     n       NN      cat-n|gen-f|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP2|chunkType-head|stype-|voicetype-     6     k1      _       _
    ...     ... 3       केवल     केवल     avy     RP      cat-avy|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP3|chunkType-child|stype-|voicetype-   4       lwg__rp _       _
    ...     ... 4       1982    1982    num     QC      cat-num|gen-any|num-any|pers-|case-any|vib-|tam-|chunkId-NP3|chunkType-child|stype-|voicetype-  5       nmod__adj       _       _
    ...     ... 5       मीटर     मीटर     n       NN      cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-head|stype-|voicetype-     6     k1s     _       _
    ...     ... 6       है       है       v       VM      cat-v|gen-any|num-sg|pers-3|case-|vib-है|tam-hE|chunkId-VGF|chunkType-head|stype-declarative|voicetype-active    0       root    _       _
    ...     ... 7       ।       ।       punc    SYM     cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-BLK|chunkType-head|stype-|voicetype-   6       rsym    _       _"""
    >>> print trn.transform(conll)
    ۔۔۔ 1       اسکی     یہ      pn      PRP     cat−pn|gen−f|num−sg|pers−3|case−o|vib−کا|tam−kA|chunkId−NP|chunkType−head|stype−|voicetype−    2     r6      _       _
        ۔۔۔ 2       اونچائی     اونچائی     n       NN      cat−n|gen−f|num−sg|pers−3|case−d|vib−0|tam−0|chunkId−NP2|chunkType−head|stype−|voicetype−     6     k1      _       _
        ۔۔۔ 3       کیول     کیول     avy     RP      cat−avy|gen−|num−|pers−|case−|vib−|tam−|chunkId−NP3|chunkType−child|stype−|voicetype−   4       lwg__rp _       _
        ۔۔۔ 4       1982    1982    num     QC      cat−num|gen−any|num−any|pers−|case−any|vib−|tam−|chunkId−NP3|chunkType−child|stype−|voicetype−  5       nmod__adj       _       _
        ۔۔۔ 5       میٹر     میٹر     n       NN      cat−n|gen−m|num−sg|pers−3|case−d|vib−0|tam−0|chunkId−NP3|chunkType−head|stype−|voicetype−     6     k1s     _       _
        ۔۔۔ 6       ہے       ہے       v       VM      cat−v|gen−any|num−sg|pers−3|case−|vib−ہے|tam−hE|chunkId−VGF|chunkType−head|stype−declarative|voicetype−active    0       root    _       _
        ۔۔۔ 7       ۔       ۔       punc    SYM     cat−punc|gen−|num−|pers−|case−|vib−|tam−|chunkId−BLK|chunkType−head|stype−|voicetype−   6       rsym    _       _

3. **work with bio or tnt:**

::

    same as conll or text

4. **work with ssf:**

::
    
    implemented for ssf files only

