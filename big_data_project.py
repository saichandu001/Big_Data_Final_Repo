import os
import random
import subprocess

k = random.randint(0, 100000000)

# Calling the first program
r = os.popen('hadoop jar /home/hdoop/hadoop-3.2.3/share/hadoop/tools/lib/hadoop-streaming-3.2.3.jar -file /home/hdoop/mapper.py -mapper mapper.py -file /home/hdoop/reducer.py -reducer reducer.py -input /enroll.txt -output /home/hdoop/output'+str(k)).read()
os.popen('hdfs dfs -copyToLocal /home/hdoop/output'+str(k))
print(k)

k = random.randint(0, 100000000)
# Calling the second program
r = os.popen('hadoop jar /home/hdoop/hadoop-3.2.3/share/hadoop/tools/lib/hadoop-streaming-3.2.3.jar -file /home/hdoop/mapper1.py -mapper mapper1.py -file /home/hdoop/reducer1.py -reducer reducer1.py -input /campstaar.csv -output /home/hdoop/output'+str(k)).read()
os.popen('hdfs dfs -copyToLocal /home/hdoop/output'+str(k))
# print(k)

os.rmdir('project_output')
os.mkdir('project_output')