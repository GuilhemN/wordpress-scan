# Configure the Wordpress website
docker-compose run --rm wpcli core install \
    --url="http://localhost:8080" \
    --title="Vulnerable Wordpress" \
    --admin_user=guilhem \
    --admin_email="guilhem@gniot.fr"

# Install a vulnerable plugin (cf https://wpscan.com/plugin/bbpress)
docker-compose run --rm wpcli plugin install bbpress --version=2.6.0 --activate
