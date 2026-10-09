# Sprint_10
UI testing, applying Page Object Model, Allure report.  
Task: write auto-tests for the educational service ["Yandex.Routes"](https://qa-routes.education-services.ru).  
Imagine that a manual tester handed you scenarios. They need to be covered with auto-tests.

## 1. Preparation
* Chrome browser is installed
* Selenium and Allure are connected.
* Studied the use of `setTimeout` in the console when testing, the `hover` method from selenium and the `@pytest.mark.xfail` decorator

## 2. Study of test scenarios
The program has 2 pre-set addresses: `Хамовнический вал, 34` and `Зубовский бульвар, 37`. You can use them in any order

### Route rendering
You need to check: 
* When entering two different pre-set addresses in the "Откуда" and "Куда" fields, two points of the route start and end are displayed on the map

### Display of the route selection block
You need to check: 
* When entering two different pre-set addresses in the "Откуда" and "Куда" fields, a block with route selection is displayed below the address selection
* When entering the same address in the "Откуда" and "Куда" fields, a route selection block is displayed below the address selection with the text "Авто Бесплатно В пути 0 мин."

### Preparation for ordering a taxi. Enter two different pre-set addresses in the "Откуда" and "Куда" fields
You need to check: 
* When switching between route types (Оптимальный\Быстрый), the active tab changes and the time and cost of the route are recalculated
* When switching to a route type Свой, the active tab changes and movement types become active (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)
* When selecting a route type Быстрый, the Вызвать такси button is active
* When selecting a route type Свой, movement type Драйв, the Забронировать button is active

### Ordering a Taxi tariff. Enter two different pre-set addresses in the "Откуда" and "Куда" fields, select Быстрый route type, click the Вызвать такси button
You need to check: 
* An order form opens with all 6 tariffs according to the TZ, one of them is active
* When hovering over the i icon in the upper right corner of each tariff, a pop-up window appears with a description of the tariff, the tariff description matches the TZ
* Below the tariffs is a block with fields Телефон, Способ оплаты, Комментарий водителю, Требования к заказу

### Scenario. Enter two different pre-set addresses in the "Откуда" and "Куда" fields, select Быстрый route type, click the Вызвать такси button
You need to check:
* Select the Рабочий tariff, enable the Столик для ноутбука checkbox, click the Ввести номер и заказать button - A window appears waiting for the car (check elements according to TZ)
* Wait for the machine search timer to end - A window of the completed order appears (check elements according to TZ)
* Click the Детали button in the Еще про поездку block - The cost that was when choosing a tariff is indicated
* Click the Отмена button - The window closes

### TZ and interfaces
#### 1. Initial screen block:
- Map in the right part of the screen
- Block with address input: Откуда, Куда
#### 2. Route selection block:
- Route types: Оптимальный, Быстрый, Свой
- Movement types: Машина, Пешком, Такси, Велосипед, Самокат, Драйв
- Information block: Cost, Travel time
- Вызвать такси button for Такси type
- Забронировать button for Драйв type
#### 3. Taxi order block:
- Tariffs: Рабочий, Сонный, Отпускной, Разговорчивый, Утешительный, Глянцевый
- Fields to fill: Телефон, Способ оплаты, Комментарий водителю, Требования к заказу
- Ввести номер и заказать button
- Description of Taxi tariffs:
  - Рабочий - Для деловых особ, которых отвлекают
  - Сонный - Для тех, кто не выспался
  - Отпускной - Если пришла пора отдохнуть
  - Разговорчивый - Если мысли не выходят из головы
  - Утешительный - Если хочется свернуться калачиком
  - Глянцевый - Если нужно блистать
- Taxi waiting window:
  - Title: Поиск машины
  - Countdown timer in the upper right corner
- Buttons: Отменить, Детали
- Детали window:
  - Addresses: Адрес подачи, Адрес назначения (the addresses entered in the "Откуда" and "Куда" fields are indicated)
  - Payment method (information from the Способ оплаты field from the Taxi order form is indicated)
  - Information block: title Еще про поездку, information Cost
- Taxi completed order window:
  - Title: n мин. и приедет >
  - Car number and tariff image in the upper right corner
  - Information block about the driver: Name, photo, rating in the upper right corner of the photo
  - Buttons: Отменить, Детали
- Drive order block:
  - Tariffs: Повседневный, Походный, Роскошный
  - Fields to fill: Добавить права, Способ оплаты, Требования к заказу
  - Ввести права и забронировать button
- Description of Drive tariffs:
  - Повседневный - BMW 750 Просто по делам, ничего лишнего
  - Походный - KIA RIO Для путешествий
  - Роскошный - PORSCHE 911 Блеск, мощь, глянец
- Drive tariff rights addition window:
  - Fields to fill: Имя, Фамилия, Дата рождения, Номер
  - Buttons: Добавить, Отмена
- Drive completed order window:
  - Title: Машина забронирована
  - Description: Бесплатное ожидание и таймер in the upper right corner
  - Image of the selected tariff picture and tariff name above it
  - Отменить button
- Information block: Car address (the address entered in the "Откуда" field is indicated), Еще про поездку (Cost)

## 3. Writing tests
- Describe the necessary locators using Page Object. Create a separate package for Page Object. For each page, you need to create a separate class with Page Object.
- Write tests on Selenium.
- Tests need to be divided by topic or functionality. Note: you do not need to create a separate class for each test. Add tests for one functionality in one class. All tests should be in the test directory. Check that the tests run.

There are bugs in the functionality, tests should correspond to the TZ, so tests that reveal bugs should fail when running

## 4. Creating an Allure report
Make a report in Allure. Generate an Allure report and push it to the repository.
