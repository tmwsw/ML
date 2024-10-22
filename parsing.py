import cianparser
from time import sleep

a = 0
while a < 108:
    moscow_parser = cianparser.CianParser(location="Москва")
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=(1, 2),
        with_saving_csv=True,
        additional_settings={"start_page": 33 + a, "end_page": 34 + a},
        with_extra_data=True,
    )
    sleep(120)
    a += 2