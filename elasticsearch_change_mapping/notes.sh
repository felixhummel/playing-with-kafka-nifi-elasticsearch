base=http://localhost:9200

curl -s -XGET /_cat/indices?v
curl -s -XGET $base/foo/_mapping?pretty > old_mapping.json
jq .foo old_mapping.json > new_mapping.json
vi new_mapping.json
# "index": "not_analyzed"
curl -s -XPUT /foo_v2 -d @new_mapping.json

curl -s -XPOST $base/_reindex?pretty -d @reindex-foo-foo_bak.json
curl -s -XPOST $base/_reindex?pretty -d @reindex.json

curl -s -XDELETE $base/foo

curl -s -XPOST $base/_aliases?pretty -d @alias-foo-foo_v2.json

curl -s -XGET /_cat/indices?v

curl -s -XDELETE $base/foo
