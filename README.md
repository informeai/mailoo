# Mailoo
![OpenSource](https://img.shields.io/static/v1?label=GitHub&message=Opensource&color=blue&logo=github&logoColor=violet)
![BuildPassing](https://img.shields.io/static/v1?label=build&message=passing&color=brightgreen)
![PythonVersion](https://img.shields.io/static/v1?label=python&message=>=3.6&color=brightgreen&logo=python&logoColor=white)
[![Pypi](https://img.shields.io/static/v1?label=Pypi&logo=pypi&logoColor=white&message=v1.0.2&color=9f55ff)](https://pypi.org/project/mailoo/)

[![HitCount](https://hits.dwyl.com/informeai/mailoo.svg)](http://hits.dwyl.com/informeai/mailoo)


Python module that facilitates sending Emails using providers
`SMTP`. 

With functions for loading content from files, writing to
`html` in-line. 

It provides easily and with few lines the creation and sending of emails.

For lovers of `Email-Marketing` or Enthusiasts in general.

Support for Python Version 3

### Installation:
```
 $ pip install mailoo
```

### Use
```
>> import mailoo

>> email = mailoo.Mail(email_user, key_pass)   # email_user -> email the user.

                                               # key_pass -> Key of application
                                               -> GMAIL, or email password us
                                               other cases

>> email.send(subject,msg,email)               # Envio do email...
```
### Other Uses
```
============
Emails.txt:
|-- email1
|-- email2
|-- ...
============

>> email.send(subject,msg, Emails.txt)

######### OR #########
                                            
>> email.send(subject,file.html, arquivo.txt)  # html file for various emails.

                                               # file.html -> html file to be
                                               sent in place of a message
                                               common.

```

## Características
* Sending several emails with simplicity.

* Automatic choice of sending via SSL / TLS.

* Write simple messages or enter html text.

* Reading and sending html / txt file content.

### Obs:
```
The module uses the outgoing servers of the user's email providers.

EX: GMAIL, OUTLOOK, HOTMAIL,YAHOO.

So beware of the Limits set by these providers, as the
they establish shipping control policies. In general they have
MAXIMUM SHIPPING limits of 300 emails / day.
Observing and Respecting the established limits, use the module at will ...
```
## Contact:
@informeai

[Facebook](https://www.facebook.com/informeai/)

[Instagram](https://www.instagram.com/informeaioficial/)

[Twitter Dev](https://twitter.com/WellingtonGade4)