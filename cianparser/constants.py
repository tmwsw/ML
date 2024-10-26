DEAL_TYPES = {"rent_long", "sale"}
OBJECT_SUBURBAN_TYPES = {
    "house": "1",
    "house-part": "2",
    "land-plot": "3",
    "townhouse": "4",
}
OBJECT_TYPES = {"secondary": "1", "new": "2"}

# DEAL_TYPES_NOT_IMPLEMENTED_YET = {"rent_short"}

# ACCOMMODATION_TYPES_NOT_IMPLEMENTED_YET = {"room", "house", "house-part", "townhouse"}

FLOATS_NUMBERS_REG_EXPRESSION = r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"

FILE_NAME_FLAT_FORMAT = "cian_{}_{}_{}_{}_{}_{}.csv"
FILE_NAME_SUBURBAN_FORMAT = "cian_{}_{}_{}_{}_{}_{}_{}.csv"
FILE_NAME_NEWOBJECT_FORMAT = "cian_{}_{}_{}.csv"

BASE_URL = "https://cian.ru"
DEFAULT_POSTFIX_PATH = "/cat.php?"
NEWOBJECT_POSTFIX_PATH = "/newobjects/list/?"
DEFAULT_PATH = "engine_version=2&p={}&with_neighbors=0"
REGION_PATH = "&region={}"
OFFER_TYPE_PATH = "&offer_type={}"
RENT_PERIOD_TYPE_PATH = "&type={}"
DEAL_TYPE_PATH = "&deal_type={}"
OBJECT_TYPE_PATH = "&object_type%5B0%5D={}"

ROOM_PATH = "&room{}=1"
STUDIO_PATH = "&room9=1"
IS_ONLY_HOMEOWNER_PATH = "&is_by_homeowner=1"
MIN_BALCONIES_PATH = "&min_balconies={}"
HAVE_LOGGIA_PATH = "&loggia=1"
MIN_HOUSE_YEAR_PATH = "&min_house_year={}"
MAX_HOUSE_YEAR_PATH = "&max_house_year={}"
MIN_PRICE_PATH = "&minprice={}"
MAX_PRICE_PATH = "&maxprice={}"
MIN_FLOOR_PATH = "&minfloor={}"
MAX_FLOOR_PATH = "&maxfloor={}"
MIN_TOTAL_FLOOR_PATH = "&minfloorn={}"
MAX_TOTAL_FLOOR_PATH = "&maxfloorn={}"

HOUSE_MATERIAL_TYPE_PATH = "&house_material%5B0%5D={}"

METRO_FOOT_MINUTE_PATH = "&only_foot=2&foot_min={}"
METRO_ID_PATH = "&metro%5B0%5D={}"

FLAT_SHARE_PATH = "&flat_share={}"
ONLY_FLAT_PATH = "&only_flat={}"
APARTMENT_PATH = "&apartment={}"

SORT_BY_PRICE_FROM_MIN_TO_MAX_PATH = "&sort=price_object_order"
SORT_BY_PRICE_FROM_MAX_TO_MIN_PATH = "&sort=total_price_desc"
SORT_BY_TOTAL_METERS_FROM_MAX_TO_MIN_PATH = "&sort=area_order"
SORT_BY_CREATION_DATA_FROM_NEWER_TO_OLDER_PATH = "&sort=creation_date_desc"
SORT_BY_CREATION_DATA_FROM_OLDER_TO_NEWER_PATH = "&sort=creation_date_asc"

IS_SORT_BY_PRICE_FROM_MIN_TO_MAX_PATH = "price_from_min_to_max"
IS_SORT_BY_PRICE_FROM_MAX_TO_MIN_PATH = "price_from_max_to_min"
IS_SORT_BY_TOTAL_METERS_FROM_MAX_TO_MIN_PATH = "total_meters_from_max_to_min"
IS_SORT_BY_CREATION_DATA_FROM_NEWER_TO_OLDER_PATH = "creation_data_from_newer_to_older"
IS_SORT_BY_CREATION_DATA_FROM_OLDER_TO_NEWER_PATH = "creation_data_from_older_to_newer"

NOT_STREET_ADDRESS_ELEMENTS = {"ЖК", "м.", "мкр.", "Жилой комплекс", "Жилой Комплекс"}

STREET_TYPES = {
    "ул.",
    "улица",
    "аллея",
    "бульвар",
    "линия",
    "набережная",
    "тракт",
    "тупик",
    "шоссе",
    "переулок",
    "проспект",
    "проезд",
    "раздъезд",
    "мост",
    "авеню",
}

SPECIFIC_FIELDS_FOR_RENT_LONG = {"price_per_month", "commissions"}
SPECIFIC_FIELDS_FOR_RENT_SHORT = {"price_per_day"}
SPECIFIC_FIELDS_FOR_SALE = {
    "price",
    "residential_complex",
    "object_type",
    "finish_type",
}

CITIES = [
    ["Москва", "1"],
    ["Санкт-Петербург", "2"],
    ["Московская область", "4593"],
    ["Абакан", "4638"],
    ["Анадырь", "4648"],
    ["Архангельск", "4658"],
    ["Астрахань", "4660"],
    ["Барнаул", "4668"],
    ["Белгород", "4671"],
    ["Биробиджан", "4682"],
    ["Благовещенск", "4683"],
    ["Бронницы", "4690"],
    ["Брянск", "4691"],
    ["Великий Новгород", "4694"],
    ["Владивосток", "4701"],
    ["Владикавказ", "4702"],
    ["Владимир", "4703"],
    ["Волгоград", "4704"],
    ["Вологда", "4708"],
    ["Воронеж", "4713"],
    ["Геленджик", "4717"],
    ["Горно-Алтайск", "4719"],
    ["Грозный", "4723"],
    ["Дзержинский", "4734"],
    ["Долгопрудный", "4738"],
    ["Дубна", "4741"],
    ["Екатеринбург", "4743"],
    ["Жуковский", "4750"],
    ["Звенигород", "4756"],
    ["Иванов", "4767"],
    ["Ижевск", "4770"],
    ["Иркутск", "4774"],
    ["Йошкар-Ола", "4776"],
    ["Казань", "4777"],
    ["Калининград", "4778"],
    ["Калуга", "4780"],
    ["Кемерово", "4795"],
    ["Киров", "4800"],
    ["Коломна", "4809"],
    ["Королёв", "4813"],
    ["Красноармейск", "4817"],
    ["Краснодар", "4820"],
    ["Краснознаменск", "4822"],
    ["Красноярск", "4827"],
    ["Курган", "4834"],
    ["Курск", "4835"],
    ["Кызыл", "4837"],
    ["Липецк", "4847"],
    ["Лобня", "4848"],
    ["Лыткарино", "4851"],
    ["Магадан", "4852"],
    ["Майкоп", "4855"],
    ["Махачкала", "4857"],
    ["Мурманск", "4871"],
    ["Нальчик", "4875"],
    ["Нарьян-Мар", "4876"],
    ["Нижний Новгород", "4885"],
    ["Новороссийск", "4896"],
    ["Новокузнецк", "4894"],
    ["Новосибирск", "4897"],
    ["Омск", "4914"],
    ["Оренбург", "4915"],
    ["Орехово-Зуево", "4916"],
    ["Пенза", "4923"],
    ["Пермь", "4927"],
    ["Петрозаводск", "4930"],
    ["Петропавловск-Камчатский", "4931"],
    ["Подольск", "4935"],
    ["Протвино", "4945"],
    ["Псков", "4946"],
    ["Пущино", "4949"],
    ["Реутов", "4958"],
    ["Ростов-на-Дону", "4959"],
    ["Рошаль", "4960"],
    ["Рязань", "4963"],
    ["Салехард", "4965"],
    ["Самара", "4966"],
    ["Саранск", "4967"],
    ["Саратов", "4969"],
    ["Серпухов", "4983"],
    ["Смоленск", "4987"],
    ["Сочи", "4998"],
    ["Ставрополь", "5001"],
    ["Сургут", "5003"],
    ["Сыктывкар", "5006"],
    ["Тамбов", "5011"],
    ["Тольятти", "5015"],
    ["Томск", "5016"],
    ["Тула", "5020"],
    ["Тюмень", "5024"],
    ["Улан-Удэ", "5026"],
    ["Ульяновск", "5027"],
    ["Фрязино", "5038"],
    ["Хабаровск", "5039"],
    ["Ханты-Мансийск", "5041"],
    ["Химки", "5044"],
    ["Чебоксары", "5047"],
    ["Челябинск", "5048"],
    ["Череповец", "5050"],
    ["Черкесск", "5051"],
    ["Чита", "5053"],
    ["Электросталь", "5064"],
    ["Элиста", "5065"],
    ["Южно-Сахалинск", "5069"],
    ["Якутск", "5073"],
    ["Ярославль", "5075"],
]

OTHER_CITIES = [
    ["Азов", "174136"],
    ["Аксай", "174151"],
    ["Альметьевск", "174184"],
    ["Анапа", "174191"],
    ["Балашиха", "174292"],
    ["Бокситогорск", "174373"],
    ["Бора", "174402"],
    ["Видное", "174508"],
    ["Волоколамск", "174522"],
    ["Воскресенск", "174530"],
    ["Высоковск", "174541"],
    ["Голицын", "174573"],
    ["Дмитров", "174634"],
    ["Домодедово", "174640"],
    ["Дрезна", "174644"],
    ["Егорьевск", "174659"],
    ["Истра", "174832"],
    ["Кашира", "174957"],
    ["Клин", "175004"],
    ["Кострома", "175050"],
    ["Котельник", "175051"],
    ["Красногорск", "175071"],
    ["Краснозаводск", "175075"],
    ["Кубинка", "175104"],
    ["Ликино-Дулёво", "175209"],
    ["Лосино-Петровский", "175219"],
    ["Луховицы", "175226"],
    ["Люберцы", "175231"],
    ["Можайск", "175349"],
    ["Мытищи", "175378"],
    ["Набережные Челны", "175380"],
    ["Назрань", "175389"],
    ["Одинцово", "175578"],
    ["Орёл", "175604"],
    ["Павловский Посад", "175635"],
    ["Пушкин", "175744"],
    ["Раменское", "175758"],
    ["Руза", "175785"],
    ["Сергиевом Посад", "175864"],
    ["Солнечногорск", "175903"],
    ["Ступино", "175996"],
    ["Талдом", "176052"],
    ["Тверь", "176083"],
    ["Уфа", "176245"],
    ["Хотьково", "176281"],
    ["Черноголовка", "176316"],
    ["Чехов", "176321"],
    ["Шатура", "176366"],
    ["Щёлково", "176401"],
    ["Электрогорск", "176405"],
    ["Яхрома", "176463"],
]

CITIES.extend(OTHER_CITIES)

METRO_STATIONS = {
    "Московский": [
        ["Авиамоторная", "1"],
        ["Автозаводская", "2"],
        ["Академическая", "3"],
        ["Александровский сад", "4"],
        ["Алексеевская", "5"],
        ["Алтуфьево", "6"],
        ["Аннино", "7"],
        ["Арбатская", "8"],
        ["Аэропорт", "9"],
        ["Бабушкинская", "10"],
        ["Багратионовская", "11"],
        ["Баррикадная", "12"],
        ["Бауманская", "13"],
        ["Беговая", "14"],
        ["Белорусская", "15"],
        ["Беляево", "16"],
        ["Бибирево", "17"],
        ["Библиотека им. Ленина", "18"],
        ["Новоясеневская", "19"],
        ["Боровицкая", "20"],
        ["Ботанический сад", "21"],
        ["Братиславская", "22"],
        ["Бульвар Адмирала Ушакова", "23"],
        ["Бульвар Дмитрия Донского", "24"],
        ["Бунинская аллея", "25"],
        ["Варшавская", "26"],
        ["ВДНХ", "27"],
        ["Владыкино", "28"],
        ["Водный стадион", "29"],
        ["Войковская", "30"],
        ["Волгоградский проспект", "31"],
        ["Волжская", "32"],
        ["Воробьёвы горы", "33"],
        ["Выхино", "34"],
        ["Выставочная", "35"],
        ["Динамо", "36"],
        ["Дмитровская", "37"],
        ["Добрынинская", "38"],
        ["Домодедовская", "39"],
        ["Дубровка", "40"],
        ["Измайловская", "41"],
        ["Калужская", "42"],
        ["Кантемировская", "43"],
        ["Каховская", "44"],
        ["Каширская", "45"],
        ["Киевская", "46"],
        ["Китай-город", "47"],
        ["Кожуховская", "48"],
        ["Коломенская", "49"],
        ["Комсомольская", "50"],
        ["Коньково", "51"],
        ["Красногвардейская", "52"],
        ["Красносельская", "53"],
        ["Красные ворота", "54"],
        ["Крестьянская застава", "55"],
        ["Кропоткинская", "56"],
        ["Крылатское", "57"],
        ["Кузнецкий мост", "58"],
        ["Кузьминки", "59"],
        ["Кунцевская", "60"],
        ["Курская", "61"],
        ["Кутузовская", "62"],
        ["Ленинский проспект", "63"],
        ["Лубянка", "64"],
        ["Люблино", "65"],
        ["Марксистская", "66"],
        ["Марьино", "67"],
        ["Маяковская", "68"],
        ["Медведково", "69"],
        ["Международная", "70"],
        ["Менделеевская", "71"],
        ["Молодёжная", "72"],
        ["Нагатинская", "73"],
        ["Нагорная", "74"],
        ["Нахимовский проспект", "75"],
        ["Новогиреево", "76"],
        ["Новокузнецкая", "77"],
        ["Новослободская", "78"],
        ["Новые Черёмушки", "79"],
        ["Октябрьская", "80"],
        ["Октябрьское поле", "81"],
        ["Орехово", "82"],
        ["Отрадное", "83"],
        ["Охотный ряд", "84"],
        ["Павелецкая", "85"],
        ["Парк Культуры", "86"],
        ["Парк Победы", "87"],
        ["Партизанская", "88"],
        ["Первомайская", "89"],
        ["Перово", "90"],
        ["Петровско-Разумовская", "91"],
        ["Печатники", "92"],
        ["Пионерская", "93"],
        ["Планерная", "94"],
        ["Площадь Ильича", "95"],
        ["Площадь Революции", "96"],
        ["Полежаевская", "97"],
        ["Полянка", "98"],
        ["Пражская", "99"],
        ["Преображенская площадь", "100"],
        ["Пролетарская", "101"],
        ["Проспект Вернадского", "102"],
        ["Проспект Мира", "103"],
        ["Профсоюзная", "104"],
        ["Пушкинская", "105"],
        ["Речной вокзал", "106"],
        ["Рижская", "107"],
        ["Римская", "108"],
        ["Рязанский проспект", "109"],
        ["Савёловская", "110"],
        ["Свиблово", "111"],
        ["Севастопольская", "112"],
        ["Семёновская", "113"],
        ["Серпуховская", "114"],
        ["Смоленская", "115"],
        ["Сокол", "116"],
        ["Сокольники", "117"],
        ["Спортивная", "118"],
        ["Сретенский бульвар", "119"],
        ["Студенческая", "120"],
        ["Сухаревская", "121"],
        ["Сходненская", "122"],
        ["Таганская", "123"],
        ["Тверская", "124"],
        ["Театральная", "125"],
        ["Текстильщики", "126"],
        ["Тёплый Стан", "127"],
        ["Тимирязевская", "128"],
        ["Третьяковская", "129"],
        ["Трубная", "130"],
        ["Тульская", "131"],
        ["Тургеневская", "132"],
        ["Тушинская", "133"],
        ["Улица 1905 года", "134"],
        ["Улица Академика Янгеля", "135"],
        ["Улица Горчакова", "136"],
        ["Бульвар Рокоссовского", "137"],
        ["Улица Скобелевская", "138"],
        ["Улица Старокачаловская", "139"],
        ["Университет", "140"],
        ["Филёвский парк", "141"],
        ["Фили", "142"],
        ["Фрунзенская", "143"],
        ["Царицыно", "144"],
        ["Цветной бульвар", "145"],
        ["Черкизовская", "146"],
        ["Чертановская", "147"],
        ["Чеховская", "148"],
        ["Чистые пруды", "149"],
        ["Чкаловская", "150"],
        ["Шаболовская", "151"],
        ["Шоссе Энтузиастов", "152"],
        ["Щёлковская", "153"],
        ["Щукинская", "154"],
        ["Электрозаводская", "155"],
        ["Юго-Западная", "156"],
        ["Южная", "157"],
        ["Ясенево", "158"],
        ["Краснопресненская", "159"],
        ["Строгино", "228"],
        ["Славянский бульвар", "229"],
        ["Мякинино", "233"],
        ["Волоколамская", "234"],
        ["Митино", "235"],
        ["Марьина Роща", "236"],
        ["Шипиловская", "238"],
        ["Зябликово", "239"],
        ["Борисово", "240"],
        ["Новокосино", "243"],
        ["Пятницкое шоссе", "244"],
        ["Алма-Атинская", "245"],
        ["Жулебино", "270"],
        ["Лермонтовский проспект", "271"],
        ["Деловой центр", "272"],
        ["Лесопарковая", "273"],
        ["Битцевский парк", "274"],
        ["Спартак", "275"],
        ["Улица Сергея Эйзенштейна", "276"],
        ["Выставочный центр", "277"],
        ["Улица Академика Королёва", "278"],
        ["Телецентр", "279"],
        ["Улица Милашенкова", "280"],
        ["Тропарёво", "281"],
        ["Котельники", "282"],
        ["Технопарк", "283"],
        ["Румянцево", "284"],
        ["Саларьево", "285"],
        ["Фонвизинская", "286"],
        ["Бутырская", "287"],
        ["Хорошёво", "289"],
        ["Зорге", "290"],
        ["Панфиловская", "291"],
        ["Стрешнево", "292"],
        ["Балтийская", "293"],
        ["Коптево", "294"],
        ["Лихоборы", "295"],
        ["Окружная", "296"],
        ["Ростокино", "297"],
        ["Белокаменная", "298"],
        ["Локомотив", "299"],
        ["Измайлово", "300"],
        ["Соколиная гора", "301"],
        ["Андроновка", "302"],
        ["Нижегородская", "303"],
        ["Новохохловская", "304"],
        ["Угрешская", "305"],
        ["ЗИЛ", "306"],
        ["Верхние котлы", "307"],
        ["Крымская", "308"],
        ["Площадь Гагарина", "309"],
        ["Лужники", "310"],
        ["Шелепиха", "311"],
        ["Минская", "337"],
        ["Ломоносовский проспект", "338"],
        ["Раменки", "339"],
        ["Ховрино", "349"],
        ["Петровский Парк", "350"],
        ["Хорошёвская", "351"],
        ["ЦСКА", "352"],
        ["Верхние Лихоборы", "353"],
        ["Селигерская", "354"],
        ["Мичуринский проспект", "361"],
        ["Озёрная", "362"],
        ["Говорово", "363"],
        ["Солнцево", "364"],
        ["Боровское шоссе", "365"],
        ["Новопеределкино", "366"],
        ["Рассказовка", "367"],
        ["Беломорская", "369"],
        ["Косино", "370"],
        ["Улица Дмитриевского", "371"],
        ["Лухмановская", "372"],
        ["Некрасовка", "373"],
        ["Юго-Восточная", "374"],
        ["Окская", "375"],
        ["Стахановская", "376"],
        ["Филатов Луг", "377"],
        ["Прокшино", "378"],
        ["Ольховая", "379"],
        ["Коммунарка", "380"],
        ["Лефортово", "381"],
        ["Шереметьевская", "383"],
        ["Рижская", "384"],
        ["Сокольники", "385"],
        ["Электрозаводская", "386"],
        ["Кленовый бульвар", "387"],
        ["Нагатинский Затон", "388"],
        ["Зюзино", "389"],
        ["Воронцовская", "390"],
        ["Новаторская", "391"],
        ["Аминьевская", "392"],
        ["Давыдково", "393"],
        ["Кунцевская", "394"],
        ["Мнёвники", "395"],
        ["Терехово ", "396"],
        ["Карамышевская", "397"],
        ["Яхромская", "398"],
        ["Лианозово", "399"],
        ["Тестовская", "400"],
        ["Рабочий посёлок", "401"],
        ["Сетунь", "402"],
        ["Немчиновка", "403"],
        ["Сколково", "404"],
        ["Баковка", "405"],
        ["Одинцово", "406"],
        ["Лобня", "407"],
        ["Хлебниково", "408"],
        ["Водники", "409"],
        ["Долгопрудная", "410"],
        ["Новодачная", "411"],
        ["Марк", "412"],
        ["Бескудниково", "413"],
        ["Дегунино", "414"],
        ["Нахабино", "415"],
        ["Аникеевка", "416"],
        ["Опалиха", "417"],
        ["Красногорская", "418"],
        ["Павшино", "419"],
        ["Пенягино", "420"],
        ["Трикотажная", "421"],
        ["Стрешнево", "422"],
        ["Красный Балтиец", "423"],
        ["Гражданская", "424"],
        ["Москва-Товарная", "425"],
        ["Калитники", "426"],
        ["Люблино", "427"],
        ["Депо", "428"],
        ["Перерва", "429"],
        ["Москворечье", "430"],
        ["Покровское", "431"],
        ["Красный Строитель", "432"],
        ["Битца", "433"],
        ["Щербинка", "434"],
        ["Силикатная", "435"],
        ["Подольск", "436"],
        ["Бутово", "437"],
        ["Остафьево", "438"],
        ["Курьяново", "439"],
        ["Народное Ополчение", "440"],
        ["Площадь трёх вокзалов", "441"],
        ["Авиамоторная", "443"],
        ["Деловой центр", "444"],
        ["Каширская", "445"],
        ["Лефортово", "446"],
        ["Мичуринский проспект", "447"],
        ["Нижегородская", "448"],
        ["Печатники", "449"],
        ["Проспект Вернадского", "450"],
        ["Савёловская", "451"],
        ["Текстильщики", "452"],
        ["Шелепиха", "453"],
        ["Марьина Роща", "454"],
        ["Зеленоград — Крюково", "455"],
        ["Фирсановская", "456"],
        ["Сходня", "457"],
        ["Подрезково", "458"],
        ["Новоподрезково", "459"],
        ["Молжаниново", "460"],
        ["Химки", "461"],
        ["Левобережная", "462"],
        ["Ховрино", "463"],
        ["Грачёвская", "464"],
        ["Моссельмаш", "465"],
        ["Лихоборы", "466"],
        ["Петровско-Разумовская", "467"],
        ["Останкино", "468"],
        ["Электрозаводская", "470"],
        ["Сортировочная", "471"],
        ["Андроновка", "473"],
        ["Перово", "474"],
        ["Плющево", "475"],
        ["Вешняки", "476"],
        ["Выхино", "477"],
        ["Рязанский проспект", "478"],
        ["Ухтомская", "479"],
        ["Люберцы", "480"],
        ["Панки", "481"],
        ["Томилино", "482"],
        ["Красково", "483"],
        ["Котельники", "484"],
        ["Отдых", "488"],
        ["Кратово", "489"],
        ["Есенинская", "490"],
        ["Фабричная", "491"],
        ["Раменское", "492"],
        ["Ипподром", "493"],
        ["Апрелевка", "494"],
        ["Победа", "495"],
        ["Крёкшино", "496"],
        ["Санино", "497"],
        ["Кокошкино", "498"],
        ["Толстопальцево", "499"],
        ["Лесной Городок", "500"],
        ["Внуково", "501"],
        ["Мичуринец", "502"],
        ["Переделкино", "503"],
        ["Солнечная", "504"],
        ["Говорово", "505"],
        ["Очаково", "506"],
        ["Аминьевская", "507"],
        ["Матвеевская", "508"],
        ["Минская", "509"],
        ["Кутузовская", "511"],
        ["Беговая", "513"],
        ["Белорусская", "514"],
        ["Рижская", "517"],
        ["Курская", "519"],
        ["Чухлинка", "522"],
        ["Кусково", "523"],
        ["Новогиреево", "524"],
        ["Реутов", "525"],
        ["Никольское", "526"],
        ["Салтыковская", "527"],
        ["Кучино", "528"],
        ["Ольгино", "529"],
        ["Железнодорожная", "530"],
        ["Физтех", "533"],
        ["Аэропорт Внуково", "535"],
        ["Пыхтино", "536"],
        ["Марьина Роща", "537"],
    ],
    "Казанский": [
        ["Северный Вокзал", "314"],
        ["Яшьлек", "315"],
        ["Козья слобода", "316"],
        ["Кремлёвская", "317"],
        ["Площадь Тукая", "318"],
        ["Суконная слобода", "319"],
        ["Аметьево", "320"],
        ["Горки", "321"],
        ["Проспект Победы", "322"],
        ["Дубравная", "368"],
    ],
    "Петербургский": [
        ["Девяткино", "167"],
        ["Гражданский проспект", "168"],
        ["Академическая", "169"],
        ["Политехническая", "170"],
        ["Площадь Мужества", "171"],
        ["Лесная", "172"],
        ["Выборгская", "173"],
        ["Площадь Ленина", "174"],
        ["Чернышевская", "175"],
        ["Площадь Восстания", "176"],
        ["Владимирская", "177"],
        ["Пушкинская", "178"],
        ["Технологический институт", "179"],
        ["Балтийская", "180"],
        ["Нарвская", "181"],
        ["Кировский завод", "182"],
        ["Автово", "183"],
        ["Ленинский проспект", "184"],
        ["Проспект Ветеранов", "185"],
        ["Парнас", "186"],
        ["Проспект Просвещения", "187"],
        ["Озерки", "188"],
        ["Удельная", "189"],
        ["Пионерская", "190"],
        ["Черная речка", "191"],
        ["Петроградская", "192"],
        ["Горьковская", "193"],
        ["Невский проспект", "194"],
        ["Сенная площадь", "195"],
        ["Фрунзенская", "197"],
        ["Московские ворота", "198"],
        ["Электросила", "199"],
        ["Парк Победы", "200"],
        ["Московская", "201"],
        ["Звездная", "202"],
        ["Купчино", "203"],
        ["Приморская", "204"],
        ["Василеостровская", "205"],
        ["Гостиный двор", "206"],
        ["Маяковская", "207"],
        ["Площадь Александра Невского", "208"],
        ["Елизаровская", "210"],
        ["Ломоносовская", "211"],
        ["Пролетарская", "212"],
        ["Обухово", "213"],
        ["Рыбацкое", "214"],
        ["Комендантский проспект", "215"],
        ["Старая Деревня", "216"],
        ["Крестовский остров", "217"],
        ["Чкаловская", "218"],
        ["Спортивная", "219"],
        ["Садовая", "220"],
        ["Достоевская", "221"],
        ["Лиговский проспект", "222"],
        ["Новочеркасская", "224"],
        ["Ладожская", "225"],
        ["Проспект Большевиков", "226"],
        ["Улица Дыбенко", "227"],
        ["Волковская", "230"],
        ["Звенигородская", "231"],
        ["Спасская", "232"],
        ["Обводный канал", "241"],
        ["Адмиралтейская", "242"],
        ["Международная", "246"],
        ["Бухарестская", "247"],
        ["Проспект Славы", "357"],
        ["Беговая", "355"],
        ["Зенит", "356"],
        ["Проспект Славы", "357"],
        ["Дунайская", "358"],
        ["Шушары", "359"],
        ["Горный институт", "382"],
    ],
    "Самарский": [
        ["Российская", "261"],
        ["Московская", "262"],
        ["Гагаринская", "263"],
        ["Спортивная", "264"],
        ["Советская", "265"],
        ["Победа", "266"],
        ["Безымянка", "267"],
        ["Кировская", "268"],
        ["Юнгородок", "269"],
        ["Победа", "270"],
        ["Алабинская", "312"],
    ],
    "Екатеринбургский": [
        ["Проспект Космонавтов", "340"],
        ["Уралмаш", "341"],
        ["Машиностроителей", "342"],
        ["Уральская", "343"],
        ["Динамо", "343"],
        ["Площадь 1905 года", "345"],
        ["Геологическая", "346"],
        ["Чкаловская", "347"],
        ["Ботаническая", "348"],
    ],
    "Новосибирский": [
        ["Заельцовская", "248"],
        ["Гагаринская", "249"],
        ["Красный Проспект", "250"],
        ["Сибирская", "251"],
        ["Площадь Ленина", "252"],
        ["Октябрьская", "253"],
        ["Речной Вокзал", "254"],
        ["Студенческая", "255"],
        ["Площадь Маркса", "256"],
        ["Площадь Гарина-Михайловского", "257"],
        ["Маршала Покрышкина", "258"],
        ["Березовая Роща", "259"],
        ["Золотая Нива", "260"],
    ],
    "Нижегородский": [
        ["Горьковская", "323"],
        ["Московская", "324"],
        ["Чкаловская", "325"],
        ["Ленинская", "326"],
        ["Заречная", "327"],
        ["Двигатель Революции", "328"],
        ["Пролетарская", "329"],
        ["Автозаводская", "330"],
        ["Комсомольская", "331"],
        ["Кировская", "332"],
        ["Парк культуры", "333"],
        ["Канавинская", "334"],
        ["Бурнаковская", "335"],
        ["Буревестник", "335"],
        ["Стрелка", "360"],
    ],
}
