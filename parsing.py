import cianparser
from time import sleep

a = 0
while a < 12:
    moscow_parser = cianparser.CianParser(location="Дубна")
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=("all"),
        with_saving_csv=True,
        additional_settings={"start_page": 1 + a, "end_page": 2 + a},
        with_extra_data=True,
    )
    sleep(60)
    a += 2
