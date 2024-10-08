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

CREATE TABLE colors (
    id SERIAL PRIMARY KEY,
    color TEXT NOT NULL
);

CREATE TABLE card_colors (
    card_id INTEGER REFERENCES cards(id),
    color_id INTEGER REFERENCES colors(id),
    PRIMARY KEY (card_id, color_id)
);

CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    name TEXT NOT NULL
);

CREATE TABLE collection_cards (
    collection_id INTEGER REFERENCES collections(id),
    card_id INTEGER REFERENCES cards(id),
    quantity INTEGER NOT NULL DEFAULT 1,
    foil BOOLEAN NOT NULL DEFAULT FALSE,
    condition TEXT,
    PRIMARY KEY (collection_id, card_id)
);
