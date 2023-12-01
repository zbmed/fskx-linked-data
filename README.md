# FSKX Linked Data

This project is meant for developments regarding the transformation of the FSKX Metadata Schema to linked data.

`genericModelMetadataSchema_104.json` is the JSON Schema file defining the current FSKX Metadata Schema version. 

## The context
`jsonld-context.json` contains a context object for JSON-LD, which is meant to be prepended to a filled-out FSKX metadata JSON file, to result in meaningful JSON-LD.

## Knowledge graph generator
- `kg-generator.py` is a utility script that can prepend the JSON-LD context to a given filled-out FSKX metadata JSON file, and save the resulting knowledge graph in the `JSON-LD` and `N-Quads` formats.
- developed for python 3.9
- requirements can be found in requirements.txt
