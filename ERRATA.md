Chapter 06, Page 133 should read:

  3. Build the Python container to run our scripts:
  
  ```sh
      $ docker build --pull --tag python/ch6 .
  ```
  4. ...
```sh
    $ docker run --rm --network=host -v "$(PWD):/usr/src/app" \
             --name python python/ch6 bin/weather.py \
             --output data/wx.txt \
             --stations KSFO,KDEN,KSTL,KJFK
```
  5. ...
```sh
    $ docker run --rm --network=host -v "$(PWD):/usr/src/app" \
             --name python python/ch6 bin/weather.py \
             --input data/wx.txt \
             --db weatherdb
```
