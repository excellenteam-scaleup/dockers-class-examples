docker volume create mydata
docker run -it --name regular_volume_example -v mydata:/mnt busybox

# echo "data" > /mnt/file.txt
# docker stop regular_volume_example
# docker rm regular_volume_example
# docker run -it --name another_regular_volume_example -v mydata:/mnt busybox
# mkdir -p /tmp/bind_exmaple
# docker run -it --name host_folder_mount_example -v /tmp/bind_example:/mnt busybox
# show example of file creation


