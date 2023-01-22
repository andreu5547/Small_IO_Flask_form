from flask import Flask, render_template, request  # Импортируем библиотеку Flask

app = Flask(__name__)  # создаем экземпляр класса Flask


@app.route('/', methods=['GET', 'POST'])  # Декоратор, который указывает, что функция будет обрабатывать запросы по адресу /
def index():  # Функция, которая будет обрабатывать запросы по адресу /
    if request.method == 'POST':  # Если данные отправлены, то выполняем код ниже
        input_data = request.form['input']  # Получаем данные из поля input
        ##
        # Здесь вставляем код, который будет выполняться с данными из input
        # input_data - это переменная, в которую записано то, что ввел пользователь в поле input
        # Дальше можно делать с ней что угодно
        # В output_data записываем то, что хотим вывести пользователю, те результат работы программы

        output_data = input_data

        ##
        return render_template('index.html', output=output_data)  # Возвращаем страницу с результатом
    return render_template('index.html')  # Если данные не отправлены, то просто отображаем страницу


if __name__ == '__main__':  # Запускаем приложение
    app.run()
