go:
	docker-compose up -d
	./wait_for_nifi.sh

produce:
	./produce.py

debug:
	docker-compose logs -f debug

clean:
	docker-compose rm -f
