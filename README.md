# AKIOBOT - Family Senior Connection 
Home personnal robot for senior people to digitally and easily communicate with family and friends


![](https://img.shields.io/badge/python-v3.8.10-blue) 
![](https://img.shields.io/badge/Release%20@dev-v0.1-yellow) 
![](https://img.shields.io/badge/Release%20@test-v0.0-orange) 
![](https://img.shields.io/badge/Release%20@prod-v0.0-brightgreen) 

[![Latest Stable Version](https://img.shields.io/badge/license-CC%20BY%20NC-blue)](https://github.com/w0dd3n/akiobot/blob/main/LICENSE)

## Before you begin
* You need an [IBM Cloud][ibm-cloud-onboarding] account. We now only support `python 3.5` and above

## Installation
To install, use `pip` or `easy_install`:

```bash
pip install --upgrade akiobot
```

or

```bash
easy_install --upgrade akiobot
```

## Python version

Tested on Python 3.5, 3.6, and 3.7.

## Questions

If you have issues with the APIs or have a question about the Akiobot , see [Stack Overflow](https://stackoverflow.com/questions/tagged/akiobot+python).

## Changes for v1.0
Version 1.0 focuses on the move to programmatically-generated code for many of the services. See the [changelog](https://github.com/watson-developer-cloud/python-sdk/wiki/Changelog) for the details.


## Logging

### Enable logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

This would show output of the form:
```
DEBUG:akiobot:<timestamp>:Starting new HTTPS connection: iam.cloud.ibm.com:443
DEBUG:akiobot:<timestamp>:https://iam.cloud.ibm.com:443 "POST /identity/token HTTP/1.1" 200 1809
```

## License

This library is licensed under the [Common Creative BY NC license][https://creativecommons.org/licenses/by-nc/4.0/].


