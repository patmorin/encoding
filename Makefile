all: encoding.pdf
figs=$(wildcard *.ipe)
pdffigs=$(figs:.ipe=.pdf)


encoding.pdf : encoding.tex $(pdffigs) entropy.pdf
	latexmk -pdf encoding.tex

%.pdf : %.ipe
	ipetoipe -pdf $<

clean :
	rm -f *.pdf *.log *.bbl *.aux

