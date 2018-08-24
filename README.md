# Url-Scrambler

Generate new domain names with provided domain name, difference limited with levenshtein distance and whois checking automated.

### Installing

Clone Repository

```
https://github.com/DooMachine/url-scrambler.git
cd url-scrambler
pip install -r requirements.txt
```

## Getting Started

To generate example.com scrambled urls 
```
python scrambler --url example.com --output dnames.txt --distance 2
```

To generate example.com scrambled urls with whois check
```
python scrambler --url example.com --output dnames.txt --distance 2 --checkdomains
```


## Contributing

PR's are welcome.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
