import time

from pages.elemenets_page import TextBoxPage


class TestElemenets:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            time.sleep(1)
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_field_form()
            assert input_data == output_data
