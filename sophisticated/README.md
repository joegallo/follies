# Sophisticated

An implementation of a 'sophisticated' document encoding mechanism for
storing data in Elasticsearch.

The python bits implement a little encoder and decoder, so it works like this:

```
$ echo -n '{"foo":1, "bar":true, "baz":3, "message":"what hath god wrought?"}' | ./sophisticated.py -e 789 | ./sophisticated.py -d
{"foo":1, "bar":true, "baz":3, "message":"what hath god wrought?"}
```

The encoder spits out document chunks encoded as a series of Elasticsearch index names, which you can store with PUT:

```
$ for index in $(echo -n '{"foo":1, "bar":true, "baz":3, "message":"what hath god wrought?"}' | ./sophisticated.py -e 456); do curl -XPUT $ES/$index; done
```

And then you can back your documents by pulling the index names for a given document back out of Elasticsearch:

```
$ curl $ES/_cat/indices/456*?s=index | awk '{print $3}' | ./sophisticated.py -d
{"foo":1, "bar":true, "baz":3, "message":"what hath god wrought?"}
```
