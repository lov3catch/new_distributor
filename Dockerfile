FROM python AS py
COPY requirements.txt /project/requirements.txt
WORKDIR /project
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "-c", "python run.py"]