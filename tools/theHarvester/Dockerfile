FROM python:3.11-slim-bookworm
LABEL maintainer="@jay_townsend1 & @NotoriousRebel1"
RUN apt update && apt install -y pipx git wget unzip && rm -rf /var/lib/apt/lists/*
RUN wget https://github.com/laramies/theHarvester/archive/refs/tags/4.6.0.zip 
RUN unzip 4.6.0.zip
# temporary hotfix bug
RUN sed -i 's/dns_brute=dns_brute,/dns_brute=dns_brute,dns_resolve="",/g' ./theHarvester-4.6.0/theHarvester/lib/api/api.py
RUN pipx install ./theHarvester-4.6.0
RUN pipx ensurepath
RUN mkdir -p /root/.local/share/theHarvester/static/
ENTRYPOINT ["/root/.local/bin/restfulHarvest", "-H", "0.0.0.0", "-p", "80"]
EXPOSE 80
