# FSKX Linked Data

This project is meant for developments regarding the transformation of the FSKX Metadata Schema to linked data.

`genericModelMetadataSchema_104.json` is the JSON Schema file defining the current FSKX Metadata Schema version. 

## The context
`jsonld-context.json` contains a context object for JSON-LD, which is meant to be prepended to a filled-out FSKX metadata JSON file, to result in meaningful JSON-LD.
- Contains the newest mappings found
- `"?"` for items that still require a mapping
- `"..."` used when a node's children still need to be inserted
- `example.org`-mappings used as placeholder
