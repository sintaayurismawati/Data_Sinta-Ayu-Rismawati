docker network create citus-cluster-d

docker run -d --name=citus_coordinator --net=citus-cluster-d -p 5432:5432 -e POSTGRES_PASSWORD=mypass citusdata/citus:12.1

docker run -d --name=citus_worker_1 --net=citus-cluster-d -e POSTGRES_PASSWORD=mypass citusdata/citus:12.1

docker run -d --name=citus_worker_2 --net=citus-cluster-d -e POSTGRES_PASSWORD=mypass citusdata/citus:12.1

docker exec -it citus_coordinator psql -U postgres

create table customer (
    id serial primary key, 
    name varchar not null, 
    address varchar not null, 
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp
    );

create table transportation (
    id serial primary key, 
    category varchar not null, 
    license_plate_number varchar not null, 
    charter_price int not null, 
    capacity int not null, 
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp
    );

create table rental(
    id serial primary key, 
    customer_id int not null, 
    transportation_id int not null, 
    start_date date not null, 
    end_date date not null, 
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp, 
    foreign key(customer_id) references customer(id), 
    foreign key(transportation_id) references transportation(id)
    );

create table payment(
    id serial primary key, 
    rental_id int not null, 
    total_payment int not null, 
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp, 
    foreign key(rental_id) references rental(id)
    );

select*from master_add_node('citus_worker_1', 5432);
select*from master_add_node('citus_worker_2', 5432);

select create_distributed_table('customer','id');
select create_distributed_table('transportation','id');
select create_distributed_table('rental','id');
select create_distributed_table('payment','id');

docker exec -it citus_worker_1 psql -U postgres 
select*from payment_102104;
select*from rental_102072;
select*from transportation_102040;
select*from customer_102008;

docker exec -it citus_worker_1 psql -U postgres
select*from customer_102009; 
select*from payment_102105;
select*from rental_102073;
select*from transportation_102041;