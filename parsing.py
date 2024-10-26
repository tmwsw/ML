import cianparser
from time import sleep

a = 0
while a < 22:
    moscow_parser = cianparser.CianParser(location="Москва")
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=("all"),
        with_saving_csv=True,
        additional_settings={"start_page": 33 + a, "end_page": 34 + a, "sort_by": "creation_data_from_newer_to_older",},
        with_extra_data=True,
    )
    sleep(60)
    a += 2
