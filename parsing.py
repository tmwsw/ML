import cianparser
from time import sleep

a = 0
while a < 54:
    moscow_parser = cianparser.CianParser(location="Москва")
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=(1),
        with_saving_csv=True,
        additional_settings={"start_page": 1 + a, "end_page": 2 + a},
        with_extra_data=True,
    )
    sleep(60)
    a += 2
