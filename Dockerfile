FROM python:3.7-alpine
EXPOSE 5000
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./solar-divert.py" ]
