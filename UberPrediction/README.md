Uber Trips Prediction

Вебзастосунок на Django для прогнозування кількості поїздок Uber за допомогою моделі машинного навчання.

Опис проєкту

У цьому проєкті використовується набір даних Uber для аналізу кількості поїздок та прогнозування їх кількості залежно від часу.

Модель машинного навчання була навчена за допомогою Python та бібліотеки Scikit-learn. Навчена модель інтегрована у вебзастосунок на Django.

Використані технології
Python
Django
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
HTML / CSS
Машинне навчання

Для прогнозування кількості поїздок використовуються такі ознаки:

Hour — година
Day — день місяця
DayOfWeek — день тижня

Для прогнозування використано модель Random Forest Regressor.

Результати моделі

Фінальна модель показала приблизно такі результати:

MAE: 233.83
RMSE: 323.53
R²: 0.76
Django-застосунок

Django-застосунок містить вебінтерфейс, за допомогою якого користувач може ввести необхідні параметри та отримати прогноз кількості поїздок.

Навчена модель збережена у файлі:

uber_model.pkl

Структура проєкту
UberPrediction/
│
├── manage.py
├── README.md
├── .gitignore
├── uber_model.pkl
│
├── UberPrediction/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── prediction/
    ├── migrations/
    ├── templates/
    │   └── prediction/
    │       └── index.html
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    └── views.py
Встановлення

Клонувати репозиторій:

git clone https://github.com/pavlenkosasha/MillionaireAPI.git

Перейти до папки проєкту:

cd UberPrediction

Створити віртуальне середовище:

python -m venv .venv

Активувати віртуальне середовище у Windows:

.venv\Scripts\activate

Встановити необхідні бібліотеки:

pip install django pandas numpy scikit-learn joblib
Запуск проєкту

Запустити Django-сервер:

python manage.py runserver

Після запуску відкрити у браузері:

http://127.0.0.1:8000/
Автор

Oleksandr Pavlenko