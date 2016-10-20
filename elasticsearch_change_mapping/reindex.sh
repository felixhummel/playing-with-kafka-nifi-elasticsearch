#!/bin/bash
set -euo pipefail

base=http://localhost:9200

# refresh=wait_for blocks until done
# https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-refresh.html
curl -s -XPOST "$base/_reindex?pretty&refresh=wait_for" -d @- <<EOF
{
  "source": { "index": "$1" },
  "dest": { "index": "$2" }
}
EOF

