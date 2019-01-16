FROM python

COPY ./ /apps

WORKDIR /apps

RUN pip install .

ENTRYPOINT ["python", "-m", "challenge1.app"]
