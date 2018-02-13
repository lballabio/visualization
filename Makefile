
.PHONY: wheel image clean

image: wheel
	cp dist/*.whl docker/visualization
	docker build --rm -t lballabio/visualization docker/visualization

wheel:
	python3 setup.py bdist_wheel

clean:
	rm -rf *.whl docker/visualization/*.whl build dist *.egg-info

