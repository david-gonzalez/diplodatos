FROM python
COPY root/ /usr/local/diplodatos
RUN pip install -r /usr/local/diplodatos/requirements.txt
WORKDIR /usr/local/diplodatos
CMD python /usr/local/diplodatos/entrypoint.py 
