# Internal scripts to import EAP data

[EAP](https://eap.bl.uk/) is one of our partners, they provide us with an [OAI-PMH](https://en.wikipedia.org/wiki/Open_Archives_Initiative_Protocol_for_Metadata_Harvesting) endpoint. The scripts in this repository get the records from some collections in the endpoint and transform them into a csv file.

The OAI-PMH endpoint is not publicly accessible, a request must be made to them, and they can open the endpoint to a specific IP address.

## Dependencies

```
sudo pip3 install Sickle
```

## Running

```
python3 getallsickle.py > sickle.xml
python3 csvify.py
```

The first step takes about 10-15mn.

## TODO

There is a bug that prevents the final `</records>` to be written.