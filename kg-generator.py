from pyld import jsonld
import json
from argparse import ArgumentParser


argparser = ArgumentParser()
argparser.add_argument('--modelfile', '-M', type=str, help='Relative path to a model\'s filled-out metadata JSON file')
argparser.add_argument('--format_output', '-F', default='jsonld', type=str, help='Output format: "jsonld" (default) or "nquads"')
args = argparser.parse_args()

assert args.format_output in ['jsonld', 'nquads'], 'The supplied format ('+args.format_output+') should be "jsonld" (default) or "nquads"!'

with open(args.modelfile) as file:
    modeljson = file.read()
with open('jsonld-context.json') as file:
    contextjson = file.read()
context = json.loads(contextjson)
model = json.loads(modeljson)
merge = dict(context, **model)

expanded = jsonld.expand(merge)

if args.format_output == 'nquads':
    normalized = jsonld.normalize(expanded, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
    with open('graph-out.nq', 'w') as outfile:
        outfile.write(normalized)
        print('Wrote output to: "graph-out.nq"')
else: #default: args.output_format == 'jsonld'
    with open('graph-out.jsonld', 'w') as outfile:
        outfile.write(json.dumps(expanded))
        print('Wrote output to: "graph-out.jsonld"')

print('fin')
