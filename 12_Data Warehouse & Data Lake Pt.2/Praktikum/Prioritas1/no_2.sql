create table users (
    id serial primary key, 
    username varchar not null,
    password varchar not null, 
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

create table categories (
    id serial primary key, 
    name varchar not null, 
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

create table posts (
    id serial primary key,
    uer_id int not null, 
    category_id int not null, 
    title varchar not null, 
    content text not null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp,
    foreign key (user_id) references users(id),
    foreign key (category_id)references categories(id)
);

create table comments (
    id serial primary key,
    post_id int not null, 
    user_id int not null, 
    content varchar not null, 
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp,
    foreign key (post_id) references posts(id),
    foreign key (user_id) references users(id)
);
