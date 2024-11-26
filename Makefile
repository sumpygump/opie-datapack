# Makefile for opie datapack

ccyellow = $(shell echo "\033[33m")
ccend = $(shell tput op)

help:
	@echo "$(ccyellow)------------------------------------------$(ccend)"
	@echo "$(ccyellow)Opie Minecraft Datapack Makefile$(ccend)"
	@echo "$(ccyellow)------------------------------------------$(ccend)"
	@echo "Usage:"
	@echo "  make recipes : Create the generated recipe files"
	@echo "  make format : Normalize format of json files"
	@echo "  make datapack : Regenerate the opie.zip file and move to docs directory"

recipes:
	python3 bin/wood_matrix.py
	python3 bin/wool_matrix.py

format:
	@echo "$(ccyellow)Normalizing format of json files...$(ccend)"
	bin/normalize-json data/opie/advancement/recipes/decoration/*.json
	bin/normalize-json data/opie/advancement/recipes/misc/*.json
	bin/normalize-json data/opie/recipe/*.json
	bin/normalize-json data/opie/recipe/crafting_shapeless/*.json
	bin/normalize-json data/opie/recipe/stone_cutter/*.json
	bin/normalize-json data/opie/recipe/wood_cutter/*.json
	bin/normalize-json data/opie/tags/item/*.json
	@echo "$(ccyellow)Done.$(ccend)"

datapack:
	@echo "$(ccyellow)Creating datapack zip file...$(ccend)"
	zip -r opie data pack.mcmeta
	mv opie.zip docs
	@echo "$(ccyellow)Done.$(ccend)"
	@echo "$(ccyellow)File in 'docs/opie.zip'$(ccend)"
