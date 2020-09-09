# HADOOP_Assignments
#### How to compile and run any task:
* Add all the jars in the lib file of the assignment x, to /home/hadoop-3.2.0/share/hadoop/mapreduce/lib
* Run the following command from **/Assigment1/**
```shell
$mkdir task1
$javac -cp ".:./lib/*" -d task1 task1.java                                            //".;./lib/*" for Windows
$jar -cvf task1.jar -C task1/ .
$Hadoop jar task1.jar hadoop.task1 <input directory> <output directory> <inputString>
```
