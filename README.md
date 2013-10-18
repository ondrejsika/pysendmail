pysendmail
==========

Send email from Python

#### Authors
*  Ondrej Sika, <http://ondrejsika.com>, ondrej@ondrejsika.com

#### Source
* Python Package Index: <http://pypi.python.org/pypi/pysendmail>
* GitHub: <https://github.com/sikaondrej/pysendmail>

Documentation
-------------

### Installation

    pip install pysendmail

### Example
short arguments
 
    pysendmail -f from@gmail.com \
        -t to@gmail.com \
        -m "message from pysendmail" \
        -u from@gmail.com \
        -p password \
        -s smtp.gmail.com:587


short argumens (inline)

    pysendmail -f from@gmail.com -t to@gmail.com -m "message from pysendmail" -u from@gmail.com -p password -s smtp.gmail.com:587

long argumens
 
    pysendmail --fromemail from@gmail.com \
        --toeamail to@gmail.com \
        --message "message from pysendmail" \
        --user from@gmail.com \
        --password password \
        --server smtp.gmail.com:587

long argumens (inline)

    pysendmail --fromemail from@gmail.com --toeamail to@gmail.com --message "message from pysendmail" --user from@gmail.com --password password --server smtp.gmail.com:587
