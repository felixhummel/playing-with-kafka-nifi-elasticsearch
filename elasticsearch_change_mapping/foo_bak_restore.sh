#!/bin/bash
set -euo pipefail

base=http://localhost:9200

set -x
# inspect
curl -s $base/_cat/indices?v | grep foo_bak
# downtime begins
curl -s -XDELETE $base/foo?pretty
./reindex.sh foo_bak foo
# downtime ends
# cleanup
curl -s -XDELETE $base/foo_bak?pretty
