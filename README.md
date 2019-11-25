# MicroDeliveryService

The map is not updated, and this example is not complete. The end result is an example of a mini microservice example.

## Layout

Frontend will send request to data access (Flask API). Data Access will send a request to job manager to collect all the information from each service and return the requested information back to data access to deliver to the client.

RabbitMQ is the messaging service queue that directs the communication between the services.


Map needs to be update with image collector, two more services will be added to speak to job manager.


![Environment](https://github.com/teaglebuilt/MicroDeliveryService/blob/master/Environ.png)



Create Network

```
docker network create rabbitmq-cluster

```

Launch Services

```

docker-compose up -d 

```

Test

```
chmod +x ./check_services

./check_services

```