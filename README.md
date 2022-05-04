# Wordpress Configuration

Wordpress version: 5.2.4
Plugins:

* bbPress (version 2.6.0)

# Wordpress setup

The Wordpress is setup using Docker Compose and WP-cli.

The first step is to start the docker containers:
```
cd wordpress
docker-compose up -d
```

This will expose a Wordpress server at `http://localhost:8080`.

You then need to wait until the database is correctly initialized before continuing (you can check whether http://localhost:8080 is accessible).

The next step is to configure the website and plugins by running (the user must be able to run Docker, you may want to use sudo):
```
./setup.sh
```
in the folder `wordpress`.

It will set up the admin email, username and install bbPress.

# WPScan

For simplicity, we run WPScan locally in a Docker image.

To launch it, you need to input **your WPScan API Token** in the file `wpscan/run.sh` under the variable `TOKEN` (otherwise plugins detection is not accurate).

Then, to analyze the Wordpress website set up before on `http://localhost:8080`, run the following commands (the user must be able to run Docker, you may want to use sudo):
```
cd wpscan
./run.sh
python3 ./process_wpscan.py wpscan_result.json
```

This script produces only checks (and a 0 exit status) when no vulnerability is detected, otherwise
it produces cross marks (and a 1 exit status).

# Automated Scanning

Automated Scanning is implemented as a Github Action (see https://github.com/GuilhemN/wordpress-scan/actions/workflows/scan-wordpress.yaml).

For simplicity, it uses the third party Github Action [WTFender/wpscan-action](https://github.com/WTFender/wpscan-action) to generate the WPScan analysis report.

Then, it calls the Python script from previous section to analyze the report.

Here, we trigger it manually, but it could easily be executed on a regular basis (see https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule).