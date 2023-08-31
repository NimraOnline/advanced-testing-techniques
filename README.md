# Advanced-testing-techniques
Repo for advanced testing practise

# Setup

1. Create and source virtualenv

```bash
virtualenv ~/.advanced-testing
source ~./advanced-testing/bin/activate
```

2. Create scaffold

```
touch Makefile  && touch README.md  && touch hello.py && touch requirements.txt &&  
touch test_hello.py
```

3. Populate 'Makefile'
```
install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

test:
    python -m pytest -vv -cov=hello --cov=hellocli test_hello.py

lint:
    pylint --disable=R,C hello.py hellocli.py

all: install lint test
```

### How to debug

* Print
* PDB
* Testing