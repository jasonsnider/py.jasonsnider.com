# py.jasonsnider.com
My personal website written in Python.


## Install

> My dev environment is Ubuntu 18.04, Apache 2.4.29, and Python 3.6.8.
> These instructions should be compatible on most Debian based distributions 
> running Apache >= 2.4 and Python >= 3.6.

Clone the project into */var/www*
```sh
cd /var/www
git clone git@github.com:jasonsnider/py.jasonsnider.com.git
```

Enable cgi modules
```sh
sudo a2enmod mpm_prefork cgi
sudo systemctl restart apache2
```

Add a virtual host file
*/etc/apache2/sites-available/py.conf*
```apache
<VirtualHost 127.0.0.2:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/py.jasonsnider.com/webroot
    <Directory /var/www/py.jasonsnider.com/webroot>
        Options +ExecCGI
        DirectoryIndex index.py
        AllowOverride All
    </Directory>
    AddHandler cgi-script .py
</VirtualHost>
```

Enable the virtual host
```sh
sudo a2ensite py
sudo systemctl restart apache2
```

Set defaults to Python3


Use Python3
```sh
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 0
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --config python
```

Choose either option 0 or 2 to use Python3 if one of those options are not
already selected.

```sh
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path              Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3   1         auto mode
  1            /usr/bin/python2   0         manual mode
  2            /usr/bin/python3   1         manual mode

Press <enter> to keep the current choice[*], or type selection number: 0
```

Install PIP - I'm having some issue with PIP. Try installing both version.
When running PIP results in an error regarding *cannot import name main* 
Reinstalling seems to fix it.

```sh
sudo apt install python-pip
sudo apt install python3-pip

# If your having issues try to reinstall
sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall
```

## Dependencies

```sh
sudo pip3 install pymysql
```


Navigate to [http://127.0.0.2](http://127.0.0.2)
