from pyld import jsonld
import json
from argparse import ArgumentParser


argparser = ArgumentParser()
argparser.add_argument('--modelfile', '-M', type=str, help='Relative path to a model\'s filled-out metadata JSON file')
args = argparser.parse_args()

with open(args.modelfile) as file:
    modeljson = file.read()
with open('jsonld-context.json') as file:
    contextjson = file.read()
context = json.loads(contextjson)
model = json.loads(modeljson)
merge = dict(context, **model)

expanded = jsonld.expand(merge)

normalized = jsonld.normalize(expanded, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})

with open('graph-out.nq', 'w') as outfile:
    outfile.write(normalized)

print('fin')
