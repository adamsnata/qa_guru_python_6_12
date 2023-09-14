import datetime
from data.users import User
from models.page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ebezgubenko")
@allure.feature("Регистрация пользователя")
@allure.story("Регистрация с полными данными")
@allure.link("https://demoqa.com/automation-practice-form", name="Page for testing form")
def test_success_registration(setup_browser):
    registration_page = RegistrationPage()

    user1 = User(
        first_name='Helen',
        last_name='Bezgubenko',
        email='eb@gmail.com',
        gender='Female',
        mobile_number=9011111111,
        date_of_birth=datetime.date(1993, 11, 1),
        subjects=('Maths', 'Arts', 'Commerce', 'Economics'),
        hobbies=('Sports', 'Reading', 'Music'),
        picture='h.jpg',
        current_address='Istr Street, 17, 21',
        state='NCR',
        city='Delhi'
    )

    registration_page.open()

    registration_page.register(user1)

    registration_page.should_have_registered(user1)
