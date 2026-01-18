from psycopg.rows import class_row

import utils.database as database
from utils import models


def run(minimal: bool):
    conn = database.pool.getconn()
    try:
        cur = conn.cursor(row_factory=class_row(models.Server))
        random_server = cur.execute("SELECT * FROM servers ORDER BY RANDOM() LIMIT 1").fetchone()
    finally:
        database.pool.putconn(conn=conn)

    if random_server is None:
        return {"error": "No servers found in database"}

    if minimal:
        return {
            "address": random_server.address,
            "port": random_server.port,
            "version": random_server.version,
            "country": random_server.country,
            "lastseen": random_server.lastseen
        }

    return {
        "address": random_server.address,
        "port": random_server.port,
        "version": random_server.version,
        "protocol": random_server.protocol,
        "software": random_server.software,
        "motd": random_server.motd,
        "country": random_server.country,
        "asn": random_server.asn,
        "org": random_server.org,
        "hostname": random_server.reversedns,
        "firstseen": random_server.firstseen,
        "lastseen": random_server.lastseen,
        "whitelist": random_server.whitelist,
        "cracked": random_server.cracked,
        "enforces_secure_chat": random_server.enforces_secure_chat,
        "prevents_reports": random_server.prevents_reports,
        "maxplayers": random_server.maxplayers,
        "onlineplayers": random_server.onlineplayers,
        "icon": random_server.icon
    }
