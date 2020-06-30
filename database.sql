DROP DATABASE prospects;

CREATE DATABASE prospects;

\connect prospects

CREATE TABLE team (
    id            SERIAL PRIMARY KEY,
    team_id       INT NOT NULL,
    name          VARCHAR (50) NOT NULL,
    city          VARCHAR (50) NOT NULL,
    code          VARCHAR (50) NOT NULL,
    team_logo_url VARCHAR (512)
);

CREATE TABLE player (
    id             SERIAL PRIMARY KEY,
    player_id      INT NOT NULL,
    name           VARCHAR (50) NOT NULL,
    first_name     VARCHAR (50) NOT NULL,
    last_name      VARCHAR (50) NOT NULL,
    country        VARCHAR (50),
    height         FLOAT,
    birthdate      DATE,
    active         BOOLEAN NOT NULL DEFAULT FALSE,
    rookie         BOOLEAN NOT NULL DEFAULT FALSE,
    shoots         VARCHAR (1),
    weight         INT,
    position       VARCHAR (2),
    player_img_url VARCHAR (512)
);

CREATE TABLE player_game_by_game_stats (
    id                   SERIAL PRIMARY KEY,
    player_id            INT NOT NULL,
    first_name           VARCHAR (50),
    last_name            VARCHAR (50),
    position             VARCHAR (2),
    team                 VARCHAR (5),
    date                 DATE NOT NULL,
    goals                INT DEFAULT 0,
    assists              INT DEFAULT 0,
    points               INT DEFAULT 0,
    plus_minus           INT DEFAULT 0,
    pim                  INT DEFAULT 0,
    faceoffs_won         INT DEFAULT 0,
    faceoffs_lost        INT DEFAULT 0,
    shots                INT DEFAULT 0,
    shots_on_net         INT DEFAULT 0,
    primary_assists      INT DEFAULT 0,
    secondary_assists    INT DEFAULT 0,
    pp_goals             INT DEFAULT 0,
    pp_primary_assists   INT DEFAULT 0,
    pp_secondary_assists INT DEFAULT 0,
    sh_goals             INT DEFAULT 0,
    sh_primary_assists   INT DEFAULT 0,
    sh_secondary_assists INT DEFAULT 0,
    insurance_goals      INT DEFAULT 0,
    empty_net_goals      INT DEFAULT 0,
    game_winning_goals   INT DEFAULT 0,
    game_tieing_goals    INT DEFAULT 0,
    shooting_per         INT DEFAULT 0
)
