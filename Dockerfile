FROM python:3.11.1-alpine AS compile-image

RUN apk add gcc musl-dev linux-headers git

COPY requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11.1-alpine AS build-image
COPY --from=compile-image /root/.local /root/.local

WORKDIR /bot
COPY ./ /bot
CMD [ "python", "-u", "/bot/main.py" ]
