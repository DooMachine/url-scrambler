# url-scrambler

Generate new scrambled domain names with provided domain name, difference limited with levenshtein distance and whois checking automated.<br>
Scramble dmaoin nmeas to prenevt hijacking, phishing wtih yuor domain name.

### Installing

Clone Repository

```
git clone https://github.com/DooMachine/url-scrambler.git
```
Install Requirements
```
cd url-scrambler
pip install -r requirements.txt
```

## Getting Started

To generate example.com scrambled urls with whois check
```
python scrambler.py --url example.com --output dnames.txt --distance 2 --checkdomains
```
Output:
```
example.com - 2019-08-13 04:00:00
examlpe.com - 2019-07-11 06:25:06
exapmle.com - 2018-12-23 19:26:59
exaplme.com - Avaliable
exalmpe.com - Avaliable
exalpme.com - Avaliable
exmaple.com - 2018-10-08 13:53:42
exmpale.com - Avaliable
exmplae.com - Avaliable
expamle.com - Avaliable
expmale.com - Avaliable
exlampe.com - Avaliable
exlmpae.com - Avaliable
eaxmple.com - 2019-06-20 14:32:59
eamxple.com - Avaliable
eampxle.com - Avaliable
eamplxe.com - Avaliable
emxaple.com - Avaliable
emaxple.com - Avaliable
epxamle.com - Avaliable
epamxle.com - Avaliable
elxampe.com - Avaliable
elampxe.com - Avaliable
```

## Contributing

PR's are welcome.


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Purpose

Education
