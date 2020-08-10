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
