DROP DATABASE prospects;

CREATE DATABASE prospects;

\connect prospects

CREATE TABLE team (
    name          VARCHAR (50) NOT NULL,
    city          VARCHAR (50) NOT NULL,
    code          VARCHAR (50) NOT NULL,
    team_logo_url VARCHAR (512)
);

CREATE TABLE player (
    player_id      INT NOT NULL,
    name           VARCHAR (50) NOT NULL,
    first_name     VARCHAR (50) NOT NULL,
    last_name      VARCHAR (50) NOT NULL,
    height         FLOAT,
    birthdate      DATE NOT NULL,
    active         BOOLEAN NOT NULL,
    rookie         BOOLEAN NOT NULL,
    shoots         VARCHAR (1) NOT NULL,
    weight         INT,
    position       VARCHAR (2) NOT NULL,
    player_img_url VARCHAR (512)
);
