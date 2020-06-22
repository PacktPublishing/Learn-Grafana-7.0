IMAGE=python
TAG=$(IMAGE)/ch6

WXBIN=bin/weather.py
WXDB=weatherdb
WXTEMPFILE=data/wx.txt
STATIONS=KSFO,KDEN,KSTL,KJFK

EQBIN=bin/earthquake.py
EQIMAGE=earthquake
EQDB=earthquakedb
EQTEMPFILE=data/eq.txt
EQSIZE=all
EQWINDOW=week


build:
	docker-compose pull

up:
	docker-compose up -d

down:
	docker-compose down

start:
	docker-compose start

stop:
	docker-compose stop

build-$(IMAGE):
	docker build --pull --tag $(TAG) .

dump-weather:
	docker run --rm --network=host -v "$$(PWD):/usr/src/app" --name $(IMAGE) $(TAG) \
		$(WXBIN) --output $(WXTEMPFILE) --stations $(STATIONS)

load-weather:
	docker run --rm --network=host -v "$$(PWD):/usr/src/app" --name $(IMAGE) $(TAG) \
 		$(WXBIN) --input $(WXTEMPFILE) --db $(WXDB)

drop-weather:
	docker run --rm --network=host --name $(IMAGE) $(TAG) \
 		$(WXBIN) --drop --db $(DB)

reload-weather: dump-weather load-weather

full-reload-weather: drop-weather reload-weather

dump-earthquake:
	docker run --rm --network=host -v "$$(PWD):/usr/src/app" --name $(IMAGE) $(TAG) \
		$(EQBIN) --size $(EQSIZE) --window $(EQWINDOW) --output $(EQTEMPFILE)

load-earthquake:
	docker run --rm --network=host -v "$$(PWD):/usr/src/app" --name $(IMAGE) $(TAG) \
 		$(EQBIN) --input $(EQTEMPFILE) --db $(EQDB)

drop-earthquake:
	docker run --rm --network=host --name $(IMAGE) $(TAG) \
 		$(EQBIN) --drop --db $(DB)

reload-earthquake: dump-earthquake load-earthquake

full-reload-earthquake: drop-earthquake reload-earthquake

test-influxdb:
	curl -i http://localhost:8086/ping

auto: build up test-influxdb build-$(IMAGE) reload-weather reload-earthquake down
