## About

timsaxu is a prototype distributed dictionary for Lojban. A timsaxu instance
is a directory of JSON files. An update map is a JSON file mapping usernames
to lists of URLs. Four scripts are included:

* baseline-convert.py: convert baseline gismu.txt, cmavo.txt, and rafsi.txt to
  a timsaxu instance
* jvs-convert.py: convert jbovlaste XML to a timsaxu instance
* search.py: search a timsaxu instance at the command line
* update.py: use an update map to update a timsaxu instance

Conceptually, a healthy community of valsi zbasu would publish individual
timsaxu instances at public (HTTP) URLs and share update maps which reference
those URLs. Then, individual lookups can be addressed to personal timsaxu
instances, local community timsaxu instances, official LLG timsaxu instances,
etc.

Inspiration comes from RSS, Atom, and JSON Feed; and Nostr.

The structure of individual JSON dictionaries can be intuited from
baseline-convert.py, jvs-convert.py, or search.py; or by running update.py and
examining the downloaded dictionaries, or by considering the following
example:

```
{
    "cmene": "korvo",
    "valsi": [{
        "klesi": "gismu",
        "valsi": "mlatu",
        "velcki": "m₁ is a cat/feline (clade *Feliformia*) of species m₂",
        "xelfanva": [
            {"valsi": "cat"},
            {"valsi": "kitten"},
            {"valsi": "pussy", "notci": "housecat"}
        ]
    }]
}
```

## Contributing

In general, you are welcome to open pull requests.

### Adding new languages

First, get the JVS XML export link. (Ask in chat.) Also, determine the
two-letter ISO code that will be used, or possibly the three-letter code for
e.g. Lojban with "jbo", say `$L`. Finally, determine where to mirror the
instances for bootstrap. (Ask in chat.)

To start a new language, export the corresponding JVS XML. Check both boxes
before exporting to ensure that all records are retrieved! Save it as
something like "jbovlaste.xml". Then run:

    $ mkdir jvs/
    $ python jvs-convert.py jbovlaste.xml

Now the folder "jvs" is a timsaxu instance. Copy it to the mirror location.
This might take some time depending on your hosting provider.

While waiting for that copy, prepare the update map. Determine the base URL
where the instance will be mirrored, say `$BASE`, and then run:

    $ python make-mirror.py jvs/ $BASE > $L.json

Finally, add the new language to the top of search.py.

Now, it's time to test that everything works. First, test the mirror:

    $ mkdir dicts/$L
    $ python update.py $L

Then, test that the new language is available in search:

    $ LANG=$L python search.py mlatu

### Adding new sources

To add new sources for a particular language, edit the update map which
corresponds to that language to include URLs where those instances are
located. Each instance's individual JSON dictionary is associated with an
account either on JVS or GH; if you do not have a JVS account then you may use
your GH account. The accounts are purely to provide a modicum of namespacing.

### Removing mirrors

If a mirror is dead, old, malicious, or corrupted, then we can remove it. This
applies to the bootstrap mirrors which I maintain, too! Edit the update maps
which contain that mirror.
