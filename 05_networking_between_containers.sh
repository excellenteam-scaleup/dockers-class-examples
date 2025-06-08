docker network create mynet
docker run -d --name db --network mynet -e POSTGRES_PASSWORD=secret postgres:15
docker run -it --network mynet postgres psql -h db -U postgres

# apt update && apt install -y iputils-ping
# How did this command work?
# ping 8.8.8.8
# ping google.com
# cat /etc/resolv.conf - to find the dns
# sudo apt install postgresql-client
# psql -h db -p 5432 -U postgres -d postgres

# -- 1. Create a table
#CREATE TABLE students (
#    id SERIAL PRIMARY KEY,
#    name TEXT NOT NULL,
#    grade INTEGER
#);
#
#-- 2. Insert some data
#INSERT INTO students (name, grade) VALUES
#('Alice', 90),
#('Bob', 82),
#('Charlie', 76);

#-- 3. Query the data
#SELECT * FROM students;
