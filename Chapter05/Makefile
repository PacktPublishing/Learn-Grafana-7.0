IMAGE=weather
TAG=$(IMAGE)/ch5
DB=weatherdb
TEMPFILE=wx.txt
STATIONS=KSFO,KDEN,KSTL,KJFK

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

dump-$(IMAGE):
	docker run --rm --network=host -v "$$(PWD):/usr/src/app" --name $(IMAGE) $(TAG) \
		--output $(TEMPFILE) --stations $(STATIONS)

load-$(IMAGE):
	docker run --rm --network=host -v "$$(PWD):/usr/src/app" --name $(IMAGE) $(TAG) \
 		--input $(TEMPFILE) --db $(DB)

drop-$(IMAGE):
	docker run --rm --network=host --name $(IMAGE) $(TAG) \
 		--drop --db $(DB)

reload: dump-$(IMAGE) load-$(IMAGE)

full-reload: drop-$(IMAGE) dump-$(IMAGE) load-$(IMAGE)

test-influxdb:
	curl -i http://localhost:8086/ping

auto: build up test-influxdb build-$(IMAGE)  dump-$(IMAGE) load-$(IMAGE) down
