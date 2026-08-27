timsaxu is a prototype distributed dictionary for Lojban. A timsaxu instance
is a directory of JSON files. An update map is a JSON file mapping usernames
to lists of URLs. Three scripts are included:

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
jvs-convert.py or search.py, or by running update.py and examining the
downloaded dictionaries, or by considering the following example:

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
