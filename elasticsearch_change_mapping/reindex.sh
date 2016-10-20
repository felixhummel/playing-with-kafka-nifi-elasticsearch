#!/bin/bash
set -euo pipefail

base=http://localhost:9200

curl -s -XPOST $base/_reindex?pretty -d @- <<EOF
{
  "source": { "index": "$1" },
  "dest": { "index": "$2" }
}
EOF

