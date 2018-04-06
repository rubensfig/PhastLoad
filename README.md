[![Build Status](https://travis-ci.org/rubensfig/PhastLoad.svg?branch=master)](https://travis-ci.org/rubensfig/PhastLoad)

testing 

```  
virtualenv .env -p python3
source .env/bin/activate
cd phastload
./manage.py runserver
```

build the image

``` sudo docker build -t phastload . ```

run the file

``` sudo docker run -dp 80:80 --name phastload phastload ```

Access the Web page

``` localhost/index ```
