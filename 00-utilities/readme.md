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

## Rabbitmq

Install rabbitmq by docker:

```
docker pull rabbitmq
```