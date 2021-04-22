import stomp, sys

conn = stomp.Connection([("activemq",61613)])
conn.connect(wait=True)
for i in range(0, 50):
   conn.send(body=' '.join(sys.argv[1:]), destination='/queue/bla.bla')
conn.disconnect()

print("Mensagens enviadas")