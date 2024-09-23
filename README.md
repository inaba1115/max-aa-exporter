# max-aa-exporter

This exports max pacher as ascii art.

## prerequisite
Install [graph-easy](https://github.com/ironcamel/Graph-Easy).
```
$ cpan Graph::Easy  # mac
```

## usage
```
$ poetry run python -m max_aa_exporter -f ./testdata/hello.maxpat | graph-easy
+-----------+
|    btn    |
+-----------+
  |
  |
  v
+-----------+
| msg:hello |
+-----------+
  |
  |
  v
+-----------+
| obj:print |
+-----------+
```
