all: encoding.pdf
figs=$(wildcard *.ipe)
pdffigs=$(figs:.ipe=.pdf)


encoding.pdf : encoding.tex $(pdffigs) entropy.pdf
	latexmk -pdf encoding.tex

#entropy.pdf : entropy.py
#	python entropy.py

%.pdf : %.ipe
	ipetoipe -pdf $<

clean :
	rm -f $(pdffigs) *.log *.bbl *.aux

