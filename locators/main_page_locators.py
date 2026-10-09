from selenium.webdriver.common.by import By

class MainPageLocators:
    #Блок ввода адреса 
    FROM_FIELD = (By.ID, "from")
    WHERE_FIELD = (By.ID, "to")
    
    #Блок карты
    MARK_A = (By.XPATH, "//ymaps[contains(@class, 'ymaps-2-1-79-placemark-overlay')]")
    MARK_B = (By.XPATH, "//ymaps[contains(@class, 'ymaps-2-1-79-placemark-overlay')]")

    #Выбор маршрута
    TYPE_PICKER_BLOCK  = (By.XPATH, "//div[contains(@class, 'type-picker shown')]")
    
    OPTIMAL = (By.XPATH, "//div[contains(@class, 'mode') and contains(text(), 'Оптимальный')]")
    OPTIMAL_ACTIVE = (By.XPATH, "//div[contains(@class, 'mode active') and contains(text(), 'Оптимальный')]")

    FAST = (By.XPATH, "//div[contains(@class, 'mode') and contains(text(), 'Быстрый')]")
    FAST_ACTIVE = (By.XPATH, "//div[contains(@class, 'mode active') and contains(text(), 'Быстрый')]")

    OWN = (By.XPATH, "//div[contains(@class, 'mode') and text()='Свой']")
    OWN_ACTIVE = (By.XPATH, "//div[contains(@class, 'mode active') and text()='Свой']")

    #Выбор транспорта 
    CAR = (By.XPATH, '//img[contains(@src, "/static/media/car.8a2b1ff5.svg")]')
    WALK = (By.XPATH, '//img[contains(@src, "/static/media/walk.d33bf83c.svg")]')
    TAXI = (By.XPATH, '//img[contains(@src, "/static/media/taxi-active.b0be3054.svg")]')
    BIKE = (By.XPATH, '//img[contains(@src, "/static/media/bike.fb41c762.svg")]')
    SCOOTER = (By.XPATH, '//img[contains(@src, "/static/media/scooter.cf9bb57e.svg")]')
    DRIVE= (By.XPATH, '//img[contains(@src, "/static/media/drive.fa5137d7.svg")]')

    #Детали маршрута
    MARKS_A_AND_B_SAME_OUTPUT = (By.XPATH, "//div[contains(@class, 'results-text')]//div[contains(text(), 'Авто Бесплатно')]/following-sibling::div[contains(text(), 'В пути 0 мин')]")
    PRICE_OUTPUT = (By.XPATH, "//div[contains(@class, 'text') and (contains(., 'руб.') or contains(., 'Бесплатно'))]")
    TIME_OUTPUT = (By.XPATH, "//div[contains(@class, 'duration') and contains(., 'В пути')]")

    CALL_TAXI_BUTTON  = (By.XPATH, "//button[contains(., 'Вызвать такси')]")
    BOOK_BUTTON  = (By.XPATH, "//button[contains(@class, 'button round') and text()='Забронировать']")