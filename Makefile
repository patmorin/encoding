all: encoding.pdf
figs=$(wildcard *.ipe)
pdffigs=$(figs:.ipe=.pdf)


encoding.pdf : encoding.tex  $(pdffigs)
	latexmk -pdf encoding.tex

%.pdf : %.ipe
	ipetoipe -pdf $<


