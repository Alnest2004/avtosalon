FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
# Устанавливает переменную окружения, которая гарантирует,
# что вывод из python будет отправлен прямо в терминал без
# предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог в контейнере
WORKDIR /Users/Aleksandr/avtosalon

COPY requirements.txt /Users/Aleksandr/avtosalon/requirements.txt
RUN pip install -r requirements.txt

COPY . /Users/Aleksandr/avtosalon/

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

