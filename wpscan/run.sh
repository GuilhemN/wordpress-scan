TOKEN=

docker run --add-host=host.docker.internal:host-gateway -it --rm wpscanteam/wpscan \
    --url http://host.docker.internal:8080 \
    --api-token $TOKEN \
    -e vp,vt \
    --plugins-detection mixed \
    --themes-detection mixed \
    -f json \
> wpscan_result.json