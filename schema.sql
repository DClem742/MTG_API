-- Stores individual card information
-- Contains card attributes like name, mana cost, type, oracle text, power/toughness, rarity, set code, and collector number
-- Primary key is 'id'

CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    mana_cost TEXT,
    cmc DECIMAL(5,1),
    type_line TEXT,
    oracle_text TEXT,
    power TEXT,
    toughness TEXT,
    rarity TEXT,
    set_code TEXT,
    collector_number TEXT,
    -- image_url TEXT
);

-- Stores color information
-- Simple table with just 'id' and 'color' columns
-- Used to represent the five colors of Magic: The Gathering

CREATE TABLE colors (
    id SERIAL PRIMARY KEY,
    color TEXT NOT NULL
);

-- Junction table for the many-to-many relationship between cards and colors
-- Links cards to their respective colors
-- Uses composite primary key of card_id and color_id


CREATE TABLE card_colors (
    card_id INTEGER REFERENCES cards(id),
    color_id INTEGER REFERENCES colors(id),
    PRIMARY KEY (card_id, color_id)
);

-- Represents user-created collections of cards
-- Contains 'id', 'user_id', and 'name' columns
-- Allows users to organize their cards into named collections

CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    name TEXT NOT NULL
);

-- Junction table linking collections to cards
-- Stores information about specific cards in a collection
-- Includes quantity, foil status, and condition of cards
-- Uses composite primary key of collection_id and card_id

CREATE TABLE collection_cards (
    collection_id INTEGER REFERENCES collections(id),
    card_id INTEGER REFERENCES cards(id),
    quantity INTEGER NOT NULL DEFAULT 1,
    foil BOOLEAN NOT NULL DEFAULT FALSE,
    condition TEXT,
    PRIMARY KEY (collection_id, card_id)
);
