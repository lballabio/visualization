FROM python:slim
MAINTAINER Luigi Ballabio <luigi.ballabio@gmail.com>
LABEL Description="A slim Jupyter notebook server"

RUN pip install --no-cache-dir jupyter matplotlib numpy scipy pandas RISE \
                               xlrd openpyxl requests BeautifulSoup4

RUN jupyter-nbextension install rise --py --sys-prefix \
 && jupyter-nbextension enable rise --py --sys-prefix

EXPOSE 8888

RUN mkdir /notebooks
VOLUME /notebooks

CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --port=8888 --notebook-dir=/notebooks

