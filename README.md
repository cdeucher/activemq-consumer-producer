

# Instalar ActiveMQ
    docker pull rmohr/activemq
    docker run  -itd --name activemq -p 61616:61616 -p 61613:61613 -p 8161:8161 rmohr/activemq

# Gerar mensagens
    docker run -it --link activemq --rm --name running-python -v "$PWD":/usr/src/myapp -w /usr/src/myapp ryanface/python-stomp:0.1 python producer.py

# Ler as mensagens

    java -cp app.jar com.activemq.consumer.Consumer "bla.bla" 1 "tcp://localhost:61616"


