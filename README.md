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
