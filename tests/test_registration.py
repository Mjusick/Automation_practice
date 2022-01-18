import pytest
from utils.parameters import missing_fields_with_error_messages


def test_registration_successful(client, driver,
                                 main_page, login_page, create_account_page, my_account_page):
    main_page.click_sign_in_button()
    login_page.create_account(client)
    create_account_page.fill_account_form(client)
    create_account_page.submit_account_form()
    assert my_account_page.is_at()


@pytest.mark.parametrize("missing_input, expected_missing_field",
                         [("first_name", "first name"), ("last_name", "last name"), ("password", "password")])
def test_registration_missing_field_highlighted_in_red(client, driver, main_page, login_page, create_account_page,
                                                       missing_input, expected_missing_field):
    main_page.click_sign_in_button()
    login_page.create_account(client)
    create_account_page.fill_account_form_with_missing_field(client, missing_input)
    missing_field_name = create_account_page.field_name_with_missing_parameter().lower()
    assert expected_missing_field in missing_field_name


@pytest.mark.parametrize("missing_field, expected_error_message",
                         missing_fields_with_error_messages)
def test_registration_failed_with_missing_field(client, driver, main_page, login_page, create_account_page,
                                                missing_field, expected_error_message):
    main_page.click_sign_in_button()
    login_page.create_account(client)
    create_account_page.fill_account_form_with_missing_field(client, missing_field)
    create_account_page.submit_account_form()
    error_text = create_account_page.get_error_text()
    assert expected_error_message in error_text

