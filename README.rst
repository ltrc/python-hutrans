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

`python-hutrans`_ requires `sklearn`_, `cython`_, `SciPy`_ and `indic-wx-converter`_.

.. _`sklearn`: https://github.com/scikit-learn/scikit-learn

.. _`cython`: http://docs.cython.org/src/quickstart/install.html

.. _`Scipy`: http://www.scipy.org/install.html

.. _`indic-wx-converter`: https://github.com/irshadbhat/indic-wx-converter

To install the dependencies do something like (Ubuntu):

::

    sudo apt-get install python-sklearn
    sudo apt-get install cython
    sudo apt-get install python-scipy

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

.. parsed-literal::

    hutrans --i tests/text/urdu.txt --s urdu --o tests/urdu-dev.txt
    hutrans --i tests/text/hindi.txt --s hindi --o tests/hindi-parab.txt
    hutrans --i tests/ssf-intra/hin-ssf.txt  --s hindi --f ssf --t intra --o hin-ssf-parab.txt
    hutrans --i tests/ssf-intra/hin-ssf.txt  --s hindi --f ssf --t inter --n --o hin-ssf-parab.txt

    --i input     <input-file>
    --s source    source script [hindi|urdu]
    --f format    select output format [text|ssf|conll|bio|tnt]
    --t ssf-type  specify ssf-type [inter|intra] in case file format (--f) is ssf
    --n		  set this flag for nested ssf
    --o output    <output-file>    

    irshad@python-hutrans$ cat tests/text/hindi.txt 
    देश के कई हिस्सों में सूखे के आसार उत्पन्न हो गए हैं
    लेकिन तकनीकी कारणों से इन्हें अभी सूखाग्रस्त घोषित नहीं किया गया है
    इसमें अब तक कुल छह फीसदी की कमी है
    इससे इन राज्यों में कृषि को भारी क्षति होने की आशंका है
    मानसून की सबसे बुरी स्थिति उत्तरी राज्यों में रही
    पश्चिमी राजस्थान में महज १४६ मिलीमीटर बारिश हुई
    irshad@python-hutrans$ hutrans < tests/text/hindi.txt 
    دیش کے کئی حصوں میں سوکھے کے آثار اتپن ہو گئے ہیں
    لیکن تکنیکی کارنوں سے انھیں ابھی سوکھاگرست گھوشت نہیں کیا گیا ہے
    اسمیں اب تک کل چھہ فیصدی کی کمی ہے
    اسسے ان راجیوں میں کرشی کو بھاری شتی ہونے کی آشنکا ہے
    مانسون کی سبسے بری ستھتی اتری راجیوں میں رہی
    پچھمی راجستھان میں محض 146 ملیمیٹر بارش ہوئی

    irshad@python-hutrans$ cat tests/conll/hin-conll.txt 
    1   यहाँ	यहाँ  pn	PRP cat-pn|gen-|num-|pers-|case-o|vib-0_से|tam-|chunkId-NP|chunkType-head|stype-|voicetype-  5	nmod	__
    2   से	से   psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP|chunkType-child|stype-|voicetype-    1	lwg__psp    _	_
    3   5	5   num	QC  cat-num|gen-any|num-any|pers-|case-any|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-  4	nmod__adj   _	_
    4   किमी	किमी  n	NN  cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP2|chunkType-child|stype-|voicetype-	5   nmod__adj	_   _
    5   दूरी	दूरी  n	NN  cat-n|gen-f|num-sg|pers-3|case-o|vib-0_पर|tam-0|chunkId-NP2|chunkType-head|stype-|voicetype-    7	jjmod	_   _
    6   पर	पर  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-   5	lwg__psp    _	_
    7   स्थित	स्थित adj	JJ  cat-adj|gen-any|num-any|pers-|case-d|vib-|tam-|chunkId-JJP|chunkType-head|stype-|voicetype-	9   nmod    _	_
    8   वासुकि	वासुकि n	NNPC	cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-child|stype-|voicetype-  9	pof__cn	_   _
    9   ताल	ताल  n	NNP cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-head|stype-|voicetype-	25  k1	_   _
    10  अपने	अपना pn	PRP cat-pn|gen-m|num-any|pers-any|case-o|vib-0|tam-0|chunkId-NP4|chunkType-head|stype-|voicetype-   12	r6  _	_
    11  पारदर्शी   पारदर्शी   adj	JJ  cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP5|chunkType-child|stype-|voicetype-    12	nmod__adj   _	_
    12  जल	जल  n	NN  cat-n|gen-m|num-sg|pers-3|case-o|vib-0|tam-0|chunkId-NP5|chunkType-head|stype-|voicetype-	13  ccof    _	_
    13  और	और  avy	CC  cat-avy|gen-|num-|pers-|case-|vib-|tam-|chunkId-CCP|chunkType-head|stype-|voicetype-    25	rt  __
    14  उसमें	वह  pn	PRP cat-pn|gen-any|num-sg|pers-3|case-o|vib-में|tam-meM|chunkId-NP6|chunkType-head|stype-|voicetype-  17	k7  _	_
    15  डूबते	डूब  v	VMC cat-v|gen-m|num-pl|pers-any|case-|vib-ता|tam-wA|chunkId-VGNF|chunkType-child|stype-|voicetype-   17	pof__cv	_   _
    16  -	-   punc    SYM	cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-VGNF|chunkType-child|stype-|voicetype-	17  rsym    __
    17  उतराते    उतरा	v   VM	cat-v|gen-m|num-pl|pers-any|case-|vib-ता|tam-wA|chunkId-VGNF|chunkType-head|stype-|voicetype-	18  nmod__k1inv	_   _
    18  हिमखंडों    हिमखंड    n	NN  cat-n|gen-m|num-pl|pers-3|case-o|vib-0_का|tam-0|chunkId-NP7|chunkType-head|stype-|voicetype-	21  r6	_   _
    19  के	का   psp	PSP cat-psp|gen-m|num-pl|pers-|case-o|vib-|tam-|chunkId-NP7|chunkType-child|stype-|voicetype-	18  lwg__psp	_   _
    20  अद्भुत    अद्भुत    adj	JJ  cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-    21	nmod__adj   _	_
    21  दृश्यों	दृश्य n	NN  cat-n|gen-m|num-pl|pers-3|case-o|vib-0_के_लिए|tam-0|chunkId-NP8|chunkType-head|stype-|voicetype-  13	ccof	_   _
    22  के	के   psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21	lwg__psp    _	_
    23  लिए	लिए  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21	lwg__psp    _	_
    24  विख्यात    विख्यात    adj	JJ  cat-adj|gen-any|num-any|pers-|case-|vib-|tam-|chunkId-JJP2|chunkType-head|stype-|voicetype-	25  k1s	_   _
    25  है	है   v	VM  cat-v|gen-any|num-sg|pers-3|case-|vib-है|tam-hE|chunkId-VGF|chunkType-head|stype-declarative|voicetype-active    0	root	_   _
    26  ।	।   punc    SYM	cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-BLK|chunkType-head|stype-|voicetype-	25  rsym    __
    irshad@python-hutrans$ hutrans < tests/conll/hin-conll.txt --f conll
    1   یہاں    یہاں    pn	PRP cat-pn|gen-|num-|pers-|case-o|vib-0_سے|tam-|chunkId-NP|chunkType-head|stype-|voicetype- 5	nmod	__
    2   سے	سے  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP|chunkType-child|stype-|voicetype-    1	lwg__psp    _	_
    3   5	5   num	QC  cat-num|gen-any|num-any|pers-|case-any|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-  4	nmod__adj   _	_
    4   کمی	کمی n	NN  cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP2|chunkType-child|stype-|voicetype-	5   nmod__adj	_   _
    5   دوری    دوری    n	NN  cat-n|gen-f|num-sg|pers-3|case-o|vib-0_پر|tam-0|chunkId-NP2|chunkType-head|stype-|voicetype-    7	jjmod	_   _
    6   پر	پر  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-   5	lwg__psp    _	_
    7   ستھت    ستھت    adj	JJ  cat-adj|gen-any|num-any|pers-|case-d|vib-|tam-|chunkId-JJP|chunkType-head|stype-|voicetype-	9   nmod    _	_
    8   واسکی   واسکی   n	NNPC	cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-child|stype-|voicetype-  9	pof__cn	_   _
    9   تال	تال n	NNP cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-head|stype-|voicetype-	25  k1	_   _
    10  اپنے    اپنا    pn	PRP cat-pn|gen-m|num-any|pers-any|case-o|vib-0|tam-0|chunkId-NP4|chunkType-head|stype-|voicetype-   12	r6  _	_
    11  پاردرشی پاردرشی adj	JJ  cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP5|chunkType-child|stype-|voicetype-    12	nmod__adj   _	_
    12  جل	جل  n	NN  cat-n|gen-m|num-sg|pers-3|case-o|vib-0|tam-0|chunkId-NP5|chunkType-head|stype-|voicetype-	13  ccof    _	_
    13  اور	اور avy	CC  cat-avy|gen-|num-|pers-|case-|vib-|tam-|chunkId-CCP|chunkType-head|stype-|voicetype-    25	rt  __
    14  اسمیں   وہ	pn  PRP	cat-pn|gen-any|num-sg|pers-3|case-o|vib-میں|tam-meM|chunkId-NP6|chunkType-head|stype-|voicetype-    17	k7  _	_
    15  ڈوبتے   ڈوب	v   VMC	cat-v|gen-m|num-pl|pers-any|case-|vib-تا|tam-wA|chunkId-VGNF|chunkType-child|stype-|voicetype-	17  pof__cv _	_
    16  −	−   punc    SYM	cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-VGNF|chunkType-child|stype-|voicetype-	17  rsym    __
    17  اتراتے  اترا    v	VM  cat-v|gen-m|num-pl|pers-any|case-|vib-تا|tam-wA|chunkId-VGNF|chunkType-head|stype-|voicetype-   18	nmod__k1inv _	_
    18  ہمکھنڈوں	ہمکھنڈ	n   NN	cat-n|gen-m|num-pl|pers-3|case-o|vib-0_کا|tam-0|chunkId-NP7|chunkType-head|stype-|voicetype-	21  r6	_   _
    19  کے	کا  psp	PSP cat-psp|gen-m|num-pl|pers-|case-o|vib-|tam-|chunkId-NP7|chunkType-child|stype-|voicetype-	18  lwg__psp	_   _
    20  ادبھت   ادبھت   adj	JJ  cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-    21	nmod__adj   _	_
    21  درشیوں  درشیہ   n	NN  cat-n|gen-m|num-pl|pers-3|case-o|vib-0_کے_لئے|tam-0|chunkId-NP8|chunkType-head|stype-|voicetype-	13  ccof    _	_
    22  کے	کے  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21	lwg__psp    _	_
    23  لئے	لئے psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21	lwg__psp    _	_
    24  وکھیات  وکھیات  adj	JJ  cat-adj|gen-any|num-any|pers-|case-|vib-|tam-|chunkId-JJP2|chunkType-head|stype-|voicetype-	25  k1s	_   _
    25  ہے	ہے  v	VM  cat-v|gen-any|num-sg|pers-3|case-|vib-ہے|tam-hE|chunkId-VGF|chunkType-head|stype-declarative|voicetype-active   0	root	_   _
    26  ۔	۔   punc    SYM	cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-BLK|chunkType-head|stype-|voicetype-	25  rsym    __

    irshad@python-hutrans$ cat tests/ssf-intra/hin-ssf.txt 
    <Sentence id='2'>
    1   यहाँ	PRP <fs af='यहाँ,pn,,,,o,0_से,' drel='nmod:दूरी' vpos='vib_2' name='यहाँ' chunkId='NP' chunkType='head:NP' posn='10'>
    2   से	PSP <fs af='से,psp,,,,,,' drel='lwg__psp:यहाँ' name='से' chunkType='child:NP' posn='20'>
    3   5	QC  <fs af='5,num,any,any,,any,,' drel='nmod__adj:किमी' name='5' chunkType='child:NP2' posn='30'>
    4   किमी	NN  <fs af='किमी,n,m,sg,3,d,0,0' drel='nmod__adj:दूरी' name='किमी' chunkType='child:NP2' posn='40'>
    5   दूरी	NN  <fs af='दूरी,n,f,sg,3,o,0_पर,0' drel='jjmod:स्थित' vpos='vib_vib_4' name='दूरी' chunkId='NP2' chunkType='head:NP2' posn='50'>
    6   पर	PSP <fs af='पर,psp,,,,,,' drel='lwg__psp:दूरी' name='पर' chunkType='child:NP2' posn='60'>
    7   स्थित	JJ  <fs af='स्थित,adj,any,any,,d,,' drel='nmod:ताल' name='स्थित' chunkId='JJP' chunkType='head:JJP' posn='70'>
    8   वासुकि	NNPC	<fs af='वासुकि,n,m,sg,3,d,0,0' drel='pof__cn:ताल' name='वासुकि' chunkType='child:NP3' posn='80'>
    9   ताल	NNP <fs af='ताल,n,m,sg,3,d,0,0' drel='k1:है' name='ताल' chunkId='NP3' chunkType='head:NP3' posn='90'>
    10  अपने	PRP <fs af='अपना,pn,m,any,any,o,0,0' drel='r6:जल' name='अपने' chunkId='NP4' chunkType='head:NP4' posn='100'>
    11  पारदर्शी   JJ	<fs af='पारदर्शी,adj,any,any,,o,,' drel='nmod__adj:जल' name='पारदर्शी' chunkType='child:NP5' posn='110'>
    12  जल	NN  <fs af='जल,n,m,sg,3,o,0,0' drel='ccof:और' name='जल' chunkId='NP5' chunkType='head:NP5' posn='120'>
    13  और	CC  <fs af='और,avy,,,,,,' drel='rt:है' name='और' chunkId='CCP' chunkType='head:CCP' posn='130'>
    14  उसमें	PRP <fs af='वह,pn,any,sg,3,o,में,meM' drel='k7:उतराते' name='उसमें' chunkId='NP6' chunkType='head:NP6' posn='140'>
    15  डूबते	VMC <fs af='डूब,v,m,pl,any,,ता,wA' drel='pof__cv:उतराते' name='डूबते' chunkType='child:VGNF' posn='150'>
    16  -	SYM <fs af='-,punc,,,,,,' drel='rsym:उतराते' name='-' chunkType='child:VGNF' posn='160'>
    17  उतराते    VM	<fs af='उतरा,v,m,pl,any,,ता,wA' drel='nmod__k1inv:हिमखंडों' name='उतराते' chunkId='VGNF' chunkType='head:VGNF' posn='170'>
    18  हिमखंडों    NN	<fs af='हिमखंड,n,m,pl,3,o,0_का,0' drel='r6:दृश्यों' vpos='vib_2' name='हिमखंडों' chunkId='NP7' chunkType='head:NP7' posn='180'>
    19  के	PSP <fs af='का,psp,m,pl,,o,,' drel='lwg__psp:हिमखंडों' name='के' chunkType='child:NP7' posn='190'>
    20  अद्भुत    JJ	<fs af='अद्भुत,adj,any,any,,o,,' drel='nmod__adj:दृश्यों' name='अद्भुत' chunkType='child:NP8' posn='200'>
    21  दृश्यों	NN  <fs af='दृश्य,n,m,pl,3,o,0_के_लिए,0' drel='ccof:और' vpos='vib_3_4' name='दृश्यों' chunkId='NP8' chunkType='head:NP8' posn='210'>
    22  के	PSP <fs af='के,psp,,,,,,' drel='lwg__psp:दृश्यों' name='के2' chunkType='child:NP8' posn='220'>
    23  लिए	PSP <fs af='लिए,psp,,,,,,' drel='lwg__psp:दृश्यों' name='लिए' chunkType='child:NP8' posn='230'>
    24  विख्यात    JJ	<fs af='विख्यात,adj,any,any,,,,' drel='k1s:है' name='विख्यात' chunkId='JJP2' chunkType='head:JJP2' posn='240'>
    25  है	VM  <fs af='है,v,any,sg,3,,है,hE' name='है' chunkId='VGF' chunkType='head:VGF' stype='declarative' voicetype='active' posn='250'>
    26  ।	SYM <fs af='।,punc,,,,,,' drel='rsym:है' name='।' chunkId='BLK' chunkType='head:BLK' posn='260'>
    </Sentence>

    irshad@python-hutrans$ hutrans < tests/ssf-intra/hin-ssf.txt --f ssf --t intra 
    <Sentence id='2'>
    1   یہاں    PRP	<fs af='یہاں,pn,,,,o,0_سے,' drel='nmod:دوری' vpos='vib_2' name='یہاں' chunkId='NP' chunkType='head:NP' posn='10'>
    2   سے	PSP <fs af='سے,psp,,,,,,' drel='lwg__psp:یہاں' name='سے' chunkType='child:NP' posn='20'>
    3   5	QC  <fs af='5,num,any,any,,any,,' drel='nmod__adj:کمی' name='5' chunkType='child:NP2' posn='30'>
    4   کمی	NN  <fs af='کمی,n,m,sg,3,d,0,0' drel='nmod__adj:دوری' name='کمی' chunkType='child:NP2' posn='40'>
    5   دوری    NN	<fs af='دوری,n,f,sg,3,o,0_پر,0' drel='jjmod:ستھت' vpos='vib_vib_4' name='دوری' chunkId='NP2' chunkType='head:NP2' posn='50'>
    6   پر	PSP <fs af='پر,psp,,,,,,' drel='lwg__psp:دوری' name='پر' chunkType='child:NP2' posn='60'>
    7   ستھت    JJ	<fs af='ستھت,adj,any,any,,d,,' drel='nmod:تال' name='ستھت' chunkId='JJP' chunkType='head:JJP' posn='70'>
    8   واسکی   NNPC    <fs af='واسکی,n,m,sg,3,d,0,0' drel='pof__cn:تال' name='واسکی' chunkType='child:NP3' posn='80'>
    9   تال	NNP <fs af='تال,n,m,sg,3,d,0,0' drel='k1:ہے' name='تال' chunkId='NP3' chunkType='head:NP3' posn='90'>
    10  اپنے    PRP	<fs af='اپنا,pn,m,any,any,o,0,0' drel='r6:جل' name='اپنے' chunkId='NP4' chunkType='head:NP4' posn='100'>
    11  پاردرشی JJ	<fs af='پاردرشی,adj,any,any,,o,,' drel='nmod__adj:جل' name='پاردرشی' chunkType='child:NP5' posn='110'>
    12  جل	NN  <fs af='جل,n,m,sg,3,o,0,0' drel='ccof:اور' name='جل' chunkId='NP5' chunkType='head:NP5' posn='120'>
    13  اور	CC  <fs af='اور,avy,,,,,,' drel='rt:ہے' name='اور' chunkId='CCP' chunkType='head:CCP' posn='130'>
    14  اسمیں   PRP	<fs af='وہ,pn,any,sg,3,o,میں,meM' drel='k7:اتراتے' name='اسمیں' chunkId='NP6' chunkType='head:NP6' posn='140'>
    15  ڈوبتے   VMC	<fs af='ڈوب,v,m,pl,any,,تا,wA' drel='pof__cv:اتراتے' name='ڈوبتے' chunkType='child:VGNF' posn='150'>
    16  −	SYM <fs af='−,punc,,,,,,' drel='rsym:اتراتے' name='−' chunkType='child:VGNF' posn='160'>
    17  اتراتے  VM	<fs af='اترا,v,m,pl,any,,تا,wA' drel='nmod__k1inv:ہمکھنڈوں' name='اتراتے' chunkId='VGNF' chunkType='head:VGNF' posn='170'>
    18  ہمکھنڈوں	NN  <fs af='ہمکھنڈ,n,m,pl,3,o,0_کا,0' drel='r6:درشیوں' vpos='vib_2' name='ہمکھنڈوں' chunkId='NP7' chunkType='head:NP7' posn='180'>
    19  کے	PSP <fs af='کا,psp,m,pl,,o,,' drel='lwg__psp:ہمکھنڈوں' name='کے' chunkType='child:NP7' posn='190'>
    20  ادبھت   JJ	<fs af='ادبھت,adj,any,any,,o,,' drel='nmod__adj:درشیوں' name='ادبھت' chunkType='child:NP8' posn='200'>
    21  درشیوں  NN	<fs af='درشیہ,n,m,pl,3,o,0_کے_لئے,0' drel='ccof:اور' vpos='vib_3_4' name='درشیوں' chunkId='NP8' chunkType='head:NP8' posn='210'>
    22  کے	PSP <fs af='کے,psp,,,,,,' drel='lwg__psp:درشیوں' name='کے2' chunkType='child:NP8' posn='220'>
    23  لئے	PSP <fs af='لئے,psp,,,,,,' drel='lwg__psp:درشیوں' name='لئے' chunkType='child:NP8' posn='230'>
    24  وکھیات  JJ	<fs af='وکھیات,adj,any,any,,,,' drel='k1s:ہے' name='وکھیات' chunkId='JJP2' chunkType='head:JJP2' posn='240'>
    25  ہے	VM  <fs af='ہے,v,any,sg,3,,ہے,hE' name='ہے' chunkId='VGF' chunkType='head:VGF' stype='declarative' voicetype='active' posn='250'>
    26  ۔	SYM <fs af='۔,punc,,,,,,' drel='rsym:ہے' name='۔' chunkId='BLK' chunkType='head:BLK' posn='260'>
    </Sentence>
    
    irshad@python-hutrans$ cat tests/ssf-inter/hin-inter.txt 
    <Sentence id='1'>
    1   ((	NP  <fs name='NP' drel='k1:VGF'>
    1.1 बलवीर    NNP	<fs af='बलवीर,n,m,sg,3,d,0,0' name='बलवीर' posn='10'>
    1.2 काका	NN  <fs af='काका,n,m,sg,3,d,0,0' name='काका' posn='20'>
        ))
    2   ((	NP  <fs name='NP2' drel='nmod__emph:NP'>
    2.1 खुद	PRP <fs af='खुद,pn,,,,,,' name='खुद' posn='30'>
    2.2 तो	RP  <fs af='तो,avy,,,,,,' name='तो' posn='40'>
        ))
    3   ((	JJP <fs name='JJP' drel='k1s:VGF'>
    3.1 अल्पशिक्षित JJ	<fs af='अल्पशिक्षित,adj,any,any,,,,' name='अल्पशिक्षित' posn='50'>
        ))
    4   ((	VGF <fs drel='ccof:CCP' name='VGF' stype='declarative' voicetype='active''>
    4.1 थे	VM  <fs af='था,v,m,sg,3h,,था,WA' name='थे' posn='60'>
        ))
    5   ((	CCP <fs name='CCP' drel='ccof:CCP3'>
    5.1 पर	CC  <fs af='पर,avy,,,,,,' name='पर' posn='70'>
        ))
    6   ((	NP  <fs name='NP3' drel='r6:NP4'>
    6.1 पढ़ाई	NN  <fs af='पढाई,n,f,sg,3,o,0,0' name='पढ़ाई' posn='80'>
    6.2 के	PSP <fs af='का,psp,m,sg,,o,,' name='के' posn='90'>
        ))
    7   ((	NP  <fs name='NP4' drel='k2:VGF2'>
    7.1 महत्व    NN	<fs af='महत्व,n,m,sg,3,o,0,0' name='महत्व' posn='100'>
    7.2 को	PSP <fs af='को,psp,,,,,,' name='को' posn='110'>
        ))
    8   ((	JJP <fs name='JJP2' drel='ccof:CCP2'>
    8.1 अधिक	QF  <fs af='अधिक,avy,,,,,,' name='अधिक' posn='120'>
        ))
    9   ((	CCP <fs name='CCP2' drel='nmod:NP5'>
    9.1 और	CC  <fs af='और,avy,,,,,,' name='और' posn='130'>
        ))
    10  ((	JJP <fs name='JJP3' drel='ccof:CCP2'>
    10.1	बहुत QF	<fs af='बहुत,avy,,,,,,' name='बहुत' posn='140'>
        ))
    11  ((	NP  <fs name='NP5' drel='adv:VGF2'>
    11.1	बारीकी NN	<fs af='बारीकी,n,f,sg,3,o,0,0' name='बारीकी' posn='150'>
    11.2	से   PSP	<fs af='से,psp,,,,,,' name='से' posn='160'>
        ))
    12  ((	VGF <fs drel='ccof:CCP' name='VGF2' stype='declarative' voicetype='active''>
    12.1	समझते	VM  <fs af='समझ,v,m,sg,3h,,ता,wA' name='समझते' posn='170'>
        ))
    13  ((	CCP <fs name='CCP3'>
    13.1	और  CC	<fs af='और,avy,,,,,,' name='और2' posn='180'>
        ))
    14  ((	NP  <fs name='NP6' drel='k4:VGF3'>
    14.1	दूसरों NN	<fs af='दूसरा,n,m,pl,3,o,0,0' name='दूसरों' posn='190'>
    14.2	को   PSP	<fs af='को,psp,,,,,,' name='को2' posn='200'>
    14.3	भी   RP	<fs af='भी,avy,,,,,,' name='भी' posn='210'>
        ))
    15  ((	VGF <fs drel='ccof:CCP3' name='VGF3' stype='declarative' voicetype='active''>
    15.1	समझाते	VM  <fs af='समझा,v,m,sg,3h,,ता,wA' name='समझाते' posn='220'>
    15.2	थे   VAUX    <fs af='था,v,m,sg,3h,,था,WA' name='थे2' posn='230'>
        ))
    16  ((	BLK <fs name='BLK' drel='rsym:CCP3'>
    16.1	।   SYM	<fs af='।,punc,,,,,,' name='।' posn='240'>
        ))
    </Sentence>
    irshad@python-hutrans$ hutrans < tests/ssf-inter/hin-inter.txt --f ssf --t inter
    <Sentence id='1'>
    1   ((	NP  <fs name='NP' drel='k1:VGF'>
    1.1 بلویر   NNP	<fs af='بلویر,n,m,sg,3,d,0,0' name='بلویر' posn='10'>
    1.2 کاکا    NN	<fs af='کاکا,n,m,sg,3,d,0,0' name='کاکا' posn='20'>
        ))	    
    2   ((	NP  <fs name='NP2' drel='nmod__emph:NP'>
    2.1 خود	PRP <fs af='خود,pn,,,,,,' name='خود' posn='30'>
    2.2 تو	RP  <fs af='تو,avy,,,,,,' name='تو' posn='40'>
        ))	    
    3   ((	JJP <fs name='JJP' drel='k1s:VGF'>
    3.1 الپشکشت JJ	<fs af='الپشکشت,adj,any,any,,,,' name='الپشکشت' posn='50'>
        ))	    
    4   ((	VGF <fs drel='ccof:CCP' name='VGF' stype='declarative' voicetype='active'>
    4.1 تھے	VM  <fs af='تھا,v,m,sg,3h,,تھا,WA' name='تھے' posn='60'>
        ))	    
    5   ((	CCP <fs name='CCP' drel='ccof:CCP3'>
    5.1 پر	CC  <fs af='پر,avy,,,,,,' name='پر' posn='70'>
        ))	    
    6   ((	NP  <fs name='NP3' drel='r6:NP4'>
    6.1 پڑھائی  NN	<fs af='پڈھائی,n,f,sg,3,o,0,0' name='پڑھائی' posn='80'>
    6.2 کے	PSP <fs af='کا,psp,m,sg,,o,,' name='کے' posn='90'>
        ))	    
    7   ((	NP  <fs name='NP4' drel='k2:VGF2'>
    7.1 مہتو    NN	<fs af='مہتو,n,m,sg,3,o,0,0' name='مہتو' posn='100'>
    7.2 کو	PSP <fs af='کو,psp,,,,,,' name='کو' posn='110'>
        ))	    
    8   ((	JJP <fs name='JJP2' drel='ccof:CCP2'>
    8.1 ادھک    QF	<fs af='ادھک,avy,,,,,,' name='ادھک' posn='120'>
        ))	    
    9   ((	CCP <fs name='CCP2' drel='nmod:NP5'>
    9.1 اور	CC  <fs af='اور,avy,,,,,,' name='اور' posn='130'>
        ))	    
    10  ((	JJP <fs name='JJP3' drel='ccof:CCP2'>
    10.1	بہت QF	<fs af='بہت,avy,,,,,,' name='بہت' posn='140'>
        ))	    
    11  ((	NP  <fs name='NP5' drel='adv:VGF2'>
    11.1	باریکی	NN  <fs af='باریکی,n,f,sg,3,o,0,0' name='باریکی' posn='150'>
    11.2	سے  PSP	<fs af='سے,psp,,,,,,' name='سے' posn='160'>
        ))	    
    12  ((	VGF <fs drel='ccof:CCP' name='VGF2' stype='declarative' voicetype='active'>
    12.1	سمجھتے	VM  <fs af='سمجھ,v,m,sg,3h,,تا,wA' name='سمجھتے' posn='170'>
        ))	    
    13  ((	CCP <fs name='CCP3'>
    13.1	اور CC	<fs af='اور,avy,,,,,,' name='اور2' posn='180'>
        ))	    
    14  ((	NP  <fs name='NP6' drel='k4:VGF3'>
    14.1	دوسروں	NN  <fs af='دوسرا,n,m,pl,3,o,0,0' name='دوسروں' posn='190'>
    14.2	کو  PSP	<fs af='کو,psp,,,,,,' name='کو2' posn='200'>
    14.3	بھی RP	<fs af='بھی,avy,,,,,,' name='بھی' posn='210'>
        ))	    
    15  ((	VGF <fs drel='ccof:CCP3' name='VGF3' stype='declarative' voicetype='active'>
    15.1	سمجھاتے	VM  <fs af='سمجھا,v,m,sg,3h,,تا,wA' name='سمجھاتے' posn='220'>
    15.2	تھے VAUX    <fs af='تھا,v,m,sg,3h,,تھا,WA' name='تھے2' posn='230'>
        ))	    
    16  ((	BLK <fs name='BLK' drel='rsym:CCP3'>
    16.1	۔   SYM	<fs af='۔,punc,,,,,,' name='۔' posn='240'>
        ))	    
    </Sentence>
    
    irshad@python-hutrans$ cat tests/tnt/hin-tnt.txt 
    यों   RB
    सिंगल JJ
    स्क्रीन	NNC
    थिएटर	NNP
    के   PSP
    दर्शकों	NN
    को   PSP
    अग्निपथ	NNP
    अधिक QF
    नहीं  NEG
    भा   VM
    सकी  VAUX
    ।   SYM
    irshad@python-hutrans$ hutrans < tests/tnt/hin-tnt.txt --f tnt
    یوں RB
    سنگل	JJ
    سکرین	NNC
    تھئیٹر	NNP
    کے  PSP
    درشکوں	NN
    کو  PSP
    اگنپتھ	NNP
    ادھک	QF
    نہیں	NEG
    بھا VM
    سکی VAUX
    ۔   SYM

2. **From Python**

2.1 **Text:**

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


2.2 **work with conll:**

.. code:: python

    >>> trn = transliterator(format_='conll') #source=hindi (default)
    >>>
    >>> conll = """1        यहाँ     यहाँ     pn      PRP     cat-pn|gen-|num-|pers-|case-o|vib-0_से|tam-|chunkId-NP|chunkType-head|stype-|voicetype-  5      nmod    _       _
    ... 2   से       से       psp     PSP     cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP|chunkType-child|stype-|voicetype-    1       lwg__psp       _       _
    ... 3   5       5       num     QC      cat-num|gen-any|num-any|pers-|case-any|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-  4       nmod__adj      _       _
    ... 4   किमी    किमी    n       NN      cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP2|chunkType-child|stype-|voicetype-      5       nmod__adj      _       _
    ... 5   दूरी     दूरी     n       NN      cat-n|gen-f|num-sg|pers-3|case-o|vib-0_पर|tam-0|chunkId-NP2|chunkType-head|stype-|voicetype-    7       jjmod  _       _
    ... 6   पर      पर      psp     PSP     cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-   5       lwg__psp       _       _
    ... 7   स्थित    स्थित    adj     JJ      cat-adj|gen-any|num-any|pers-|case-d|vib-|tam-|chunkId-JJP|chunkType-head|stype-|voicetype-     9       nmod   _       _
    ... 8   वासुकि   वासुकि   n       NNPC    cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-child|stype-|voicetype-      9       pof__cn        _       _
    ... 9   ताल     ताल     n       NNP     cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-head|stype-|voicetype-       25      k1     _       _
    ... 10  अपने     अपना    pn      PRP     cat-pn|gen-m|num-any|pers-any|case-o|vib-0|tam-0|chunkId-NP4|chunkType-head|stype-|voicetype-   12      r6     _       _
    ... 11  पारदर्शी पारदर्शी adj     JJ      cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP5|chunkType-child|stype-|voicetype-    12      nmod__adj      _       _
    ... 12  जल      जल      n       NN      cat-n|gen-m|num-sg|pers-3|case-o|vib-0|tam-0|chunkId-NP5|chunkType-head|stype-|voicetype-       13      ccof   _       _
    ... 13  और      और      avy     CC      cat-avy|gen-|num-|pers-|case-|vib-|tam-|chunkId-CCP|chunkType-head|stype-|voicetype-    25      rt      _      _
    ... 14  उसमें     वह      pn      PRP     cat-pn|gen-any|num-sg|pers-3|case-o|vib-में|tam-meM|chunkId-NP6|chunkType-head|stype-|voicetype-  17      k7     _       _
    ... 15  डूबते     डूब      v       VMC     cat-v|gen-m|num-pl|pers-any|case-|vib-ता|tam-wA|chunkId-VGNF|chunkType-child|stype-|voicetype-  17      pof__cv        _       _
    ... 16  -       -       punc    SYM     cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-VGNF|chunkType-child|stype-|voicetype- 17      rsym    _      _
    ... 17  उतराते   उतरा    v       VM      cat-v|gen-m|num-pl|pers-any|case-|vib-ता|tam-wA|chunkId-VGNF|chunkType-head|stype-|voicetype-   18      nmod__k1inv    _       _
    ... 18  हिमखंडों  हिमखंड   n       NN      cat-n|gen-m|num-pl|pers-3|case-o|vib-0_का|tam-0|chunkId-NP7|chunkType-head|stype-|voicetype-    21      r6     _       _
    ... 19  के       का      psp     PSP     cat-psp|gen-m|num-pl|pers-|case-o|vib-|tam-|chunkId-NP7|chunkType-child|stype-|voicetype-       18      lwg__psp       _       _
    ... 20  अद्भुत    अद्भुत    adj     JJ      cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-    21      nmod__adj      _       _
    ... 21  दृश्यों    दृश्य     n       NN      cat-n|gen-m|num-pl|pers-3|case-o|vib-0_के_लिए|tam-0|chunkId-NP8|chunkType-head|stype-|voicetype- 13      ccof   _       _
    ... 22  के       के       psp     PSP     cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21      lwg__psp       _       _
    ... 23  लिए     लिए     psp     PSP     cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21      lwg__psp       _       _
    ... 24  विख्यात  विख्यात  adj     JJ      cat-adj|gen-any|num-any|pers-|case-|vib-|tam-|chunkId-JJP2|chunkType-head|stype-|voicetype-     25      k1s    _       _
    ... 25  है       है       v       VM      cat-v|gen-any|num-sg|pers-3|case-|vib-है|tam-hE|chunkId-VGF|chunkType-head|stype-declarative|voicetype-active   0       root    _       _
    ... 26  ।       ।       punc    SYM     cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-BLK|chunkType-head|stype-|voicetype-   25      rsym    _      _"""
    >>> 
    >>> print trn.convert(conll)
    1   یہاں    یہاں    pn	PRP cat-pn|gen-|num-|pers-|case-o|vib-0_سے|tam-|chunkId-NP|chunkType-head|stype-|voicetype- 5	nmod	__
    2   سے	سے  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP|chunkType-child|stype-|voicetype-    1	lwg__psp    _	_
    3   5	5   num	QC  cat-num|gen-any|num-any|pers-|case-any|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-  4	nmod__adj   _	_
    4   کمی	کمی n	NN  cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP2|chunkType-child|stype-|voicetype-	5   nmod__adj	_   _
    5   دوری    دوری    n	NN  cat-n|gen-f|num-sg|pers-3|case-o|vib-0_پر|tam-0|chunkId-NP2|chunkType-head|stype-|voicetype-    7	jjmod	_   _
    6   پر	پر  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP2|chunkType-child|stype-|voicetype-   5	lwg__psp    _	_
    7   ستھت    ستھت    adj	JJ  cat-adj|gen-any|num-any|pers-|case-d|vib-|tam-|chunkId-JJP|chunkType-head|stype-|voicetype-	9   nmod    _	_
    8   واسکی   واسکی   n	NNPC	cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-child|stype-|voicetype-  9	pof__cn	_   _
    9   تال	تال n	NNP cat-n|gen-m|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP3|chunkType-head|stype-|voicetype-	25  k1	_   _
    10  اپنے    اپنا    pn	PRP cat-pn|gen-m|num-any|pers-any|case-o|vib-0|tam-0|chunkId-NP4|chunkType-head|stype-|voicetype-   12	r6  _	_
    11  پاردرشی پاردرشی adj	JJ  cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP5|chunkType-child|stype-|voicetype-    12	nmod__adj   _	_
    12  جل	جل  n	NN  cat-n|gen-m|num-sg|pers-3|case-o|vib-0|tam-0|chunkId-NP5|chunkType-head|stype-|voicetype-	13  ccof    _	_
    13  اور	اور avy	CC  cat-avy|gen-|num-|pers-|case-|vib-|tam-|chunkId-CCP|chunkType-head|stype-|voicetype-    25	rt  __
    14  اسمیں   وہ	pn  PRP	cat-pn|gen-any|num-sg|pers-3|case-o|vib-میں|tam-meM|chunkId-NP6|chunkType-head|stype-|voicetype-    17	k7  _	_
    15  ڈوبتے   ڈوب	v   VMC	cat-v|gen-m|num-pl|pers-any|case-|vib-تا|tam-wA|chunkId-VGNF|chunkType-child|stype-|voicetype-	17  pof__cv _	_
    16  −	−   punc    SYM	cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-VGNF|chunkType-child|stype-|voicetype-	17  rsym    __
    17  اتراتے  اترا    v	VM  cat-v|gen-m|num-pl|pers-any|case-|vib-تا|tam-wA|chunkId-VGNF|chunkType-head|stype-|voicetype-   18	nmod__k1inv _	_
    18  ہمکھنڈوں	ہمکھنڈ	n   NN	cat-n|gen-m|num-pl|pers-3|case-o|vib-0_کا|tam-0|chunkId-NP7|chunkType-head|stype-|voicetype-	21  r6	_   _
    19  کے	کا  psp	PSP cat-psp|gen-m|num-pl|pers-|case-o|vib-|tam-|chunkId-NP7|chunkType-child|stype-|voicetype-	18  lwg__psp	_   _
    20  ادبھت   ادبھت   adj	JJ  cat-adj|gen-any|num-any|pers-|case-o|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-    21	nmod__adj   _	_
    21  درشیوں  درشیہ   n	NN  cat-n|gen-m|num-pl|pers-3|case-o|vib-0_کے_لئے|tam-0|chunkId-NP8|chunkType-head|stype-|voicetype-	13  ccof    _	_
    22  کے	کے  psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21	lwg__psp    _	_
    23  لئے	لئے psp	PSP cat-psp|gen-|num-|pers-|case-|vib-|tam-|chunkId-NP8|chunkType-child|stype-|voicetype-   21	lwg__psp    _	_
    24  وکھیات  وکھیات  adj	JJ  cat-adj|gen-any|num-any|pers-|case-|vib-|tam-|chunkId-JJP2|chunkType-head|stype-|voicetype-	25  k1s	_   _
    25  ہے	ہے  v	VM  cat-v|gen-any|num-sg|pers-3|case-|vib-ہے|tam-hE|chunkId-VGF|chunkType-head|stype-declarative|voicetype-active   0	root	_   _
    26  ۔	۔   punc    SYM	cat-punc|gen-|num-|pers-|case-|vib-|tam-|chunkId-BLK|chunkType-head|stype-|voicetype-	25  rsym    __

2.3 **work with bio or tnt:**

::

    same as conll or text

2.4 **work with ssf:**

::
    
    implemented for ssf files only

