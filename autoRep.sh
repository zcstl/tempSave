workDir=/home/test/
destFile=./autoRep.sh

containID=`docker ps |  sed -n "2, 1p"  | awk '{print $1}'`
docker cp $destFile $containID:$workDir
docker exec $containID chmod 777 $workDir
docker exec $containID chown root:root /home/test/autoRep.sh

