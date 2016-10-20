#!/bin/bash
set -euo pipefail

base=http://localhost:9200

set -x
# inspect
curl -s $base/_cat/indices?v
# backup
./reindex.sh foo foo_bak

# get and update mapping (note the call to jq here)
curl -s $base/foo/_mapping?pretty | jq .foo > old_mapping.json
patch old_mapping.json action_not_analyzed.patch -o new_mapping.json

# downtime begins
curl -s -XDELETE $base/foo?pretty
curl -s -XPUT $base/foo?pretty -d @new_mapping.json
./reindex.sh foo_bak foo
# downtime ends

