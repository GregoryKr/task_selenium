from tenzorpage import SearchHelper
import time

def test_tenzor_page(browser):
    tenzor_page = SearchHelper(browser, base_url='https://sbis.ru/contacts/')
    tenzor_page.go_to_site()
    time.sleep(3)
    tenzor_page.open_tenzor_main_page()
    time.sleep(3)
    power_in_people = tenzor_page.check_working_block()
    assert power_in_people == 'Сила в людях'
    tenzor_page.move_to_more_details_link()
    time.sleep(5)
    photos_size = tenzor_page.check_photos_size()
    assert photos_size == "Фото одного размера"