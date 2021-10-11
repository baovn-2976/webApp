FROM python:3

WORKDIR /webApp

COPY . /webApp/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5001

CMD ["python", "webApp.py"]