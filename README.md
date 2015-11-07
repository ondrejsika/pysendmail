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
        -s smtp.gmail.com:587 \
        -T TRUE


short argumens (inline)

    pysendmail -f from@gmail.com -t to@gmail.com -m "message from pysendmail" -u from@gmail.com -p password -s smtp.gmail.com:587 -T TRUE

long argumens
 
    pysendmail --fromemail from@gmail.com \
        --toeamail to@gmail.com \
        --message "message from pysendmail" \
        --user from@gmail.com \
        --password password \
        --server smtp.gmail.com:587 \
        --tls TRUE

long argumens (inline)

    pysendmail --fromemail from@gmail.com --toeamail to@gmail.com --message "message from pysendmail" --user from@gmail.com --password password --server smtp.gmail.com:587

bash variables

```
PYSENDMAIL_FROM="from@gmail.com"
PYSENDMAIL_USER="from@gmail.com"
PYSENDMAIL_PASSWORD="password"
PYSENDMAIL_SERVER="smtp.gmail.com:587"
PYSENDMAIL_TLS="TRUE"

pysendmail --fromemail from@gmail.com --message "message from pysendmail"
```

or

```
PYSENDMAIL_FROM="from@gmail.com"
PYSENDMAIL_USER="from@gmail.com"
PYSENDMAIL_PASSWORD="password"
PYSENDMAIL_SERVER="smtp.gmail.com:587"
PYSENDMAIL_TLS="TRUE"

PYSENDMAIL_TO="to@gmail.com"
PYSENDMAIL_MESSAGE="message from pysendmail"

pysendmail
```
