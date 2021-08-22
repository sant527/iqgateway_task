# afer copying remote .git folder

# django development debugging

changes to be done

1) settings.py

a) this is to use docker in production and development

ADD the below code after DEBUG is defined like below

```
DEBUG=True

# we will check the environ variable if defined
try:
    import os
    if os.environ['DEBUG'] == "1":
        DEBUG = True
    else:
    	DEBUG = False
except:
    pass
```


2) at the end of settings.py add this

```
#install snoop for this
#https://github.com/alexmojaki/snoop
import snoop
import os

def path(event):
    return event.code.co_filename[-20:]

from cheap_repr import find_repr_function
import six
find_repr_function(object).maxparts =    100000000
find_repr_function(dict).maxparts = 100000000
find_repr_function(list).maxparts = 100000000
find_repr_function(six.text_type).maxparts = 500000000
find_repr_function(six.binary_type).maxparts = 100000000


snoop.install(enabled=DEBUG,columns=[path, "function"])

if DEBUG:

    PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))

    if os.path.exists(os.path.join(PROJECT_HOME, "external_config", "api_local_settings_fixed.py")):
        from .external_config.api_local_settings_fixed import *


    if os.path.exists(os.path.join(PROJECT_HOME, "external_config", "api_local_settings_var.py")):
        from .external_config.api_local_settings_var import *
```


## dont change anything in api_local_settings_fixed.py
1. shows the debugging of sql, requests, and logger.debug() 

## add midlerware and installed apps from settings.py into api_local_settings_var.py


## copy pretty_printing.py into the same folder as settings.py

and then use

```
from project.pretty_priting import dumps
```
and then 

```
logger.debug(dumps(obj))  
```

also we can use sorcery, it has dict_as()


so one can use

```
logger.debug(dumps(dict_as(var1,var2....)))

or

logger.debug(dumps(
					{
						**dict_as(var1,var2....),
						**{"var1":var1}
					}
				)
			)
```

also check snoopy pp and deeper



```
# install these packages

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "==3.1"
snoop = "*"

[dev-packages]
django-extensions = "*"
ipython = "*"
jupyter = "*"
django-request-logging = "*"
werkzeug = "*"

[requires]
python_version = "3.9"
```