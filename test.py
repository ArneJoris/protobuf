import locks_pb2 as lockMessage
import uuid
from datetime import datetime, timedelta

TIMEFMT = '%Y-%m-%d %H:%M:%S %z'

John = uuid.uuid4().hex
Paul = uuid.uuid4().hex
Ringo = uuid.uuid4().hex

l = lockMessage.Commands()

for g in (John, Paul, Ringo):
    c = l.commands.add() 
    c.type = lockMessage.Command.CommandType.DELETE
    c.guid = g
    c.start = int(datetime.strptime('2021-10-01 08:00:00 +0700', TIMEFMT).timestamp() / 60)

    for d in range(1,6):
        c = l.commands.add()
        c.type = lockMessage.Command.CommandType.ADD
        c.guid = g
        c.start = int((datetime.strptime('2021-10-01 08:00:00 +0700', TIMEFMT) + timedelta(days=d)).timestamp() / 60)
        c.stop = int((datetime.strptime('2021-10-01 12:00:00 +0700', TIMEFMT) + timedelta(days=d)).timestamp() / 60)

        c = l.commands.add()
        c.type = lockMessage.Command.CommandType.ADD
        c.guid = g
        c.start = int((datetime.strptime('2021-10-01 13:00:00 +0700', TIMEFMT) + timedelta(days=d)).timestamp() / 60)
        c.stop = int((datetime.strptime('2021-10-01 17:00:00 +0700', TIMEFMT) + timedelta(days=d)).timestamp() / 60)

print("%d commands:" %(len(l.commands)))
for c in l.commands:
    print(c)

print("Serialized into %d bytes." %(len(l.SerializeToString())))
print(l.SerializeToString())
