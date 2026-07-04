from selenium.webdriver.common.by import By

class TaxiPageLocators:
    #Тарифы
    TARIFF_BLOCK = (By.XPATH, "//div[contains(@class, 'tariff-picker shown')]")

    WORK_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(text(), 'Рабочий')]")
    I_BUTTON_WORK = (By.XPATH, "//button[@data-for='tariff-card-0']")
    INFO_TITLE_WORK = (By.XPATH, "//div[@id='tariff-card-0']//div[@class='i-title']")
    INFO_DESCRIPTION_WORK = (By.XPATH, "//div[@id='tariff-card-0']//div[@class='i-dPrefix']")

    SLEEPY_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Сонный')]")
    I_BUTTON_SLEEPY = (By.XPATH, "//button[@data-for='tariff-card-1']")
    INFO_TITLE_SLEEPY = (By.XPATH, "//div[@id='tariff-card-1']//div[@class='i-title']")
    INFO_DESCRIPTION_SLEEPY = (By.XPATH, "//div[@id='tariff-card-1']//div[@class='i-dPrefix']")

    VACATION_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Отпускной')]")
    I_BUTTON_VACATION = (By.XPATH, "//button[@data-for='tariff-card-2']")
    INFO_TITLE_VACATION = (By.XPATH, "//div[@id='tariff-card-2']//div[@class='i-title']")
    INFO_DESCRIPTION_VACATION = (By.XPATH, "//div[@id='tariff-card-2']//div[@class='i-dPrefix']")
    
    TALKATIVE_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Разговорчивый')]")
    I_BUTTON_TALKATIVE = (By.XPATH, "//button[@data-for='tariff-card-3']")
    INFO_TITLE_TALKATIVE = (By.XPATH, "//div[@id='tariff-card-3']//div[@class='i-title']")
    INFO_DESCRIPTION_TALKATIVE = (By.XPATH, "//div[@id='tariff-card-3']//div[@class='i-dPrefix']")

    COMFORTING_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Утешительный')]")
    I_BUTTON_COMFORTING = (By.XPATH, "//button[@data-for='tariff-card-4']")
    INFO_TITLE_COMFORTING = (By.XPATH, "//div[@id='tariff-card-4']//div[@class='i-title']")
    INFO_DESCRIPTION_COMFORTING = (By.XPATH, "//div[@id='tariff-card-4']//div[@class='i-dPrefix']")

    GLOSSY_TARIFF = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Глянцевый')]")
    I_BUTTON_GLOSSY = (By.XPATH, "//button[@data-for='tariff-card-5']")
    INFO_TITLE_GLOSSY = (By.XPATH, "//div[@id='tariff-card-5']//div[@class='i-title']")
    INFO_DESCRIPTION_GLOSSY = (By.XPATH, "//div[@id='tariff-card-5']//div[@class='i-dPrefix']")
    
    #Поля в блоке заказа такси
    PHONE_FIELD = (By.XPATH, "//div[contains(@class, 'np-button')]//div[contains(text(), 'Телефон')]")
    COMMENT_FIELD = (By.XPATH, "//div[contains(@class, 'input-container')]//label[contains(text(), 'Комментарий водителю...')]")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[contains(@class, 'pp-button filled')]//div[contains(text(), 'Способ оплаты')]")
    REQUIREMENTS_BUTTON = (By.XPATH, "//div[contains(@class, 'reqs-header')]//div[contains(text(), 'Требования к заказу')]")
    MAKE_ODER_BUTTON = (By.XPATH, "//div[contains(@class, 'smart-button')]")
    CHECK_BOX = (By.XPATH, "//span[contains(@class, 'slider round')]")

    EXPECTED_COST = (By.XPATH, "//div[contains(@class, 'tcard active')]//div[contains(@class, 'tcard-price')]")

    #Окно поиск машины
    TIMER = (By.XPATH, "//div[contains(@class, 'order-header-time')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='close']")
    DETAILS_BUTTON = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='burger']")
    CAR_SEARCH_TITLE  =(By.XPATH, "//div[contains(@class, 'order-header-title')]")

    #Окно завершённого заказа
    COMPLETED_ODER_TITLE = (By.XPATH, "//img[@src='/static/media/chewron.f3fff088.svg']")
    CAR_NUMBER = (By.XPATH, "//div[contains(@class, 'order-number')]//div[contains(@class, 'number')]")
    TARIFF_IMAGE = (By.XPATH, "//img[@alt='Car']")
    DRIVER_NAME = (By.XPATH, "//div[contains(@class, 'order-btn-group')]")
    DRIVER_RAITING = (By.XPATH, "//div[contains(@class, 'order-btn-rating')]")
    FIN_CANCEL_BUTTON = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='close']")
    FIN_DETAILS_BUTTON  = (By.XPATH, "//button[contains(@class, 'order-button')]//img[@alt='burger']")
    FIN_COST = (By.XPATH, "//div[@class='o-d-sh'][contains(text(), 'Стоимость')]")
