FROM python
COPY . /usr/local/diplodatos
RUN pip install -r /usr/local/diplodatos/requirements.txt
WORKDIR /usr/local/diplodatos
CMD python /usr/local/diplodatos/scripts/entrypoint.py 
