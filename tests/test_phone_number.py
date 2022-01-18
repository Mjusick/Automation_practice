from pages.main_page import MainPage


def test_phone_number(driver):
    main_page = MainPage(driver)
    expected_phone_number = '0123-456-789'
    actual_phone_number = main_page.get_phone_number()
    assert expected_phone_number == actual_phone_number
