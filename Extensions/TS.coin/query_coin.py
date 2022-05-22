#import os, sys
#import sqlite3
#import json
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# Path: Extensions\TS.coin\query_coin_history.py

def query(self):
    """
    Query the coin data from the database.
    """
    self.cursor.execute("""
        SELECT * FROM coin
        WHERE id = ?
    """, (self.coin_id,))
    return self.cursor.fetchone()

def update(self):
    """
    Update the coin data in the database.
    """
    self.cursor.execute("""
        UPDATE coin
        SET name = ?, symbol = ?, rank = ?, price_usd = ?, price_btc = ?,
            market_cap_usd = ?, available_supply = ?, total_supply = ?,
            max_supply = ?, percent_change_1h = ?, percent_change_24h = ?,
            percent_change_7d = ?, last_updated = ?
        WHERE id = ?
    """,
        (self.name, self.symbol, self.rank, self.price_usd, self.price_btc,
        self.market_cap_usd, self.available_supply, self.total_supply,
        self.max_supply, self.percent_change_1h, self.percent_change_24h,
        self.percent_change_7d, self.last_updated, self.coin_id))
    return self.cursor.fetchone()
    