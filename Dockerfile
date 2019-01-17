FROM python

COPY ./ /apps

WORKDIR /apps

RUN pip install .

EXPOSE 8080

ENTRYPOINT ["python", "-m", "challenge1.app"]
