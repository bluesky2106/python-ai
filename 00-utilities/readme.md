# Installation

## MongoDB

Install mongodb by docker:

```
docker pull mongo
```

Then, run mongodb by following command:

```
docker container stop mongo
docker run --name mongo -p 27017:27017 -v $HOME/mongo:/data/db --rm -d mongo:latest
```

The first command will stop container named mongo.

The second command will start a new container named mongo
- `-p 27017:27017` : map port 27017 (host) to 27017 (docker).
- `-v $HOME/mongo:/data/db` : map volumnn $HOME/mongo (host) to /data/db (docker)
- `--rm` : delete instance when stop
- `-d` : run in detach mode (background). Nếu thiết đặt cờ này bạn sẽ không nhìn thấy output nào của câu lệnh cả. Nếu bạn thoát ra khỏi ssh session, máy chủ vẫn tiếp tục chạy. Trong trường hợp bạn muốn theo dõi output của câu lệnh hoặc các truy vấn, thay cờ `-d` bằng cờ `-it`, sau đó dùng tổ hợp phí `ctrl-p` `ctrl-q` để chuyển sang background mode nếu muốn. Câu lệnh full trong trường hợp này

For more information, please read following article:

https://transang.me/cach-thiet-lap-may-chu-mongo-thong-qua-docker/

## Robo 3T

Download and install Robo 3T:

https://robomongo.org/download

Then, run this command in order to allow opening Robo 3T in macos.

```
sudo xattr -r -d com.apple.quarantine /Applications/Some.app
```

## Scrapy

Run following command to install Scrapy

```
pip3 install Scrapy
```

For more information, please following below link:

https://doc.scrapy.org/en/latest/intro/install.html

## PyMongo

Install PyMongo with pip:

```
pip3 install pymongo
```

## postgres

```
docker pull postgres
```

```
docker run -d -e POSTGRES_USER=dantrisoft -e POSTGRES_PASSWORD=dantrisoft -e POSTGRES_DB=dantrisoft -v $HOME/postgres:/var/lib/postgresql/data  -p 5432:5432  --restart=always postgres
```

```
docker exec -ti NAME_OF_CONTAINER psql -U YOUR_POSTGRES_USERNAME
```


```
docker run -d \
    --name some-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /custom/mount:/var/lib/postgresql/data \
    postgres
```

## pgadmin

https://www.pgadmin.org/download/pgadmin-4-macos/

## Rabbitmq

Install rabbitmq by docker:

```
docker pull rabbitmq
```

## Useful links

- https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-to-classify-photos-of-dogs-and-cats/
- https://aicurious.io/posts/2019-09-23-cac-ham-kich-hoat-activation-function-trong-neural-networks/
- https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/