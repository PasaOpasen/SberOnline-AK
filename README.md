- [Экспертная система для нечёткой классификации отзывов к приложению Сбербанк-Онлайн](#----------------------------------------------------------------------------------)
  * [Идея алгоритма](#идея-алгоритма)
  * [Как формируется граф понятий](#как-формируется-граф-понятий)
  * [Преимущество алгоритма](#преимущества-алгоритма)
- [История о том, как сильно поднастрал мне этот хакатон](#история-о-том-как-сильно-поднасрал-мне-этот-хакатон)

# Экспертная система для нечёткой классификации отзывов к приложению Сбербанк-Онлайн

[Ссылка на изначальный репозиторий](https://github.com/PasaOpasen/SberCode_online_AK_Team)

![1](https://github.com/PasaOpasen/SberOnline-AK/blob/master/16.png)

## Идея алгоритма

Алгоритм использует поиск ключевых фраз по ориентированному ациклическому графу понятий. Мы исходим из предположения, что разнообразие ошибок для каждой команды разработчиков укладывается в 5-10 ключевых фраз, если использовать стемминг. И поэтому намного проще написать эти фразы (и так известные разработчикам), чем помечать огромные объёмы данных и скармливать их классическим моделям машинного обучения, чтобы те сами определили, какие фразы к каким командам относятся.

Задача выполняется в три этапа:

1. Проводится очистка текста отзыва: удаляются лишние символы, стоп-слова, ссылки и т. д. Таким образом, текст сводится к набору фраз.

1. Из этого набора фраз извлекаются униграммы и биграммы (не перекрывающие сепараторы), производится их стемминг. Результаты объединяются в облако понятий, откуда извлекаются понятия, представляющие интерес.

1. Для каждого понятия, представляющего интерес, происходит его поиск в графе понятий. В случае успеха от найденного понятия происходит движение по графу к его родителям и дальше, пока есть родители. В конечном итоге любое понятие из графа приводит как минимум к одной команде, которой следует обратить внимание на отзыв.

## Как формируется граф понятий

При добавлении новой группы разработчиков, в [этот текстовый файл](https://github.com/PasaOpasen/SberOnline-AK/blob/master/Code/Models_modules/graph_module/content_detector/graph_skills.txt) требуется добавить псевдоним для этой группы и после этого список ключевых фраз для этой группы (фразы, которые обычно используют пользователи при жалобах на ошибки, предназначенные этой группе). Затем [скрипт](https://github.com/PasaOpasen/SberOnline-AK/blob/master/Code/Models_modules/graph_module/content_detector/create_graph_dictionary.py) конвертирует этот файлы в обычный [словарь json](https://github.com/PasaOpasen/SberOnline-AK/blob/master/Code/Models_modules/graph_module/content_detector/graph_skills.json) с сохранением всевозможных результатов поиска (то есть реальный поиск на графе происходит только во время его построения, дальше работа идёт с кешированными данными). Таким образом, для упрощения поддержки графа используется псевдоязык программирования.

В целом, понятия устанавливаются человеком, но человек может обращаться к языковой модели **word2vec** для определения близких по смыслу слов (и наиболее распространённых биграмм и триграмм). Например, на слово *виснет* эта модель выдаст очень близкие по смыслу фразы (ключи) *глючит*, *зависает*, *тормозит*, *долго думает*, *постоянно зависает*, *очень долго грузит*; человек должен определить, какие из них действительно имеют значение и должны быть добавлены в граф.

## Преимущество алгоритма

1. **Предельная прозрачность**. Очень легко определить, какие именно фразы обуславливают конкретный результат классификации. 

1. **Гибкость**. Модель легко изменять, и каждое изменение почти наверняка будет улучшать её качество. Также ничего не стоит "дообучить" модель при появлении новых команд и новых тенденций: это займёт 10 строк кода и 15 минут работы одного человека.

1. **Скорость**. Для каждого отзыва модель лишь удаляет некоторые слова, проводит стемминг и делает поиск по небольшому словарю. Этот процесс происходит очень быстро.

1. **Легковесность**. Все нужные данные и скрипты для реальной эксплуатации весят меньше одного мегабайта. Мы не используем никаких крупных пакетов тяжелее стандартного NumPy.

1. **Качество**. По качеству эта модель способна составить конкуренцию многим реккурентным нейросетям, обученным на больших объёмах размеченных данных.


# История о том, как сильно поднастрал мне этот хакатон

**1-е января 2021-го**. Сегодня решил высказать некоторые мысли, к которым пришёл. В конце августа мы участвовали в хакатоне от Сбербанка. Пошли на него, потому что хотели развиваться в этом плане, может даже получить работу в будущем и т. п. Я сразу подумал, что Сбербанк – это очень серьёзная организация, у них не должно быть всё через жопу, как на нашем прошлом хакатоне. Как оказалось, я фатально ошибся…

По небольшому описанию задачи, к которому мы имели доступ до начала соревнований, я сделал вывод, что это будет классификация маленьких текстов на примерно 4 класса, очень даже нормальный расклад. Ага, только после открытия нас ожидал шок. Нам скинули несколько очень грязных файлов с отзывами на приложение «Сбербанк Онлайн» из AppStore, Google Play и может ещё откуда-то; файлы были ровно такие, какими их сохраняют указанные сервисы, то есть с датами, именами пользователей, почтами и кучей другой мусорной информации; где-то посреди этого всего были текстовые отзывы людей. И задачу нам поставили так: есть несколько десятков команд, отвечающих за разные направления (платежи, переводы, кредиты, про остальные мы вообще не шарили, мы не экономисты и не сотрудники Сбера), и нужно написать систему, которая будет каждый отзыв как-нибудь сбрасывать нужной команде или командам (то есть нечеткая классификация). Вроде бы, задача ясна, только вот она нерешаемая, потому что:
* Команд (целевых классов) были реально очень много, где-то 30, и почти про все из них мы совершенно не имели представления, чем же конкретным они занимаются. Переводы – это я примерно понимаю, но про основную часть команд были известны только названия (обычно, аббревиатуры латиницей), то есть чем одна отличается от другой – вообще не ясно.
* На самом деле это не должно приводить к крупным проблемам, потому что в первую очередь модели обучаются по меткам классов, только вот У НАС ЭТИХ МЕТОК НЕ БЫЛО ВООБЩЕ, никаких даже намеков о том, что вот этот отзыв должен прийти вот этой команде, нет, был только большой набор сырых текстов, которые мы хер знает почему должны сбрасывать каким-то командам из кучи команд, о которых ничего неизвестно.
* Чуть позже, хоть этого не было в постановки задачи, нам непрозрачно намекнули, что обязательно нужно сделать анализ тональностей этих отзывов. На что я спросил, какой в этом смысл, если при отправке отзыва человек ещё и оценивает приложение с помощью звёздочек, которые и являются показателем тональности. Мне сказали, что часто людям это делать лень и они оправляют рандомные звезды и т. п. Это правда, но ахуенно не это, а то, что я должен провести анализ тональности, опираясь на эти, в основном рандомные, говнозвездочки (ведь другой разметки не предоставлено)! В итоге в процессе построения модели (а всё получилось очень даже неплохого качества) мы не раз сталкивались с тем, что вполне неплохой отзыв идёт в паре с 2 звёздами (а не 4-5), а плохой отзыв имеет 5 звезд, либо абсолютно один и тот же текст («всё норм») может иметь 3, 4 или 5 звёзд! И вот по таким данным надо обучаться! Как они сами рассчитывают использовать у себя модель, обученную на таком говне?
* Но самым ахуительным моментом стало то, что чуваки из Сбера так и не определись, что именно им нужно – модель (машинного обучения) или сервис. Если и то и другое, то они реально ахуели: невозможно сделать и хорошую модель и хороший сервис за двое суток в команде из 3 человек! Тем более это две сложные и абсолютно не связанные задачи, то есть каждой должен заниматься свой человек, либо терминатор, который шарит в обеих областях и не нуждается во сне. Весь прикол в том, что и на первом митапе и на втором нам говорили: «конкретно эта задача – это машинное обучение, нам нужна модель», – а уже под конец второй половины хакатона начали гнать, что «нам нужен сервис, желательно мобильное приложение».

В общем, мы пахали как черти, сделали, вероятно, наилучшие возможные модели (с учётом всратости данных) как по тональности, так и по классификации, даже сделали маленький сайт для тестирования всего онлайн, только вот победители состояли из чуваков, которые либо просто использовали нейросети (это ж круто, современно, все дела) с очень сомнительной эффективностью (оглашали точность тональности 97% при том, что положительных отзывов самих по себе уже 95%), либо сделали какое-то многофункциональное мобильное приложение вообще без алгоритма (и при том, что почти весь хакатон нам говорили, что нужна модель, а не сервис).

Сейчас я понимаю, что именно с этого хакатона у меня начались большие проблемы. Осознание того, что мир настолько тупой, иррациональный, неоптимизированный, что кучу денег платят пацанам чисто за нейросети (и похуй, как это будет работать на продакшене, если вообще туда доберется), что к этому событию долго готовятся, а в итоге так и не решено, нужна им модель или сервис, что данные абсолютно сырые (хотя вам же будет лучше, если данные будут чистые, тогда и модели будут годные), что судьи не особо компетентные – всё это очень нехорошо на мне отразилось. И те 2000 в виде купонов для доставки еды совсем не стоили того, что несколько недель у меня была тяжелая депрессия, что с тех пор я очень плохо сплю, что месяц была диарея, потом – коронавирус, параллельно – проблемы со щитовидной железой и сердцем (пока считаем, что одно спровоцировало другое), ну и, конечно, обострение синусита, увеличение лимфоузлов, преследующие меня с середины сентября и по сей день. На одних врачей и анализы я уже потратил около 15к, еще больше 5к на лекарства, вдобавок последние 4 месяца (!) жизни (может быть, исключая 10 отдельных дней) вообще сомнительно считать за жизнь. И я очень надеюсь, что какое-то глубокое осознание описанных событий поможет мне вылечить мои болезни, если, конечно, я всё правильно понимаю.

