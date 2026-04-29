MAIN = report

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex


clean:
	rm -f $(MAIN).pdf $(MAIN).aux $(MAIN).log $(MAIN).toc $(MAIN).out
