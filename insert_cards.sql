-- Insert sample cards
INSERT INTO cards (name, mana_cost, cmc, type_line, oracle_text, power, toughness, rarity, set_code, collector_number, colors)
VALUES
('Lightning Bolt', '{R}', 1, 'Instant', 'Lightning Bolt deals 3 damage to any target.', NULL, NULL, 'common', 'M10', '146', 'Red'),
('Serra Angel', '{3}{W}{W}', 5, 'Creature — Angel', 'Flying, vigilance', '4', '4', 'uncommon', 'DOM', '33', 'White'),
('Demonic Tutor', '{1}{B}', 2, 'Sorcery', 'Search your library for a card, put that card into your hand, then shuffle.', NULL, NULL, 'rare', 'DMR', '46', 'Black'),
('Birds of Paradise', '{G}', 1, 'Creature — Bird', '{T}: Add one mana of any color.', '0', '1', 'rare', 'M12', '165', 'Green'),
('Counterspell', '{U}{U}', 2, 'Instant', 'Counter target spell.', NULL, NULL, 'uncommon', 'DMR', '457', 'Blue'),
('Nicol Bolas, Dragon-God', '{U}{B}{B}{B}{R}', 5, 'Legendary Planeswalker — Bolas', 'Nicol Bolas, Dragon-God has all loyalty abilities of all other planeswalkers on the battlefield.', NULL, NULL, 'mythic', 'WAR', '207', 'Blue,Black,Red');
-- Create a sample collection
INSERT INTO collections (user_id, name)
VALUES (1, 'My First Collection');

-- Add cards to the collection
INSERT INTO collection_cards (collection_id, card_id, quantity, foil)
VALUES 
(1, 1, 4, false),  -- 4 non-foil Lightning Bolts
(1, 2, 1, true),   -- 1 foil Serra Angel
(1, 3, 2, false),  -- 2 non-foil Demonic Tutors
(1, 4, 1, true),   -- 1 foil Birds of Paradise
(1, 5, 3, false);  -- 3 non-foil Counterspells
(1, 6, 1, true);  -- 1 foil Nicol Bolas, Dragon-God