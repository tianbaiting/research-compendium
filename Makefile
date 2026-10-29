SHELL := /bin/bash
REVIEWS := $(sort $(notdir $(patsubst %/,%,$(wildcard reviews/*/))))
TEXFLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: all list clean new check $(REVIEWS) template
all: $(REVIEWS)

list:
	@printf '%s\n' $(REVIEWS)

$(REVIEWS):
	cd reviews/$@ && latexmk $(TEXFLAGS) main.tex

template:
	cd templates/review && latexmk $(TEXFLAGS) main.tex

check: all template

clean:
	@for d in $(addprefix reviews/,$(REVIEWS)) templates/review; do (cd $$d && latexmk -C main.tex); done

new:
	@test -n "$(TOPIC)" && test -n "$(TITLE)" || (echo 'Usage: make new TOPIC=my-topic TITLE="My topic"' && exit 2)
	python3 scripts/new_review.py "$(TOPIC)" "$(TITLE)"
