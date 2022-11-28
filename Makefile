install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib test_logic.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	#docker run -p 127.0.0.1:8080:8080 684af06bcd34
deploy:
	#deploy
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 662295231644.dkr.ecr.us-east-1.amazonaws.com
	# docker build -t fastapi-trial .
	# docker tag fastapi-trial:latest 662295231644.dkr.ecr.us-east-1.amazonaws.com/fastapi-trial:latest
	# docker push 662295231644.dkr.ecr.us-east-1.amazonaws.com/fastapi-trial:latest
all: install lint test deploy