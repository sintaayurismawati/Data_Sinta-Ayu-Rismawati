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
    start_date timestamp not null, 
    end_date timestamp not null, 
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