# iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf

# 🚀 IotCloud is a platform where you can automate your house easily and in an inexpensive way. 🚀

https://github.com/coding-to-music/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf

From / By Cesar Sanz https://github.com/csanz91

https://github.com/csanz91/IotCloud

## Environment variables:

```java

```

## GitHub

```java
git init
git add .
git remote remove origin
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:coding-to-music/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf.git
git push -u origin main
```

# IotCloud

IotCloud is a platform where you can automate your house easily and in an inexpensive way.

## Secrets

```
secrets:
  modules_secrets:
      file: ./python-modules/secrets
```

## How to run:

```
docker-compose up
```

# How to stop

```
docker-compose down
```

Output:

```java
WARNING: Service "backup-manager" uses an undefined secret file "/mnt/volume_nyc1_01/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf/backup-manager/secrets/gdrive_backup_folder", the following file should be created "/mnt/volume_nyc1_01/iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf/backup-manager/secrets/gdrive_backup_folder"
Stopping nginx-proxy-letsencrypt                                               ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_telegraf_1  ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mongodb_1   ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mosquitto_1 ... done
Stopping iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_influxdb_1  ... done
Stopping monitoring                                                            ... done
Stopping ota                                                                   ... done
Stopping nginx-proxy                                                           ... done
Removing nginx-proxy-letsencrypt                                               ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_telegraf_1  ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mongodb_1   ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_mosquitto_1 ... done
Removing iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_influxdb_1  ... done
Removing monitoring                                                            ... done
Removing ota                                                                   ... done
Removing nginx-proxy                                                           ... done
Removing network iot-cloud-nginx-mongo-api-influx-weather-grafana-telegraf_default
```

### Errors

```java
docker compose up
```

```java
[+] Building 7.1s (30/98)                                                                                                                             docker:default
 => [grafana-datasource internal] load build definition from Dockerfile                                                                                         0.1s
 => => transferring dockerfile: 884B                                                                                                                            0.0s
 => [monitoring internal] load build definition from Dockerfile                                                                                                 0.0s
 => => transferring dockerfile: 447B                                                                                                                            0.0s
 => [modules2 internal] load build definition from Dockerfile                                                                                                   0.0s
 => => transferring dockerfile: 339B                                                                                                                            0.0s
 => [weather internal] load build definition from Dockerfile                                                                                                    0.0s
 => => transferring dockerfile: 546B                                                                                                                            0.0s
 => [influx_mqtt_gateway internal] load build definition from Dockerfile                                                                                        0.0s
 => => transferring dockerfile: 340B                                                                                                                            0.0s
 => [backup-manager internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 1.24kB                                                                                                                          0.0s
 => [api internal] load build definition from Dockerfile                                                                                                        0.0s
 => => transferring dockerfile: 514B                                                                                                                            0.0s
 => [grafana-datasource internal] load .dockerignore                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [home internal] load build definition from Dockerfile                                                                                                       0.0s
 => => transferring dockerfile: 960B                                                                                                                            0.0s
 => [monitoring internal] load .dockerignore                                                                                                                    0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [modules2 internal] load .dockerignore                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [weather internal] load .dockerignore                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [influx_mqtt_gateway internal] load .dockerignore                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [backup-manager internal] load .dockerignore                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [api internal] load .dockerignore                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [home internal] load .dockerignore                                                                                                                          0.0s
 => => transferring context: 2B                                                                                                                                 0.0s
 => [grafana-datasource internal] load metadata for docker.io/library/golang:1.13-alpine                                                                        0.9s
 => [monitoring internal] load metadata for docker.io/library/python:3.10                                                                                       0.9s
 => [backup-manager internal] load metadata for docker.io/library/alpine:latest                                                                                 0.7s
 => [backup-manager  1/15] FROM docker.io/library/alpine@sha256:51b67269f354137895d43f3b3d810bfacd3945438e94dc5ac55fdac340352f48                                0.1s
 => => resolve docker.io/library/alpine@sha256:51b67269f354137895d43f3b3d810bfacd3945438e94dc5ac55fdac340352f48                                                 0.0s
 => => sha256:51b67269f354137895d43f3b3d810bfacd3945438e94dc5ac55fdac340352f48 1.64kB / 1.64kB                                                                  0.0s
 => => sha256:13b7e62e8df80264dbb747995705a986aa530415763a6c58f84a3ca8af9a5bcd 528B / 528B                                                                      0.0s
 => => sha256:f8c20f8bbcb684055b4fea470fdd169c86e87786940b3262335b12ec3adef418 1.47kB / 1.47kB                                                                  0.0s
 => [backup-manager internal] load build context                                                                                                                0.0s
 => => transferring context: 2.41kB                                                                                                                             0.0s
 => CANCELED [grafana-datasource builder 1/8] FROM docker.io/library/golang:1.13-alpine@sha256:e74b83b94d499cb34c7edf55fbdff9d3cfabd238a35f9cb1b59d0e74f50b1dd  5.8s
 => => resolve docker.io/library/golang:1.13-alpine@sha256:e74b83b94d499cb34c7edf55fbdff9d3cfabd238a35f9cb1b59d0e74f50b1ddd                                     0.0s
 => => sha256:5863598a981a037fbf078324d356cb3e7deade1c8ddb67550a1e9809274a8a11 3.83kB / 3.83kB                                                                  0.0s
 => => sha256:df20fa9351a15782c64e6dddb2d4a6f50bf6d3688060a34c4014b0d9a752eb4c 2.80MB / 2.80MB                                                                  0.3s
 => => sha256:ed8968b2872e472e21554ca58b35a02277634f3e501cc04ab7b0d0963f60f54d 282.60kB / 282.60kB                                                              0.3s
 => => sha256:a92cc7c5fd73817407fa0e4de5e1fb262a9c0f34c35c7450a2d01a7cef79c62f 155B / 155B                                                                      0.1s
 => => sha256:e74b83b94d499cb34c7edf55fbdff9d3cfabd238a35f9cb1b59d0e74f50b1ddd 1.65kB / 1.65kB                                                                  0.0s
 => => sha256:8cc699270cfeed0864420e5c650aa9c1b51ed5b23cf927ab4c5eea47f6c0c1a8 1.36kB / 1.36kB                                                                  0.0s
 => => sha256:dd0b68742591b9b4e6f97f414760ada9c0b7554006477d31532b85e6ad0f3f6b 18.87MB / 127.34MB                                                               5.7s
 => => sha256:fb4ae7ba11024d2acfa3a21422bafbb3a2e4497a1cea750402d5a444c6251d12 126B / 126B                                                                      0.4s
 => => extracting sha256:df20fa9351a15782c64e6dddb2d4a6f50bf6d3688060a34c4014b0d9a752eb4c                                                                       0.9s
 => => extracting sha256:ed8968b2872e472e21554ca58b35a02277634f3e501cc04ab7b0d0963f60f54d                                                                       0.1s
 => => extracting sha256:a92cc7c5fd73817407fa0e4de5e1fb262a9c0f34c35c7450a2d01a7cef79c62f                                                                       0.0s
 => [home internal] load build context                                                                                                                          0.0s
 => => transferring context: 54.44kB                                                                                                                            0.0s
 => [grafana-datasource internal] load build context                                                                                                            0.0s
 => => transferring context: 39.57kB                                                                                                                            0.0s
 => ERROR [backup-manager  2/15] RUN set -ex &&     apk update &&     apk upgrade &&     apk add --no-cache     influxdb     sqlite     mongodb-tools &&     r  5.6s
 => CANCELED [api  1/10] FROM docker.io/library/python:3.10@sha256:77335ff30c2b89e66ae3b70589ca20a3f3cf1c815710438d14d61661b37d1a4a                             5.7s
 => => resolve docker.io/library/python:3.10@sha256:77335ff30c2b89e66ae3b70589ca20a3f3cf1c815710438d14d61661b37d1a4a                                            0.0s
 => => sha256:77335ff30c2b89e66ae3b70589ca20a3f3cf1c815710438d14d61661b37d1a4a 1.65kB / 1.65kB                                                                  0.0s
 => => sha256:0a2e6600fb65626cb06681b3d289b59163063e76b2bfe373cceb33fc01d148d8 2.01kB / 2.01kB                                                                  0.0s
 => => sha256:748d669298acc9605821e625330330abe9475e19863a06fa0a78f6170b37b104 7.48kB / 7.48kB                                                                  0.0s
 => => sha256:d3a767d1d12e57724b9f254794e359f3b04d4d5ad966006e5b5cda78cc382762 49.28MB / 64.13MB                                                                5.7s
 => => sha256:711be5dc50448ab08ccab0b44d65962f36574d341749ab30651b78ec0d4bfd1c 178.26MB / 211.07MB                                                              5.7s
 => [api internal] load build context                                                                                                                           0.2s
 => => transferring context: 235.70kB                                                                                                                           0.1s
 => [influx_mqtt_gateway internal] load build context                                                                                                           0.0s
 => => transferring context: 47.00kB                                                                                                                            0.0s
 => [weather internal] load build context                                                                                                                       0.2s
 => => transferring context: 2.75MB                                                                                                                             0.1s
 => [monitoring internal] load build context                                                                                                                    0.1s
 => => transferring context: 9.53kB                                                                                                                             0.0s
 => [modules2 internal] load build context                                                                                                                      0.1s
 => => transferring context: 59.04kB                                                                                                                            0.0s
------
 > [backup-manager  2/15] RUN set -ex &&     apk update &&     apk upgrade &&     apk add --no-cache     influxdb     sqlite     mongodb-tools &&     rm -rf /usr/src/* &&     rm -rf /root/.cache /tmp/* /var/cache/apk/*:
1.363 + apk update
1.425 fetch https://dl-cdn.alpinelinux.org/alpine/v3.19/main/x86_64/APKINDEX.tar.gz
2.251 fetch https://dl-cdn.alpinelinux.org/alpine/v3.19/community/x86_64/APKINDEX.tar.gz
3.759 v3.19.0-19-ga0ddaee500e [https://dl-cdn.alpinelinux.org/alpine/v3.19/main]
3.759 v3.19.0-21-g50a95c55db3 [https://dl-cdn.alpinelinux.org/alpine/v3.19/community]
3.759 OK: 22983 distinct packages available
3.858 + apk upgrade
4.363 OK: 7 MiB in 15 packages
4.492 + apk add --no-cache influxdb sqlite mongodb-tools
4.497 fetch https://dl-cdn.alpinelinux.org/alpine/v3.19/main/x86_64/APKINDEX.tar.gz
4.699 fetch https://dl-cdn.alpinelinux.org/alpine/v3.19/community/x86_64/APKINDEX.tar.gz
5.236 ERROR: unable to select packages:
5.236   influxdb (no such package):
5.236     required by: world[influxdb]
------
failed to solve: executor failed running [/bin/sh -c set -ex &&     apk update &&     apk upgrade &&     apk add --no-cache     influxdb     sqlite     mongodb-tools &&     rm -rf /usr/src/* &&     rm -rf /root/.cache /tmp/* /var/cache/apk/*]: exit code: 1
```

## Remove Docker

```java
dpkg -l | grep -i docker

sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli docker-compose-plugin docker-buildx-plugin docker-ce-rootless-extras python3-docker python3-dockerpty

sudo rm -rf /var/lib/docker /etc/docker

sudo groupdel docker

sudo find / -name "_docker_"

sudo rm /usr/local/bin/docker-compose

sudo rm /snap/bin/docker-compose
```

## Install Docker

```java
sudo apt update

sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt update

sudo apt install docker-ce docker-ce-cli containerd.io

sudo docker run hello-world
```

## Fix permissions problems when running `docker ps`

```
sudo usermod -aG docker $USER

groups $USER

sudo chown root:docker /var/run/docker.sock

ls -l /var/run/docker.sock

sudo systemctl reset-failed docker.service

sudo systemctl restart docker.service

sudo systemctl status docker.service

docker ps
```

## Install docker-compose

```java
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose rm --all && docker-compose pull && docker-compose build --no-cache && docker-compose up -d --force-recreate
```

## rebuild Snap cache

```java
sudo rm -rf /var/cache/snapd/

sudo apt-get install --reinstall snapd

sudo systemctl restart snapd.service
```
