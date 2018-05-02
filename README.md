# network-tools

Given an IPv4 network address and associated CIDR suffix, this program will display the following:

* network block size
* netmask (dotted decimal notation with dotted binary as an option)
* network address (dotted decimal notation with dotted binary as an option)
* first host address (dotted decimal notation with dotted binary as an option)
* last host address (dotted decimal notation with dotted binary as an option)
* broadcast address (dotted decimal notation with dotted binary as an option)
* next network address (dotted decimal notation with dotted binary as an option)

Optionally, the individual host address can be displayed

## Examples
netcheck.py 150.75.0.0/28

* Output:
* block size      16
* netmask         255.255.255.240
* network         150.75.0.0
* first host      150.75.0.1
* last host       150.75.0.14
* broadcast       150.75.0.15
* next network    150.75.0.16

netcheck.py 150.75.0.0/28 --hosts

Output:
block size      16
netmask         255.255.255.240
network         150.75.0.0
                150.75.0.1
                150.75.0.2
                150.75.0.3
                150.75.0.4
                150.75.0.5
                150.75.0.6
                150.75.0.7
                150.75.0.8
                150.75.0.9
                150.75.0.10
                150.75.0.11
                150.75.0.12
                150.75.0.13
                150.75.0.14
broadcast       150.75.0.15
next network    150.75.0.16

netcheck.py 150.75.0.0/28 --bits

Output:
block size      16
netmask         255.255.255.240         11111111.11111111.11111111.11110000
network         150.75.0.0              10010110.01001011.00000000.00000000
first host      150.75.0.1
last host       150.75.0.14
broadcast       150.75.0.15             10010110.01001011.00000000.00001111
next network    150.75.0.16




## Getting Started

TODO:

### Prerequisites

TODO:

```
TODO:
```

### Installing

TODO:

```
TODO:
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

TODO:

TODO:

## Contributing

TODO:

## Versioning

TODO: 

## Authors

Stuart Willcocks

TODO:

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

TODO:
