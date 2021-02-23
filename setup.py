from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from shutil import unpack_archive
from os import path

pretrain_name = 'wiki-news-300d-1M.vec'
if not path.exists(pretrain_name):
    zipurl = 'https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip'
    with urlopen(zipurl) as zipresp, NamedTemporaryFile() as tfile:
        print('Downloading the pretrained embeddings...')
        tfile.write(zipresp.read())
        tfile.seek(0)
        unpack_archive(tfile.name, '.', format = 'zip')
        print('Finish downloading pretrained embeddings!')





