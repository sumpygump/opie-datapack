# Makefile for opie datapack

ccyellow = $(shell echo "\033[33m")
ccend = $(shell tput op)

help:
	@echo "$(ccyellow)------------------------------------------$(ccend)"
	@echo "$(ccyellow)Opie Minecraft Datapack Makefile$(ccend)"
	@echo "$(ccyellow)------------------------------------------$(ccend)"
	@echo "Usage:"
	@echo "  make datapack : Regenerate the opie.zip file and move to docs directory"

datapack:
	zip -r opie data pack.mcmeta
	mv opie.zip docs
