from tenzorpage import SearchHelper
import time

def test_tenzor_page(browser):
    tenzor_page = SearchHelper(browser)
    tenzor_page.go_to_site()
    tenzor_page.open_tenzor_main_page()
    power_in_people = tenzor_page.check_working_block()
    assert power_in_people == 'Сила в людях'
    tenzor_page.move_to_more_details_link()
    photos_size = tenzor_page.check_photos_size()
    assert photos_size == "Фото одного размера"