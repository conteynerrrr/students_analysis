"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

students = {}
math_id = 0
python_id = 1
english_id = 2

math_grades = 0
python_grades = 0
english_grades = 0
students_count = 0

math_mean = 0
python_mean = 0
english_mean = 0

current_mvp_student = 0
mvp_student = 0
mvp_student_id = 0

with open(INPUT_FILE, encoding="utf-8") as f:
    next(f)

    for line in f:
        name, *grades = line.strip().split(",")
        grades = [int(g) for g in grades]

        current_mvp_student = sum(grades)/len(grades)
        if current_mvp_student > mvp_student:
            mvp_student = current_mvp_student
            mvp_student_id = name

        math_grades += grades[math_id]
        python_grades += grades[python_id]
        english_grades += grades[english_id]
        students[name] = grades
        students_count += 1

math_mean = round((math_grades / students_count),1)
python_mean = round((python_grades / students_count),1)
english_mean = round((english_grades / students_count),1)
mvp_student = round(mvp_student,1)


# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(f"Середній бал по класу:\nmath : {math_mean}\npython : {python_mean}\nenglish : {english_mean}\n")
    f.write(f"Найкращий студент: {mvp_student_id} ({mvp_student})")
    print(f"Середній бал по класу:\nmath : {math_mean}\npython : {python_mean}\nenglish : {english_mean}\n")
    print(f"Найкращий студент: {mvp_student_id} ({mvp_student})")


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
