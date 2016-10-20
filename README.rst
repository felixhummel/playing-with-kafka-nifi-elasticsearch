Usage
=====
Run things via docker compose and get a URL to NiFi::

    make

Now generate some data::

    make produce

Have fun with NiFi.

Make sure the foo index exists and has data:
http://localhost:9200/_cat/indices?v

Next, navigate to `Kibana`_

- Index contains time-based events: checked
- Index name or pattern: ``foo``
- Time-field name: ``date``

.. _Kibana: http://localhost:5601/app/kibana

Create visualization ``count-by-action``:

- Visualize
- Vertical bar chart
- new search
- X-Axis bucket (1)
    - Agg: Date Histogram
    - Field: date
    - Interval: auto
    - CustomLabel: leave empty
- sub-bucket: split bars
    - Agg: terms
    - Field: action
- save: ``count-by-action``

http://localhost:5601/app/kibana#/visualize/edit/count-by-action?_g=(refreshInterval:(display:%275%20seconds%27,pause:!f,section:1,value:5000),time:(from:now-5m,mode:relative,to:now))&_a=(filters:!(),linked:!f,query:(query_string:(analyze_wildcard:!t,query:%27*%27)),uiState:(),vis:(aggs:!((id:%271%27,params:(),schema:metric,type:count),(id:%272%27,params:(customInterval:%272h%27,extended_bounds:(),field:date,interval:auto,min_doc_count:1),schema:segment,type:date_histogram),(id:%273%27,params:(field:action,order:desc,orderBy:%271%27,size:5),schema:group,type:terms)),listeners:(),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,defaultYExtents:!f,mode:stacked,scale:linear,setYExtents:!f,shareYAxis:!t,times:!(),yAxis:()),title:count-by-action,type:histogram))


Pictures!
=========
.. image:: kibana-viz.png


Notes
=====
- ``./consume.py`` may take a while to initialize (TODO: find out why)

DB Notes
========
::

    dc exec nifi java -version
    openjdk version "1.8.0_102"

PG JDBC: https://jdbc.postgresql.org/download.html

- JRE 1.6 --> JDBC4
- JRE 1.7 --> JDBC41
- JRE 1.8 --> JDBC42

Classname: ``org.postgresql.Driver`` (https://jdbc.postgresql.org/documentation/84/load.html)

Connect-URL: ``jdbc:postgresql://postgres/foo`` (``jdbc:postgresql://host/database`` https://jdbc.postgresql.org/documentation/84/connect.html)

DBCPConnectionPool in Process Group Configuration
-------------------------------------------------
TODO: add /opt/nifi/lib/postgresql-9.4.1211.jar to nifi container (volume is
enough)

When you create a QueryDatabaseTable processor, it will prompt to create a
"Database Connection Pooling Service" for the Process Group. Here's the data
it needs:

- Database Connection URL: jdbc:postgresql://postgres/foo
- Database Driver Class Name: org.postgresql.Driver
- Database Driver Location(s): /opt/nifi/lib/postgresql-9.4.1211.jar
- Database User: foo
- Password: foo
