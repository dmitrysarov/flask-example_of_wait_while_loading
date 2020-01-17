PWD = $(shell pwd)
PORT = 4000
default: 
	make build
	make run
build:
	docker build -t flask .
run:
	docker run --rm -it \
		--name flask_cont \
		-v $(PWD)/python/:/wd/ \
		-p $(PORT):5000 \
	 	-e LANG=C.UTF-8 \
		-e FLASK_APP=application.py \
		-w /wd/ \
		flask /bin/bash -c 'tmux'\
		#-e LC_ALL=C.UTF-8 \                                                     
		#flask /bin/bash -c 'python3 application.py'\
			
