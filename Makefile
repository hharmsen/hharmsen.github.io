TITLE="Henry's Favourite Links"

.PHONY: all

index.html: index.py index.csv
	python index.py index.csv index.html $(TITLE)

all:
	python index.py index.csv index.html $(TITLE)
	make -C family all
	make -C news all
	make -C search all
	make -C weather all
