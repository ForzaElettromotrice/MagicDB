-- To optimize the DB, include these indices
CREATE INDEX index_loyalty ON activable_ability(loyalty);
CREATE INDEX index_sacrifice ON activable_ability(sacrifice);
CREATE INDEX index_attack ON card(power);
CREATE INDEX index_defense ON card(defense);
CREATE INDEX index_mana ON card(mana_cost);
--To optimize the DB, create this materialized view
CREATE MATERIALIZED VIEW tot_mana AS
    SELECT m.red+m.black+m.white+m.snow+m.green+m.blue+m.colorless AS cost,
           m.id AS id FROM mana_cost m;