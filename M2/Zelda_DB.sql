CREATE DATABASE IF NOT EXISTS zelda;
USE zelda;

CREATE TABLE IF NOT EXISTS game (
    game_id INT PRIMARY KEY,
    user_name CHAR(50) NOT NULL,
    date_started DATE NOT NULL,
    hearts_remaining INT,
    total_hearts INT,
    blood_moon_countdown INT,
    blood_moon_appearances INT,
    region_char VARCHAR(20)
);


CREATE TABLE IF NOT EXISTS game_food (
    game_id INT NOT NULL,
    food_name CHAR(15) NOT NULL,
    quantity_remaining INT,
    PRIMARY KEY (game_id, food_name),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);

CREATE TABLE IF NOT EXISTS game_weapons (
    game_id INT NOT NULL,
    weapon_name CHAR(15) NOT NULL,
    equiped BOOLEAN DEFAULT false,
    lives_remaining INT,
    PRIMARY KEY (game_id, weapon_name),
    FOREIGN KEY (game_id) REFERENCES game(game_id));

CREATE TABLE IF NOT EXISTS game_enemies (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
    lifes_remaining INT,
    PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
);
CREATE TABLE IF NOT EXISTS game_sanctuaries_opened (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
	PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id));
    
CREATE TABLE IF NOT EXISTS game_chests_opened (
    game_id INT NOT NULL,
    region CHAR(20) NOT NULL,
    num INT NOT NULL,
    xpos INT,
    ypos INT,
	PRIMARY KEY (game_id, region, num),
    FOREIGN KEY (game_id) REFERENCES game(game_id)
    );