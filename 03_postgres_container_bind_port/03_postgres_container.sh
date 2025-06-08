docker run -d --name pg-demo \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  postgres:15


# docker stop pg-demo
# docker rm pg-demo
# docker ps -a
# docker container prune
# sudo lsof -i -P -n | grep LISTEN
