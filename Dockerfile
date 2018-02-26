FROM python AS py
COPY requirements.txt /project/requirements.txt
WORKDIR /project
RUN pip install -r requirements.txt
ENV BOT_TOKEN 474745948:AAHdH9xTT6piTpD3em6XFG2VN-WK2Apfpo4
ENV TELEGRAM_CHANNEL @md_info
ENTRYPOINT ["/bin/bash", "-c", "python run.py"]