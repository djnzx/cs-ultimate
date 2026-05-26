IMAGE := cs-env-01-python-libs-minimal:latest

rebuild:
	docker build -t $(IMAGE) .
start:
	docker compose up -d
status:
	docker ps
open:
	open http://localhost:8888
stop:
	docker stop dev-env-jupiter-notebook-1
restart:
	$(MAKE) stop
	$(MAKE) start
