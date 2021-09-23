# Scrapyd (with authentication & support of Asyncio Reactor based Spiders)

Scrapyd is an application for deploying and running Scrapy spiders. It enables you to deploy (upload) your projects and control their spiders using a JSON API.

Scrapyd doesn't include any provision for password protecting itself. This container packages Scrapyd with an nginx proxy in front of it providing basic HTTP authentication. The username and password are configured through environment variables.

For more about Scrapyd, see the [Scrapyd documentation](http://scrapyd.readthedocs.org/en/latest/).


# Using with docker-compose

Run the following commands:

```
$ docker-compose build
$ docker-compose up
```

The following printout to console should be seen after `docker-compose up`:
```shell
docker-compose up
Creating network "scrapyd-authenticated_default" with the default driver
Creating scrapyd-authenticated_scrapyd_1 ... done
Attaching to scrapyd-authenticated_scrapyd_1
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: Switching all chaperone logging to /dev/log
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: chaperone version 0.3.9, ready.
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: service nginx.service enabled, queueing start request
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: nginx.service attempting start '/usr/sbin/service nginx start'...
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: service password.service enabled, queueing start request
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: password.service attempting start '/usr/bin/htpasswd -b -c /etc/nginx/htpasswd debug debug'...
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: service scrapyd.service enabled, queueing start request
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: service password.service enabled, queueing start request
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: service upload.service enabled, queueing start request
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: service scrapyd.service enabled, queueing start request
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d password[11]: Adding password for user debug
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: REAP pid=11,status=0
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: REAP pid=0,status=0
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: password.service exit status for pid=11 is '<ProcStatus exit_status=0>'
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: password.service successfully started
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: password.service notified waiters upon completion
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: service scrapyd.service prerequisites satisfied
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: scrapyd.service attempting start '/usr/local/bin/scrapyd'...
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d nginx[8]: Starting nginx: nginx.
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: REAP pid=8,status=0
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: REAP pid=0,status=0
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: nginx.service exit status for pid=8 is '<ProcStatus exit_status=0>'
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: nginx.service successfully started
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: nginx.service notified waiters upon completion
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d chaperone[1]: nginx.service exit status for pid=8 is '<ProcStatus exit_status=0>'
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [-] Loading /usr/local/lib/python3.7/site-packages/scrapyd/txapp.py...
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [-] Scrapyd web console available at http://0.0.0.0:6801/
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [-] Loaded.
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [twisted.scripts._twistd_unix.UnixAppLogger#info] twistd 21.7.0 (/usr/local/bin/python 3.7.12) starting up.
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [twisted.scripts._twistd_unix.UnixAppLogger#info] reactor class: twisted.internet.epollreactor.EPollReactor.
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [-] Site starting on 6801
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [twisted.web.server.Site#info] Starting factory <twisted.web.server.Site object at 0x7ff89d1a1050>
scrapyd_1  | Sep 23 17:02:55 2a6b86ee639d scrapyd[17]: 2021-09-23T17:02:55+0000 [Launcher] Scrapyd 1.2.1 started: max_proc=64, runner='custom_runner.async_runner'
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: scrapyd.service successfully started
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: scrapyd.service notified waiters upon completion
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: service upload.service prerequisites satisfied
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: upload.service attempting start '/usr/bin/curl http://localhost:6800/addversion.json --location --request POST --header Authorization: Basic ZGVidWc6ZGVidWc= -F project=default
 -F version=1.0 -F egg=@default-1.0-py3.7.egg'...
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d upload[39]:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d upload[39]:                                  Dload  Upload   Total   Spent    Left  Speed
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d scrapyd[17]: 2021-09-23T17:03:05+0000 [twisted.python.log#info] "127.0.0.1" - - [23/Sep/2021:17:03:04 +0000] "POST /addversion.json HTTP/1.0" 200 100 "-" "curl/7.74.0"
100 10828  100   100  100 10728    217  23321 --:--:-- --:--:-- --:--:-- 23539
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d upload[39]: {"node_name": "2a6b86ee639d", "status": "ok", "project": "default", "version": "1.0", "spiders": 1}
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: REAP pid=39,status=0
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: REAP pid=0,status=0
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: upload.service exit status for pid=39 is '<ProcStatus exit_status=0>'
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: upload.service successfully started
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: upload.service notified waiters upon completion
scrapyd_1  | Sep 23 17:03:05 2a6b86ee639d chaperone[1]: REAP pid=0,status=0
```

To run the `async example spider`, run the following command on another terminal or on Postman: 
```shell
curl --location --request POST 'http://localhost:6801/schedule.json' --header 'Authorization: Basic ZGVidWc6ZGVidWc=' --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'project=default' --data-urlencode 'spider=example'
```

Observe the new job schduled at `http://localhost:6801/jobs`.


# How to use this image

## Start a Scrapyd server

```console
$ docker run -d -e USERNAME=my_username -e PASSWORD=hunter123 cdrx/scrapyd-authenticated
```

You can then use the [Scrapyd client](https://github.com/scrapy/scrapyd-client) to easily deploy the scraper from your machine to the running container.

## How to configure Scrapy to use HTTP basic authentication

Support for HTTP authentication is built into scrapyd client. Add the `username` and `password` field to your `scrapy.cfg` file and then deploy as you normally would.

```
[deploy]
url = http://scrapyd:6800/
username = my_username
password = hunter123
```

## Installing Python packages that your scraper depends on

If your scraper depends on some 3rd party Python packages (Redis, MySQL drivers, etc) you can install them when the container launches by adding the PACKAGES environment variable.

```console
$ docker run -d -e USERNAME=my_username -e PASSWORD=hunter123 -e PACKAGES=requests,simplejson cdrx/scrapyd-authenticated
```

This will make the container a bit slow to boot, so if your starting / stopping the container regularly you would be better off forking this repository and adding the packages to `requirements.txt`.

# Supported environment variables

| Variable | Required | Example             | Description                                                                |
|----------------------|----------|---------------------|----------------------------------------------------------------------------|
| `USERNAME`             | Yes      | my_user             | The username for authentication with the Scrapy server                     |
| `PASSWORD`             | Yes      | hunter123           | The password for authentication with the Scrapy server                     |
| `PACKAGES`             | No       | simplejson,requests | Comma separated list of Python packages to install before starting scrapyd |

# Volumes

To persist data between launches, you can mount the volume `/scrapyd` somewhere on your Docker host.

# Feedback

## Issues

If you have any problems with or questions about this image, please file an issue on the [GitHub repository](https://github.com/cdrx/scrapyd-authenticated/issues).

## Contributing

Pull requests welcome :-)
