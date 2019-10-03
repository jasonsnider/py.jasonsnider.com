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
    DocumentRoot /var/www/py.jasonsnider.com
    <Directory /var/www/py.jasonsnider.com>
        Options +ExecCGI
        DirectoryIndex index.py
    </Directory>
    AddHandler cgi-script .py
</VirtualHost>
```

Enable the virtual host
```sh
sudo a2ensite py
sudo systemctl restart apache2
```

Set the environment to Python3
```sh
alias python=python3
```

Navigate to [http://127.0.0.2](http://127.0.0.2)
